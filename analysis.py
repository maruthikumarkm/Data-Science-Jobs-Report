import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../dataset/cleaned_jobs.csv")

print("Dataset loaded successfully\n")

# Top 10 highest paying job roles
top_jobs = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(10)

print("Top 10 Highest Paying Jobs:\n")
print(top_jobs)

# Average salary by company location
location_salary = df.groupby("company_location")["salary_in_usd"].mean().sort_values(ascending=False).head(10)

print("\nTop Paying Locations:\n")
print(location_salary)

# Experience level salary
experience_salary = df.groupby("experience_level")["salary_in_usd"].mean()

print("\nSalary by Experience Level:\n")
print(experience_salary)

# Remote job distribution
remote_jobs = df["remote_ratio"].value_counts()

print("\nRemote Work Distribution:\n")
print(remote_jobs)