import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/jobs.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("../dataset/cleaned_jobs.csv", index=False)

print("\nCleaned dataset saved successfully!")