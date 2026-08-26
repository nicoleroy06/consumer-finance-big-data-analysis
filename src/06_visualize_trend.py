from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import os

spark = (
    SparkSession.builder
    .appName("ConsumerFinanceVisualization")
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

df.createOrReplaceTempView("complaints")

yearly = spark.sql("""
    SELECT YEAR(TO_DATE(`Date received`, 'MM/dd/yyyy')) AS year,
        COUNT(*) AS complaint_count
    FROM complaints
    WHERE `Date received` IS NOT NULL
    GROUP BY year
    ORDER BY year
    """)

#convert the small summarized result to Pandas for plotting
yearly_pd = yearly.toPandas()

#exclude 2026 because it is only a partial year
yearly_pd = yearly_pd[yearly_pd["year"] < 2026]

os.makedirs("images", exist_ok=True)

plt.figure(figsize=(10,6))
plt.plot(
    yearly_pd["year"],
    yearly_pd["complaint_count"],
    marker="o"
)

plt.title("CFPB Consumer Complaints by Year")
plt.xlabel("Year")
plt.ylabel("Number of Complaints")
plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"{x/1_000_000:.0f}M")
)
plt.xticks(yearly_pd["year"], rotation=45)
plt.tight_layout()

plt.savefig("images/yearly_complaint_trend.png", dpi=300)
plt.close()

spark.stop()

print("Chart saved to images/yearly_complaint_trend.png")