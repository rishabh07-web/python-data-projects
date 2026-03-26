import numpy as np

marks = np.array([45, 67, 89, 23, 76, 54, 91, 68, 72, 60])

# Statistical Operations
mean = np.mean(marks)
median = np.median(marks)
std_dev = np.std(marks)
variance = np.var(marks)

print("Mean →", mean)
print("Median →", median)
print("Standard Deviation →", std_dev)
print("Variance →", variance)

# Logical Analysis
above_75 = np.sum(marks > 75)
below_40 = np.sum(marks < 40)
index_highest = np.argmax(marks)
sorted_marks = np.sort(marks)

print("\nStudents scoring above 75 →", above_75)
print("Students scoring below 40 →", below_40)
print("Index of highest marks →", index_highest)
print("Sorted Dataset →", sorted_marks)

# Transformation
grace_marks = marks + 5
print("\nMarks after Grace (+5) →", grace_marks)

# Grade Creation
grades = np.empty(len(marks), dtype=str)

grades[marks > 80] = 'A'
grades[(marks >= 60) & (marks <= 80)] = 'B'
grades[marks < 60] = 'C'

print("Grades →", grades)