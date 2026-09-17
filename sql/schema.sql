-- NHS Healthcare Analytics
-- Suggested schema for loading the cleaned CSV into SQL.

CREATE TABLE ae_attendance (
    date DATE,
    name TEXT,
    type1_attendances INTEGER,
    type2_attendances INTEGER,
    type3_attendances INTEGER,
    total_attendances INTEGER,
    type1_within_4_hours INTEGER,
    type2_within_4_hours INTEGER,
    type3_within_4_hours INTEGER,
    percentage_within_4_hours REAL,
    emergency_admissions_type1 INTEGER,
    emergency_admissions_type2 INTEGER,
    emergency_admissions_type3_4 INTEGER,
    other_emergency_admissions INTEGER,
    patients_waiting_over_12_hours INTEGER,
    month INTEGER,
    year INTEGER,
    lat REAL,
    lon REAL
);
