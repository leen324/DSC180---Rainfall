## NOAA ISD Analysis

### Overview

In this dataset, we perform analysis through NOAA's Integrated Surface Database (ISD), which uses historical weather observations to explore San Diego County's atmospheric pressure and wind patterns (such as pressure and direction) during the three-day period of January 21-23, 2024. In particular, two locations/weather stations were explored, that being the San Diego International Airport (KSAN) and Imperial County Airport (KIPL). It is important to note that KSAN is a coastal region that is located west of mountain terrain in San Diego, while KIPL is east of the mountains and more inland. Comparing these stations is crucial in investigating patterns between coastal and inland sea-level pressure, as well as wind speed/direction at KSAN specifically.

### Data Access

The data is derived from NOAA's Integrated Surface Database (ISD).

Data source: https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database

Here, you can launch data access in the global hourly section and filter out data based on the location and certain time frames.

For this particular notebook, we require the two following CSV files:

- `72290023188.csv` — KSAN observations (San Diego International Airport)
- `74718503144.csv` — KIPL observations (Imperial County Airport)

Both CSV files have been placed in the same directory as `analysis.ipynb`. The files must contain the historical observations covering January 21–23, 2024. It also requires the inclusion of `DATE`, `SLP`, and `WND` fields.

### Software Dependencies

The analysis was executed/developed using Python 3.12.11 and requires three things:

- pandas
- matplotlib
- Jupyter Notebook

If one requires the packages in attempts to replicate the data, said packages can be installed with this command:

`python -m pip install pandas matplotlib notebook`

### Running the Analysis

Starting off, one must clone the project repository:

`git clone https://github.com/leen324/DSC180---Rainfall.git`

For analysis using this dataset specifically, navigate over to the NOAA ISD analysis folder:

`cd DSC180---Rainfall/data/NOAA_ISD_Analysis`

One must make sure that both CSV files and `analysis.ipynb` are located in this folder. If this is not the case, one can download it by accessing the data with the description above.

Once done, a Jupyter Notebook can be launched through the following command:

`python -m notebook`

It is then, one can open `analysis.ipynb` and select **Run All Cells** to reproduce the entire analysis.

## NCEP/EMC Stage IV Rainfall Analysis

### Data Access

Use the [UCAR Stage IV catalog](https://data.ucar.edu/dataset/ncep-emc-4km-gridded-data-grib-stage-iv-data), which links to the [GDEX archive](https://gdex.ucar.edu/datasets/d507005/). In Data Access, open the ST4 GRIB/GRIB2 file listing, select the `stage4.2024` directory, and download **`stage4.202401.tar`** for January 2024. Follow any archive sign-in prompts if required.

Store the downloaded archive at `stage_iv/data/stage4.202401.tar`. Keep its original filename and format; the conversion script reads the archive directly. Raw and generated data are excluded from Git, so each user must obtain or generate them locally.

### Dependencies

Use Python 3.12 with pandas, xarray, cfgrib, ecCodes, matplotlib, Jupyter Notebook, and ipykernel. From a terminal with conda installed:

```bash
conda create -n rainfall -c conda-forge python=3.12 pandas xarray cfgrib eccodes matplotlib notebook ipykernel
conda activate rainfall
python -m ipykernel install --user --name rainfall --display-name "Python (rainfall)"
```

### Reproduce the Notebook

Run these commands from the repository root after downloading the archive:

```bash
conda activate rainfall
python stage_iv/convert_stage_iv.py
python -m notebook
```

The conversion script extracts 72 hourly GRIB files into `stage_iv/data/hourly/` and writes `stage_iv/data/san_diego_stage_iv_jan21_23_2024.csv`. It selects the January 21–23, 2024 Pacific-time rainfall intervals within latitude 32.4–33.6°N and longitude 117.7–116.0°W. The area is a rectangle, not an exact county or west-of-mountains boundary.

Open `stage_iv/analysis.ipynb`, select the **Python (rainfall)** kernel, and restart the kernel and run all cells from top to bottom. In VS Code, open the repository folder, open the same notebook, select the `rainfall` environment, and use **Run All**. Conversion is only necessary if the CSV has not already been generated.

The notebook locates the repository from its working directory and uses `stage_iv/data/san_diego_stage_iv_jan21_23_2024.csv`; it does not require Andrew's personal filesystem path. Launch Jupyter from the repository root or a folder inside it. If the data file is missing, rerun the conversion step and check the archive's location.

Expected inspection outputs include 72 unique hour-ending timestamps, zero duplicate grid-cell hours, and approximately 24.74% missing rainfall. Missing values remain missing, rather than becoming zero. The filtered table contains five candidate hours and 30 qualifying cell-hour observations. The notebook saves plots to `stage_iv/figures/extreme_rainfall_screening.png` and `stage_iv/figures/extreme_rainfall_filtered_values.png`.

### Screening and Interpretation

One observation represents one approximately 4 km grid cell for the hour preceding its timestamp. Pacific times are derived from UTC, and rainfall in inches is calculated as `rainfall_mm / 25.4`. We use 1.2 inches in one hour as an initial screening threshold, based on the mentor's approximate 1.2–1.5 inch range for locations west of the mountains. Confirming extremes requires location-specific thresholds, verifying the intended geographic region, and comparison with nearby rain gauges. The hourly maximum can come from a different cell each hour; it does not track one fixed location or establish terrain-induced airflow blocking.

## Appendix: AI and Human Contributions

### Andrew Kim
- **Human contribution:** Selected and interpreted Stage IV rainfall results, refined visualizations using mentor guidance, and prepared meeting slides.
- **AI contribution:** Assisted with data conversion, notebook code, debugging, visualization design, and explanatory writing.
- **Validation:** Inspected dataframe outputs, checked 72-hour coverage and duplicate rows, reviewed missing values and unit conversions, and compared filtered values with plots.

### Calvin Truong
- **Human contribution:** [To be added.]
- **AI contribution:** [To be added, or state no AI use.]
- **Validation:** [To be added.]

### Faline Le
- **Human contribution:** [To be added.]
- **AI contribution:** [To be added, or state no AI use.]
- **Validation:** [To be added.]

See [AI_USE.md](AI_USE.md) for detailed prompts and verification notes.
