import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../dataset/cleaned_jobs.csv")

print("Dataset loaded successfully")

# Top paying jobs
top_jobs = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_jobs.plot(kind="bar")
plt.title("Top 10 Highest Paying Data Jobs")
plt.ylabel("Average Salary (USD)")
plt.xlabel("Job Title")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Salary by experience level
experience_salary = df.groupby("experience_level")["salary_in_usd"].mean()

plt.figure(figsize=(6,5))
experience_salary.plot(kind="bar")
plt.title("Salary by Experience Level")
plt.ylabel("Average Salary (USD)")
plt.xlabel("Experience Level")
plt.tight_layout()
plt.show()

# Remote work distribution
remote_jobs = df["remote_ratio"].value_counts()

plt.figure(figsize=(6,6))
remote_jobs.plot(kind="pie", autopct="%1.1f%%")
plt.title("Remote Work Distribution")
plt.ylabel("")
plt.show()

# Top paying countries
top_locations = df.groupby("company_location")["salary_in_usd"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_locations.plot(kind="bar")
plt.title("Top Paying Countries")
plt.ylabel("Average Salary (USD)")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()