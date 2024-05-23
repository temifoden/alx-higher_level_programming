-- This script prints the full description of the table first_table
SELECT TABLE_NAME, COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM information_scema.columns
WHERE table_name = 'first_table' AND table_scema = DATABASE();