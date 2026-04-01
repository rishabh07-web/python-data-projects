import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Vikas"],
    "Marks": [65, 82, 74, 91, 58],
    "StudyHours": [3, 5, 4, 6, 2],
    "Attendance": [75, 88, 80, 92, 70]
}

df = pd.DataFrame(data)

# Bar Chart
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Marks of Students")
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.show()


# Line Plot
plt.figure()
plt.plot(df["StudyHours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()


# Histogram
plt.figure()
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()