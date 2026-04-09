import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikas", "Simran",
             "Rohit", "Anjali", "Kabir", "Meena", "Arjun", "Pooja"],
    "Marks": [65, 82, 74, 91, 58, 88, 47, 76, 69, 54, 92, 61],
    "StudyHours": [3, 5, 4, 6, 2, 5, 2, 4, 3, 2, 6, 3],
    "Attendance": [75, 88, 80, 92, 70, 85, 60, 82, 78, 72, 95, 76]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# Top 3 students
top3 = df.sort_values(by="Marks", ascending=False).head(3)
print("\nTop 3 Students:\n", top3)

# Students above average
avg = df["Marks"].mean()
above_avg = df[df["Marks"] > avg]
print("\nAverage Marks →", avg)
print("Students above average →", len(above_avg))

# StudyHours > 4 vs Marks
high_study = df[df["StudyHours"] > 4]
print("\nStudents studying >4 hours:\n", high_study[["Name", "Marks"]])

# Students at risk
at_risk = df[(df["Marks"] < 50) | (df["Attendance"] < 75)]
print("\nAt Risk Students:\n", at_risk)

# Average marks per study-hour group
group = df.groupby("StudyHours")["Marks"].mean()
print("\nAverage Marks per Study Hour:\n", group)