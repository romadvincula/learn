# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img
# MAGIC     src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png"
# MAGIC     alt="Databricks Learning"
# MAGIC   >
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Warehousing with Databricks
# MAGIC
# MAGIC This course is designed for data professionals who want to explore the data warehousing capabilities of Databricks. Assuming no prior knowledge of Databricks, it provides an introduction to leveraging Databricks as a modern cloud-based data warehousing solution. Learners will explore how to use the Databricks Data Intelligence Platform to ingest, transform, govern, and analyze data efficiently using the industry-standard TPC-DI dataset as a reference. Learners will also explore Genie, an innovative Databricks feature that simplifies data exploration through natural language queries. 
# MAGIC
# MAGIC By the end of this course, participants will be equipped with the foundational skills to implement and optimize a data warehouse using Databricks.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ##Prerequisites
# MAGIC
# MAGIC The content was developed for participants with these skills/knowledge/abilities:
# MAGIC
# MAGIC   - Basic understanding of SQL and data querying concepts
# MAGIC   - General knowledge of data warehousing concepts, including tables, schemas, and ETL/ELT processes is recommended
# MAGIC   - Some experience with BI and/or data visualization tools is helpful but not required
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Course Agenda
# MAGIC
# MAGIC The following modules are part of the **Data Warehousing with Databricks** course by **Databricks Academy**.
# MAGIC
# MAGIC | Module Name &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Content &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|
# MAGIC | **M01 - Databricks Overview** | **Lecture -** Data Warehousing with Databricks </br> **Lecture -** Unity Catalog Overview </br> **Lecture -** Databricks SQL Warehouses </br> **Demo -** [01 - Preparing TPC-DI]($./01 - Preparing TPC-DI) | 
# MAGIC | **M02 - Ingesting and Transforming Data** | **Lecture -** Data Ingestion Techniques </br> **Lecture -** Data Transformation </br> **Demo -** [02.1 - Ingesting Data]($./02.1 - Ingesting Data) </br> **Demo -** [02.2 - Exploring Data]($./02.2 - Exploring Data) | 
# MAGIC | **M03 - Orchestration** | **Lecture -** Introduction to Lakeflow Jobs </br> **Demo -** [03 - Exploring Lakeflow Job Capabilities]($./03 - Exploring Lakeflow Job Capabilities) | 
# MAGIC | **M04 - Monitoring** | **Lecture -** Tagging </br> **Lecture -** System Tables </br> **Lecture -** Cost Optimization </br> |
# MAGIC | **M05 - Visualization** | **Lecture -** Introduction to AI/BI </br> **Demo -** [05 - Creating and Managing a Dashboard]($./05 - Creating and Managing a Dashboard) </br> **Lab -** [05L - Creating a Dashboard Lab]($./05L - Creating a Dashboard Lab) </br> |
# MAGIC | **M06 - Genie** | **Lecture -** Introduction to Genie </br> **Demo -** [06 - Creating Genie Spaces]($./06 - Creating Genie Spaces) </br> **Lab -** [06L - Genie Spaces Lab]($./06L - Genie Spaces Lab) |
# MAGIC | **M07 - Power BI Integration** | **Lecture -** Power BI Integration </br> **Lecture -** Star Schema Overview |
# MAGIC ---
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC * To run demo and lab notebooks, you need to use the following Databricks runtime: **`17.3.x-scala2.13`**
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2026 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="_blank">Apache Software Foundation</a>.<br/><br/><a href="https://databricks.com/privacy-policy" target="_blank">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use" target="_blank">Terms of Use</a> | <a href="https://help.databricks.com/" target="_blank">Support</a>