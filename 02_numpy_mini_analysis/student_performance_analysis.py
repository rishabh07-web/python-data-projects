import numpy as np

marks = np.array([45, 67, 89, 76, 54, 91, 68, 72])
hours = np.array([2, 3, 5, 4, 3, 6, 4, 5])
attendance = np.array([70, 80, 90, 85, 75, 95, 88, 82])

# Average marks
avg_marks = np.mean(marks)
print("Average Marks →", avg_marks)

# Student with highest marks
highest_index = np.argmax(marks)
print("Highest Marks →", marks[highest_index])
print("Student Index →", highest_index)

# Students studying >4 hours
print("Students studying >4 hours (indexes) →", np.where(hours > 4)[0])

# Students with attendance <75
print("Low attendance students (indexes) →", np.where(attendance < 75)[0])

# Students scoring above average
print("Above average students (indexes) →", np.where(marks > avg_marks)[0])

# Sort marks
sorted_marks = np.sort(marks)
print("Sorted Marks →", sorted_marks)