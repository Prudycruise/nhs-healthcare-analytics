# NHS Healthcare Analytics

An end-to-end portfolio project analysing monthly A&E attendance data for England using Python, SQL, Excel and Power BI.

## Project objectives

- Inspect and validate the source dataset.
- Analyse A&E attendance over time.
- Compare attendance across NHS organisations and department types.
- Investigate four-hour performance and long waits.
- Demonstrate a reproducible workflow across Python, SQL, Excel and Power BI.

## Repository structure

- `data/raw/` — original source data.
- `data/cleaned/` — cleaned analysis-ready data.
- `python/` — Jupyter notebooks for inspection, cleaning and exploratory analysis.
- `sql/` — SQL schema and analytical queries.
- `excel/` — Excel analysis outputs.
- `powerbi/` — Power BI dashboard files/screenshots.
- `images/` — portfolio visuals and screenshots.

## Python analysis completed so far

The Python notebook inspects the dataset, checks data quality and explores attendance patterns. Initial analysis identified the NHS organisations with the highest cumulative attendance and visualised total A&E attendance over time.

The time-series analysis highlighted unusually high monthly totals, particularly April 2019 and June 2015. A focused validation of April 2019 found that the month had a similar record count to adjacent months, no exact duplicate rows, one row per organisation in the inspected data, and internally consistent totals where Type 1 + Type 2 + Type 3 attendance equalled reported total attendance. The spike therefore remains an item for further investigation rather than being assigned an unsupported cause.

## Data-quality considerations

Inspection identified issues that should be handled or documented during cleaning, including an unnecessary index column, missing organisation names and coordinates, date-component inconsistencies, and suspicious performance values. Raw data is retained unchanged so that cleaning remains reproducible.

## Tools

- Python: pandas, matplotlib, Jupyter
- SQL
- Microsoft Excel
- Power BI
- Git and GitHub

## Status

The core portfolio project is complete and ready for trainer review. The cleaned dataset contains 27,108 records and is used across the Python, SQL, Excel and Power BI stages of the workflow.

Python was used for data inspection, cleaning, exploratory analysis and anomaly investigation. The cleaned data was loaded into SQLite and the analytical SQL queries were executed successfully against the final dataset. An Excel workbook was produced with analysis tables and charts, and a Power BI dashboard was created to present headline attendance metrics, attendance trends, top NHS organisations and long-wait patterns.

The project may be refined further following trainer feedback.

## Key principle

Findings are reported from the available data without assuming causation. Unusual values are treated as hypotheses for further investigation unless supported by additional evidence.
