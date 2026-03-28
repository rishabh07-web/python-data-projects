import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikas"],
    "Marks": [65, 82, 74, 91, 58],
    "StudyHours": [3, 5, 4, 6, 2],
    "Attendance": [75, 88, 80, 92, 70]
}

df = pd.DataFrame(data)

# Creating Grade Column
df["Grade"] = "C"

df.loc[df["Marks"] >= 80, "Grade"] = "A"
df.loc[(df["Marks"] >= 60) & (df["Marks"] <= 79), "Grade"] = "B"

print("Dataset with Grades:\n")
print(df)


# Group Analysis
group = df.groupby("Grade")["Marks"].agg(["mean", "count"])

print("\nGrouped Analysis:\n")
print(group)


# Insight Output
print("\nGrade Insights:")

for grade, row in group.iterrows():
    print(f"Grade {grade} → avg marks {row['mean']} , students {row['count']}")