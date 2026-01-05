bronze_df = (
spark.read
.option("header", "true")
.option("inferSchema", "true")
.csv("/Volumes/workspace/default/my_data_volume/PS_20174392719_1491204439457_log.csv")
)


bronze_df.write.format("delta") \
.mode("overwrite") \
.save("/Volumes/workspace/default/my_data_volume/paysim_transactions")

# COMMAND ----------

display(bronze_df)