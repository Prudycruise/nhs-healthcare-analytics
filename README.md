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

This is a working portfolio submission. The core Python exploration and repository structure are in place; SQL, Excel, Power BI and final cleaning artefacts are being developed iteratively and may be refined following review.

## Key principle

Findings are reported from the available data without assuming causation. Unusual values are treated as hypotheses for further investigation unless supported by additional evidence.
