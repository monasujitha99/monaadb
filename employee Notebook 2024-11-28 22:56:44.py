# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE Employee (
# MAGIC     EmployeeID INT PRIMARY KEY,        -- Unique identifier for each employee
# MAGIC     FirstName VARCHAR(50) NOT NULL,  -- Employee's first name
# MAGIC     LastName VARCHAR(50) NOT NULL,   -- Employee's last name
# MAGIC     Department VARCHAR(50),          -- Department the employee belongs to
# MAGIC     Email VARCHAR(100),              -- Email address of the employee
# MAGIC     Phone VARCHAR(15)                -- Contact number
# MAGIC );
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO Employee (EmployeeID, FirstName, LastName, Department, Email, Phone)
# MAGIC VALUES
# MAGIC (1, 'John', 'Doe', 'HR', 'john.doe@example.com', '123-456-7890'),
# MAGIC (2, 'Jane', 'Smith', 'Finance', 'jane.smith@example.com', '987-654-3210'),
# MAGIC (3, 'Alice', 'Johnson', 'IT', 'alice.johnson@example.com', '555-123-4567'),
# MAGIC (4, 'Bob', 'Williams', 'Marketing', 'bob.williams@example.com', '444-555-6666'),
# MAGIC (5, 'Emma', 'Brown', 'Sales', NULL, '333-444-5555'); -- No email provided
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employee
