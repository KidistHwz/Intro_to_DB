-- Use the database passed as an argument
USE alx_book_store;

-- Retrieve the structure of the Books table using information_schema
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Books' AND TABLE_SCHEMA = 'alx_book_store';
