from pyspark.sql.functions import sum, count


gold_df = (
silver_df.groupBy("type")
.agg(
count("*").alias("total_transactions"),
sum("amount").alias("total_amount"),
sum("isFraud").alias("fraud_cases")
)
)


gold_df.write.format("delta") \
.mode("overwrite") \
.save("/Volumes/workspace/default/my_data_volume/gold/fraud_metrics/paysim_transactionsmnt")

# COMMAND ----------

display(gold_df)