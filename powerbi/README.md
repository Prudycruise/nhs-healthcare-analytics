# Power BI Dashboard Plan

This folder is reserved for the Power BI stage of the NHS Healthcare Analytics project.

## Dashboard objectives

The dashboard is intended to provide an accessible summary of A&E activity and performance using the cleaned dataset produced during the project.

## Planned visuals

- KPI card: total A&E attendances
- KPI card: average percentage seen within four hours
- Line chart: total attendances by month
- Bar chart: top NHS organisations by attendance
- Department comparison: Type 1, Type 2 and Type 3 attendances
- Trend visual: four-hour performance over time
- Table/bar chart: patients spending more than 12 hours from decision to admit to admission
- Date and organisation filters where appropriate

## Suggested measures

```DAX
Total Attendances = SUM('AE Attendance'[Total attendances])

Average 4 Hour Performance = AVERAGE('AE Attendance'[Percentage in 4 hours or less (all)])

Patients Over 12 Hours = SUM('AE Attendance'[Number of patients spending >12 hours from decision to admit to admission])
```

## Submission status

The analytical questions and dashboard specification are documented. The `.pbix` dashboard is a local Power BI deliverable and should be added here once built and reviewed.

The dashboard should not assign causes to unusual attendance changes without supporting evidence; anomalous periods identified in Python should instead be highlighted for further investigation.
