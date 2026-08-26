# Consumer Finance Big Data Analysis

A large-scale analysis of the **Consumer Financial Protection Bureau (CFPB) Consumer Complaint Database** using Python, PySpark, and Spark SQL.

This project explores complaint patterns across more than **17.3 million consumer records**, including the most common financial products, companies receiving the most complaints, geographic patterns, company response behavior, and changes in complaint volume over time.

## Project Questions

This project explores:

- Which financial products generate the most consumer complaints?
- Which companies receive the highest complaint volumes?
- Which states report the most complaints?
- How often do companies provide timely responses?
- How has complaint volume changed over time?

## Data Source

This project uses the public **Consumer Financial Protection Bureau (CFPB) Consumer Complaint Database**.

The downloaded dataset contained approximately **17.3 million complaint records** at the time of analysis.

The raw CSV is not included in this repository because of its large file size. The `data/` directory is excluded through `.gitignore`.

## Tools & Skills

- Python
- PySpark
- Spark SQL
- Pandas
- Matplotlib
- Large-scale data analysis
- Data aggregation
- Data visualization
  
## Key Findings

- Analyzed approximately **17.3 million consumer complaints** using PySpark and Spark SQL.
- Credit-reporting complaints dominated the dataset, with TransUnion, Equifax, and Experian having the highest complaint counts.
- Complaint volume increased sharply in recent years, rising from about **800,000 complaints in 2022** to more than **5.4 million in 2025**.
- Companies recorded timely responses for the overwhelming majority of complaints.
  
## Complaint Trend

The CFPB Consumer Complaint Database shows a sharp increase in complaint volume in recent years, especially from 2022 through 2025.

![CFPB Consumer Complaints by Year](images/yearly_complaint_trend.png)

> 2026 is excluded from the chart because the dataset contains only a partial year.

## Repository Structure

```text
consumer-finance-big-data-analysis/
│
├── src/
│   ├── 01_data_inspection.py
│   ├── 02_basic_analysis.py
│   ├── 03_pyspark_analysis.py
│   ├── 04_pyspark_summary.py
│   ├── 05_spark_sql_analysis.py
│   └── 06_visualize_trend.py
│
├── images/
│   └── yearly_complaint_trend.png
│
├── requirements.txt
├── README.md
└── .gitignore
```
