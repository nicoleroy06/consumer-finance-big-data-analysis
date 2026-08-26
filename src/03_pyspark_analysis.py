from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ConsumerFinanceAnalysis") \
    .getOrCreate()

file_path = "data/raw/complaints.csv"

df = spark.read.csv(
    file_path,
    header=True,
    inferSchema=True,
    multiLine=True,
    quote='"',
    escape='"'
)

print("Rows:", df.count())

print("\nColumns:")
print(df.columns)

print("\nSample data:")
df.show(5, truncate=False)

spark.stop()