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


## ERA-5 Analysis

### Overview

In this dataset, we visualize a reanalysis project from the European Center for Medium Range Weather Forecast (ECMWF), which takes in decades of historical data from surface to atmospheric levels. It is important to note that the ERA-5 dataset is on a 25 degree grid scale, or 25 km scale, so it smooths out events that are extreme and localized, and is better for visualizing long term events that happen on a bigger scale.

### Data Access

The data is derived from Copernicus Data Storage (CSD) but is originally collected from the ECMWF.

Data source: [https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download)

Here, you can choose from different variables for the dataset. In our case, we included the variables: 10m u-component of wind, 10m v-component of wind, and Total precipitation. You must create an account with the CDS and get an API key to access the data.

### Initial Analysis
For our initial analysis, we graphed the daily wind speed and precipitation levels in San Diego county for 2024, and the hourly precipitation levels for the January 21-23, 2024 floods that happened in San Diego. Our findings support the limitations of this dataset.


## NCEP/EMC Stage IV Precipitation Analysis

### Overview and Screening Method

Our initial Stage IV analysis examined hourly precipitation estimates on approximately 4-kilometer grid cells during January 21–23, 2024. We used 1.2 inches in one hour as an initial screening threshold to identify candidate heavy-rainfall hours. Confirming extreme events requires checking whether locations fall within the intended western San Diego region and comparing estimates with location-specific thresholds and nearby gauges. These candidate hours guide further investigation of conditions associated with extreme rainfall, with the goal of supporting flood preparedness.

## Appendix: AI and Human Contributions

*Placeholder — to be completed by the team before submission.*

- **Human contributions:** [Describe each team member's work and review of the results.]
- **AI contributions:** [Describe AI assistance with code, debugging, analysis, and report writing, where applicable.]
- **Validation:** [Describe how AI-assisted code and results were checked or tested.]

Detailed prompts, uses of generated output, and verification notes will be documented in [AI_USE.md](AI_USE.md).
