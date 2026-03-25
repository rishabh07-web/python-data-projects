import numpy as np

n = int(input("Enter number of students: "))

marks_list = []

for i in range(n):
    m = int(input("Enter mark: "))
    marks_list.append(m)

marks = np.array(marks_list)

grade_A = 0
grade_B = 0
grade_C = 0
grade_D = 0

for m in marks:
    
    if m >= 85:
        grade_A += 1
        
    elif m >= 70 and m < 85:
        grade_B += 1
        
    elif m >= 50 and m < 70:
        grade_C += 1
        
    else:
        grade_D += 1

print("\n----- Grade Report -----")
print("Grade A →", grade_A, "students")
print("Grade B →", grade_B, "students")
print("Grade C →", grade_C, "students")
print("Grade D →", grade_D, "students")