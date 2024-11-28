# Databricks notebook source
# MAGIC %sql
# MAGIC -- Create Customer Table
# MAGIC CREATE TABLE Customer (
# MAGIC     CustomerID INT PRIMARY KEY,       -- Unique identifier for each customer
# MAGIC     FirstName VARCHAR(50) NOT NULL, -- Customer's first name
# MAGIC     LastName VARCHAR(50) NOT NULL,  -- Customer's last name
# MAGIC     Email VARCHAR(100),    
# MAGIC     phone varchar(100)   
# MAGIC     );     
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO Customer (CustomerID, FirstName, LastName, Email, Phone)
# MAGIC VALUES
# MAGIC (1, 'John', 'Doe', 'john.doe@example.com', '123-456-7890'),
# MAGIC (2, 'Jane', 'Smith', 'jane.smith@example.com', '987-654-3210'),
# MAGIC (3, 'Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567'),
# MAGIC (4, 'Bob', 'Williams', 'bob.williams@example.com', NULL), -- No phone number
# MAGIC (5, 'Emma', 'Brown', NULL, '444-555-6666'); -- No email address
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from customer
