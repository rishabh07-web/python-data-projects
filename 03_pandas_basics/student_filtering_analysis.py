import pandas as pd

# Dataset
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikas"],
    "Marks": [65, 82, 74, 91, 58],
    "StudyHours": [3, 5, 4, 6, 2],
    "Attendance": [75, 88, 80, 92, 70]
}

df = pd.DataFrame(data)

print("Full Dataset:\n", df)

# Filtering
print("\nStudents scoring >75:\n", df[df["Marks"] > 75])

print("\nStudents with attendance <80:\n", df[df["Attendance"] < 80])

print("\nStudents studying ≥4 hours:\n", df[df["StudyHours"] >= 4])

# Aggregation
avg_marks = df["Marks"].mean()
print("\nAverage Marks →", avg_marks)

highest_name = df.loc[df["Marks"].idxmax(), "Name"]
lowest_name = df.loc[df["Marks"].idxmin(), "Name"]

print("Highest Marks Student →", highest_name)
print("Lowest Marks Student →", lowest_name)

# Sorting
sorted_df = df.sort_values(by="Marks", ascending=False)
print("\nSorted by Marks (Descending):\n", sorted_df)

# New Column → Performance
df["Performance"] = "Needs Improvement"

df.loc[df["Marks"] >= 80, "Performance"] = "Excellent"
df.loc[(df["Marks"] >= 60) & (df["Marks"] <= 79), "Performance"] = "Good"

print("\nDataset with Performance Column:\n", df)