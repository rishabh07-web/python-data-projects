import pandas as pd

# Create dataset manually
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikas"],
    "Marks": [65, 82, 74, 91, 58],
    "Study Hours": [3, 5, 4, 6, 2],
    "Attendance": [75, 88, 80, 92, 70]
}

df = pd.DataFrame(data)

# Print full DataFrame
print("Full DataFrame:\n")
print(df)

# Print only Marks column
print("\nMarks Column:\n")
print(df["Marks"])

# Students scoring >70
print("\nStudents scoring >70:\n")
print(df[df["Marks"] > 70])

# Average marks
avg = df["Marks"].mean()
print("\nAverage Marks →", avg)

# Student with highest marks
highest_student = df.loc[df["Marks"].idxmax()]
print("\nStudent with Highest Marks:\n")
print(highest_student)