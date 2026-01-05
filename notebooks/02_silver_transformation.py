from pyspark.sql.functions import col
from pyspark.sql.types import DoubleType, IntegerType


silver_df = (
spark.read.format("delta")
.load("/Volumes/workspace/default/my_data_volume/paysim_transactions")
.filter(col("amount") > 0)
.dropDuplicates()
.withColumn("amount", col("amount").cast(DoubleType()))
.withColumn("isFraud", col("isFraud").cast(IntegerType()))
)


silver_df.write.format("delta") \
.mode("overwrite") \
.save("/Volumes/workspace/default/my_data_volume/silver/transactions_clean/paysim_transactions")

# COMMAND ----------

display(silver_df)