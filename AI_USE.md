# AI Use Documentation

## Andrew's logs

### Scope and record status

This record covers Andrew Kim's Stage IV work in `stage_iv/analysis.ipynb`, in notebook order.

ChatGPT/Codex assisted with Python code, debugging, data interpretation, visualization design, and presentation wording. I supplied the project context and mentor guidance, asked questions about the outputs, ran code during development, and selected material for the meeting. AI assistance also supported this documentation and review of the checkpoint report. 


### 1. Load the CSV, convert timestamps, and inspect data — cell 2

**Prompts →**

> why does it say file not found error in my analysis.ipynb

> why does it say rainfall_mm is null for all the values? or is it just for the first five rows? can you check?

**Reconstructed request →** Load the converted Stage IV CSV with pandas, convert UTC timestamps to Pacific time, display observations and rainfall summary statistics, and check time coverage, missing rainfall, and duplicate grid-cell hours.

**Code/output →** The cell uses `Path`, `pd.read_csv`, `pd.to_datetime(..., utc=True)`, and `.dt.tz_convert("America/Los_Angeles")`. It displays `df.head(30)` and `df["rainfall_mm"].describe()`.

**How the code was checked →** The cell contains print statements for the number of distinct hours, the missing-value fraction, and duplicate combinations of timestamp/latitude/longitude. Its saved outputs show:

- `Hours: 72`, matching the expected three days of hourly intervals.
- `Missing rainfall: 0.24742268041237114` (approximately 24.74%).
- `Duplicate grid-cell hours: 0`.
- 73,584 non-missing rainfall observations, with a maximum of 60.96 mm.

These checks show that rainfall is not null everywhere. Missing rainfall is retained as missing rather than replaced with zero. This is to differentiate missing rainfall with no rainfall. The CSV path in this cell is specific to Andrew's computer and must be adjusted for another environment.

### 2. Inspect January 22 at 10 a.m. — cell 3

**Prompts →**

> write me the code that shows some obvservaitons that don't have Null for the rainfall_mm

> write me the code for jan 22 2024 10am

> look at code block 11, give me an interpretaion of this snippet of the df

**Code/output →** The cell filters non-missing rainfall observations to the hour ending January 22, 2024 at 10 a.m. Pacific, derives `rainfall_inches = rainfall_mm / 25.4`, and displays the ten largest rainfall values for that hour.

**How the code was checked →** The displayed timestamps show 18:00 UTC and 10:00 a.m. Pacific for the same observations. The first displayed row has 40.39 mm, approximately 1.590157 inches, at latitude 32.760039 and longitude -117.183631. Dividing 40.39 by 25.4 provides a direct numerical check of the unit conversion. This observation represents the preceding one-hour interval, 9–10 a.m., at one grid cell; it is not a gauge reading or a regional mean.

**Follow-up request/status →** Andrew subsequently asked, “can you not sort by the rain but by the time”. Chronological sorting code was provided in the conversation, but the current saved cell still sorts by rainfall descending within one hour. All rows selected by this cell share that hour's timestamp.

### 3. Inspect the column names — cell 4

**Prompt →**

> alr so what are the columns and each observation in the dataset again?

**Code/output →** `print(df.columns)` displays the available columns.

**How the code was checked →** The saved output lists `hour_end_utc`, `hour_end_pacific`, `latitude`, `longitude`, and `rainfall_mm`. This confirms the names used in the filters and plots. Each observation is one geographic grid cell for the preceding hour. `rainfall_inches` is derived later rather than being an original CSV column.

### 4. Plot study-area mean rainfall — cell 5

**Prompts →**

> Alright help me brainstorm some visualizations that would be useful

> should i change the plot to use inches in order to match the units Tyler gave us?

> can you change the x axis to the 12-hour clock system as well

> okay so what exactly does the y-axis represent here. give an example so that i can understand it. also does it make sense here?

**Reconstructed request →** Plot hourly mean rainfall across the available study-area grid cells, convert millimeters to inches, label the x-axis in Pacific time with AM/PM, and print the peak hour and amount.

**Code/output →** The cell groups rainfall by `hour_end_pacific`, calculates the mean, sorts chronologically, divides by 25.4, and plots the series with matplotlib. `idxmax()` identifies the peak hour.

**How the code was checked →** The cell prints the peak hour and amount. Its saved output shows an hour ending January 22 at 10 a.m. Pacific and a peak area mean of 0.17 inches. These numbers were discussed alongside the plot to clarify that averaging across available cells smooths localized rainfall. This plot cannot establish whether an individual location crossed the mentor's extreme-rainfall threshold. The later maximum-cell plot addresses that different question.

### 5. Screen localized rainfall using hourly maxima — markdown cell 7 and code cell 8

**Prompts →**

> Wait so; isn't this **NOT extreme rainfall? how come it's only 0.17**

> okay i want something that identifies extreme rainfall and something that can go in hand with calvin's slides. i also want the plot to be easy to understand for my stakeholders that i'm presenting to.

> also what you do mean by "cells" and i saw in the markdown cell above the code for the plot, you said the the location can change each hour? how?

**Additional input →** Andrew supplied mentor guidance recommending approximately 1.2–1.5 inches in one hour as a practical screening flag for locations west of the mountains in San Diego County. The separate three-hour flag is not evaluated by this code.

**Code/output →** The code excludes missing rainfall, selects the wettest available cell each hour with `groupby(...).idxmax()`, retains its coordinates, and sorts those rows by time. The plot shades the 1.2–1.5 inch screening range and marks hours whose maximum is at least 1.2 inches. It saves `stage_iv/figures/extreme_rainfall_screening.png`.

**How the code was checked →** The code contains the explicit expectation check `assert len(wettest) == 72`. This checks that there is one selected maximum for each of the expected 72 hours. The cell also displays the flagged hours and their coordinates. Saved table outputs later in the notebook show January 22 maxima of approximately 1.59 inches for 9–10 a.m. and 2.40 inches for 3–4 p.m.

**Limitations identified during review →** The grid stays fixed, but a different cell can be the wettest each hour. The line therefore does not track one location or prove that a storm moved between the annotated coordinates. Plot annotations contain manually written values and should be checked against the calculated rows after any data changes. A rectangular study area is not a verified west-of-mountains mask. Threshold exceedances remain candidates requiring geographic and gauge checks, and do not establish terrain-induced airflow blocking.

### 6. Filter candidate observations and create a screenshot table — markdown cell 9 and code cell 10

**Prompt →**

>  can you create another cell that shows the actual values in the dataframe (by doing some filtering) to show it so that i can screen shot it and add it to my slides? also how do you know it's a coastal-area cell or an inland cell?

**Code/output →** The code filters non-missing observations at or above 1.2 inches, selects the maximum cell for each flagged hour, counts all qualifying cells for that hour, and sorts the resulting table chronologically. It displays dates, hour-ending times, rainfall, coordinates, and qualifying-cell counts, and saves `stage_iv/figures/extreme_rainfall_filtered_values.png`.

**How the code was checked →** A print statement reports `30 grid-cell hours meet >=1.2 inches across 5 hours.` The saved dataframe contains:

| Date | Hour ending (PST) | Maximum (inches, rounded) | Cells at or above 1.2 inches |
|---|---|---:|---:|
| Jan 21, 2024 | 10:00 AM | 1.27 | 1 |
| Jan 22, 2024 | 05:00 AM | 1.44 | 5 |
| Jan 22, 2024 | 10:00 AM | 1.59 | 12 |
| Jan 22, 2024 | 11:00 AM | 1.30 | 6 |
| Jan 22, 2024 | 04:00 PM | 2.40 | 6 |

The counts sum to 30, consistent with the print statement. These are 30 **cell-hour observations**, not necessarily 30 distinct locations or 30 separate storms. Coordinates are displayed instead of assigning unverified coastal/inland categories. Comparison with nearby gauges and location-specific thresholds remains future work.

## Calvin's logs
For now, I have listed the prompts that I had used to assist me in understanding and executing my analysis.
1. How do I access the NOAA COOP HPD v2 dataset https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database, and can you help me understand the data that I need?

2. Can you find two weather stations that I can pull out of the dataset to be able to compare different areas in San Diego? Preferably, ones on either side of the mountain terrains (so like one more coastal/one more inland).

3. What do the values in NOAA ISD's WND column represent? Also, how can I interpret the wind direction and speed measurements? I also heard about terms like southerly or westerly winds. Can you tell me what that means and how to interpret that?

4. Where is sea level pressure adjusted to in terms of elevation, and why is this adjustment necessary when comparing the KSAN and KIPL weather stations?

5. What can differences in atmospheric pressure between KSAN and KIPL tell us about wind patterns, and how can this be related to mountain blocking?


## Faline's logs

I mainly used Claude to help guide me through the setup of getting the dataset from the ERA-5 website: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview. The following include the prompts I used:

1. I want to pull a dataset for the San Diego region from the following website: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download. 
What are the variable selections I should do to match the following goal: Always check the box for reanalysis! To download data covering San Diego County, put in the LON and LAT as a bounding box in the geographical area down the page by checking the circle for area selection. I will recommend choosing your download to return as NetCDF4 instead of Grib which can be read by a line of code. For this dataset, you'll look at hourly winds, temperature, humidity, and IVT on a 0.25°.

2. What do I do with my API key? How do I get the initial dataset?

3. I am getting an error in my notebook related to running shell commands with pip. How do I resolve this error: 
-----------------------------
OSError                                   Traceback (most recent call last)
Cell In[3], line 2
      1 import sys
----> 2 get_ipython().system('{sys.executable} -m pip install "cdsapi>=0.7.2" xarray netcdf4 pandas numpy matplotlib')

OSError: Not available


4. I am getting the following error when trying to download the data:
HTTPError: 403 Client Error: Forbidden for url: https://cds.climate.copernicus.eu/api/retrieve/v1/processes/reanalysis-era5-single-levels/execution
cost limits exceeded
Your request is too large, please reduce your selection.
Would I be able to do only yearly for the past ten years instead of from 1940-2026? Or would that still be too much?

