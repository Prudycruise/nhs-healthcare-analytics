# Excel Analysis Workflow

This folder is reserved for the Excel stage of the NHS Healthcare Analytics project.

## Purpose

Excel provides a second way to inspect, clean, summarise and communicate the A&E dataset before or alongside SQL, Python and Power BI.

## Planned workflow

1. Import the cleaned A&E dataset into an Excel table.
2. Confirm date, text and numeric data types.
3. Remove or exclude the unnecessary exported index field (`Unnamed: 0`).
4. Check blanks and obvious data-quality issues.
5. Create PivotTables for monthly attendance and organisation-level attendance.
6. Compare Type 1, Type 2 and Type 3 attendance totals.
7. Summarise four-hour performance and long-wait measures.
8. Add clear charts suitable for a non-technical reader.

## Suggested PivotTables

### Monthly attendance
- Rows: date
- Values: Sum of Total attendances

### Top organisations
- Rows: Name
- Values: Sum of Total attendances
- Sort: largest to smallest

### Department attendance
- Values: Sum of Type 1, Type 2 and Type 3 attendance fields

### Four-hour performance
- Rows: date
- Values: Average of Percentage in 4 hours or less (all)

## Submission status

The Excel workflow is documented here so that the workbook can be produced and refined locally. The final `.xlsx` file should be added to this folder after validation.
