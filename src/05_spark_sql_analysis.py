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

print("\nTimely response breakdown:")

spark.sql("""
    SELECT `Timely response?` AS response_status,
           COUNT(*) AS complaint_count
    FROM complaints
    WHERE `Timely response?` IS NOT NULL
    GROUP BY `Timely response?`
    ORDER BY complaint_count DESC
""").show(truncate=False)

print("\nComplaints by year:")

spark.sql("""
    SELECT YEAR(TO_DATE(`Date received`, 'MM/dd/yyyy')) AS year,
           COUNT(*) AS complaint_count
    FROM complaints
    WHERE `Date received` IS NOT NULL
    GROUP BY year
    ORDER BY year
""").show(30, truncate=False)

spark.stop()