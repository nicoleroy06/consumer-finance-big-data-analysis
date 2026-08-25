import pandas as pd

file_path = "data/raw/complaints.csv"

# Read only a small sample for quick inspection
df = pd.read_csv(file_path, nrows=1000)

print("Sample rows loaded:", len(df))

print("\nColumns:")
for col in df.columns:
    print("-", col)

print("\nFirst 5 rows:")
print(df.head())