from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("ConsumerFinanceSQL")
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

#make the spark dataframe available to SQL
df.createOrReplaceTempView("complaints")

print("\nTop 10 states by complaint count:")

spark.sql("""
    SELECT State, COUNT(*) AS complaint_count
    FROM complaints
    WHERE State IS NOT NULL
    GROUP BY State
    ORDER BY complaint_count DESC
    LIMIT 10
""").show(truncate=False)

spark.stop()