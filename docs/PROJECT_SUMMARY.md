# Project Review Summary

## Scope

This portfolio project analyses monthly A&E attendance data for England and demonstrates an end-to-end analytics workflow across Python, SQL, Excel and Power BI.

## Work completed

- Raw NHS A&E attendance dataset added to the repository.
- Initial data-quality inspection completed in Jupyter.
- Top NHS organisations by cumulative attendance analysed and visualised.
- Total A&E attendance over time analysed and visualised.
- Unusual monthly attendance totals investigated using targeted validation checks.
- SQL schema and core analytical queries added.
- Repository README expanded with objectives, findings and limitations.

## Current Python findings

The attendance time series shows substantial variation over the period, with unusually high aggregate values in April 2019 and June 2015.

A focused investigation of April 2019 found:

- 234 records, similar to March 2019 (235) and May 2019 (231).
- No exact duplicated rows.
- Each organisation appeared once in the inspected month.
- No single organisation had an attendance value large enough to explain the overall spike by itself.
- Reported total attendance matched the sum of Type 1, Type 2 and Type 3 attendance for the inspected records.

The available checks therefore do not establish the cause of the spike. It is documented as an item for further investigation rather than assigned an unsupported explanation.

## Data-quality issues identified

- An unnecessary `Unnamed: 0` index column is present in the source data.
- Some organisation names are missing.
- Latitude and longitude contain missing values.
- Some month/year fields may not align with the parsed date.
- Some four-hour performance values require validation before interpretation.

## Review priorities

The main portfolio workflow is complete. Further review can focus on:

1. Refining notebook presentation and removing unnecessary debug outputs.
2. Reviewing the identified attendance anomalies and data-quality limitations.
3. Improving dashboard presentation where useful.
4. Incorporating trainer feedback into future iterations.

## Submission note

This is an iterative review version intended for trainer feedback. The project deliberately distinguishes observed patterns from causal explanations and documents areas requiring further validation.
