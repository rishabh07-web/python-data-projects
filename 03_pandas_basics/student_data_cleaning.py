import pandas as pd
import numpy as np

# Create dataset with NaN values
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, np.nan, 72, 60, 95],
    "StudyHours": [5, 3, np.nan, 2, 6],
    "Attendance": [90, 80, 85, np.nan, 92]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Detect missing values
print("\nMissing Values:\n")
print(df.isnull())


# Fill Marks with average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill StudyHours with median
df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].median())

# Fill Attendance with fixed value
df["Attendance"] = df["Attendance"].fillna(70)

# Print cleaned dataset
print("\nCleaned Dataset:\n")
print(df)