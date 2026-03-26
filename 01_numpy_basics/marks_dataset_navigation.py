import numpy as np

marks = np.array([45, 67, 89, 23, 76, 54, 91, 68, 72, 60])

# First 4 marks
print("First 4 Marks →", marks[:4])

# Last 2 marks
print("Last 2 Marks →", marks[-2:])

# Marks from index 2 to 7
print("Index 2 to 7 →", marks[2:8])

# Alternate marks
print("Alternate Marks →", marks[::2])

# Marks greater than 70
print("Marks > 70 →", marks[marks > 70])

# Mean of dataset
print("Mean →", np.mean(marks))

# Max & Min
print("Max →", np.max(marks))
print("Min →", np.min(marks))