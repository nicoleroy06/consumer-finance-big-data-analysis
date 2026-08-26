import pandas as pd

file_path = "data/raw/complaints.csv"

#load a manageable sample for basic analysis
df = pd.read_csv(file_path, nrows=100000, low_memory=False)

print("Rows loaded:", len(df))

print("\nTop 10 complaint products:")
print(df["Product"].value_counts().head(10))

print("\nTop 10 companies by number of complaints:")
print(df["Company"].value_counts().head(10))

print("\nComplaint submission methods:")
print(df["Submitted via"].value_counts())

print("\nTimely response breakdown:")
print(df["Timely response?"].value_counts())