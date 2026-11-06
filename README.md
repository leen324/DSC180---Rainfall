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

## Appendix: AI and Human Contributions

*Placeholder — to be completed by the team before submission.*

- **Human contributions:** [Describe each team member's work and review of the results.]
- **AI contributions:** [Describe AI assistance with code, debugging, analysis, and report writing, where applicable.]
- **Validation:** [Describe how AI-assisted code and results were checked or tested.]

Detailed prompts, uses of generated output, and verification notes will be documented in [AI_USE.md](AI_USE.md).
