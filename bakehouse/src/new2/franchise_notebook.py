# Databricks notebook source
# MAGIC %md
# MAGIC # Default notebook
# MAGIC
# MAGIC This default notebook is executed using a Lakeflow job as defined in resources/sample_job.job.yml.

# COMMAND ----------

# Set default catalog and schema (create if they don't exist)
catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
spark.sql(f"CREATE CATALOG IF NOT EXISTS `{catalog}`")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{catalog}`.`{schema}`")
spark.sql(f"USE CATALOG `{catalog}`")
spark.sql(f"USE SCHEMA `{schema}`")

# COMMAND ----------

# Create the customer_360 table in the target catalog/schema (set via widgets above)
spark.sql(f"""
    CREATE TABLE IF NOT EXISTS `{catalog}`.`{schema}`.franchises_analytics
    AS select country,count(*) franchise_count  from samples.bakehouse.sales_franchises group by country
""")

