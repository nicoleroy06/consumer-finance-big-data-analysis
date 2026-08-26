from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = (
    SparkSession.builder
    .appName("ConsumerFinanceSummary")
    .getOrCreate()
)

file_path = "data/raw/complaints.csv"

df = spark.read.csv(
    file_path,
    header=True,
    inferSchema=True,
    multiLine=True,
    quote='"',
    escape='"'
)

print("\nTop 10 complaint products:")

df.groupBy("product") \
    .count() \
    .orderBy(col("count").desc()) \
    .show(10, truncate=False)

spark.stop()