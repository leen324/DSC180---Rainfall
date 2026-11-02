from pathlib import Path
from datetime import datetime
import io
import tarfile

import pandas as pd
import xarray as xr

# Locate data relative to this script.
folder = Path(__file__).resolve().parent
archive = folder / "data" / "stage4.202401.tar"
hourly = folder / "data" / "hourly"
hourly.mkdir(parents=True, exist_ok=True)

# Hour-ending UTC timestamps covering Jan. 21–23 in Pacific time.
start = datetime(2024, 1, 21, 9)
end = datetime(2024, 1, 24, 8)

tables = []

with tarfile.open(archive) as month:
    for day in range(21, 25):
        daily_bytes = month.extractfile(f"ST4.202401{day:02d}").read()

        with tarfile.open(fileobj=io.BytesIO(daily_bytes)) as daily:
            for member in daily:
                name = Path(member.name).name

                if not (
                    name.startswith("st4_conus.")
                    and name.endswith(".01h.grb2")
                ):
                    continue

                timestamp = datetime.strptime(
                    name.split(".")[1], "%Y%m%d%H"
                )
                if not start <= timestamp <= end:
                    continue

                path = hourly / name
                path.write_bytes(daily.extractfile(member).read())

                with xr.open_dataset(
                    path,
                    engine="cfgrib",
                    backend_kwargs={"indexpath": ""},
                ) as ds:
                    # Convert longitude to the -180 to 180 convention.
                    lon = (ds.longitude + 180) % 360 - 180
                    ds = ds.assign_coords(longitude=lon)

                    # Rectangular area around San Diego County.
                    area = (
                        (ds.latitude >= 32.4)
                        & (ds.latitude <= 33.6)
                        & (ds.longitude >= -117.7)
                        & (ds.longitude <= -116.0)
                    )

                    variable = next(iter(ds.data_vars))
                    rain = ds[variable]
                    units = rain.attrs.get("units", "")
                    if units not in {"kg m**-2", "kg m-2", "mm"}:
                        raise ValueError(f"Check precipitation units: {units}")

                    table = (
                        rain.where(area, drop=True)
                        .to_dataframe(name="rainfall_mm")
                        .reset_index()
                    )

                    # Remove cells outside the rectangle while retaining
                    # missing rainfall values inside the rectangle.
                    table = table[
                        table.latitude.between(32.4, 33.6)
                        & table.longitude.between(-117.7, -116.0)
                    ].copy()

                    table["hour_end_utc"] = pd.Timestamp(
                        timestamp, tz="UTC"
                    )
                    table["hour_end_pacific"] = (
                        table["hour_end_utc"]
                        .dt.tz_convert("America/Los_Angeles")
                    )

                    tables.append(table[[
                        "hour_end_utc",
                        "hour_end_pacific",
                        "latitude",
                        "longitude",
                        "rainfall_mm",
                    ]])

                print(f"Converted {name}")

if len(tables) != 72:
    raise ValueError(f"Expected 72 hourly files; found {len(tables)}")

result = pd.concat(tables, ignore_index=True)
output = folder / "data" / "san_diego_stage_iv_jan21_23_2024.csv"
result.to_csv(output, index=False)

print(f"\nSaved {len(result):,} rows to:\n{output}")
print(result.head())