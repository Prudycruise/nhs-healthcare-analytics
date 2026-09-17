-- NHS Healthcare Analytics
-- Core SQL analysis queries
-- Assumes the cleaned dataset has been loaded into a table named ae_attendance.

-- 1. Total A&E attendance over time
SELECT
    date,
    SUM(total_attendances) AS total_attendances
FROM ae_attendance
GROUP BY date
ORDER BY date;

-- 2. NHS organisations with the highest cumulative attendance
SELECT
    name,
    SUM(total_attendances) AS total_attendances
FROM ae_attendance
WHERE name IS NOT NULL
GROUP BY name
ORDER BY total_attendances DESC
LIMIT 10;

-- 3. Attendance by department type
SELECT
    SUM(type1_attendances) AS type1_attendances,
    SUM(type2_attendances) AS type2_attendances,
    SUM(type3_attendances) AS type3_attendances
FROM ae_attendance;

-- 4. Average four-hour performance over time
SELECT
    date,
    AVG(percentage_within_4_hours) AS avg_four_hour_performance
FROM ae_attendance
WHERE percentage_within_4_hours IS NOT NULL
GROUP BY date
ORDER BY date;

-- 5. Organisations with the most >12-hour waits
SELECT
    name,
    SUM(patients_waiting_over_12_hours) AS patients_waiting_over_12_hours
FROM ae_attendance
WHERE name IS NOT NULL
GROUP BY name
ORDER BY patients_waiting_over_12_hours DESC
LIMIT 10;
