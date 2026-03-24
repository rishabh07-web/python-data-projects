import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(f"Array = {arr}")

print("Shape =", np.shape(arr))
print("Size =", np.size(arr))
print("Data Type =", arr.dtype)

new_arr = arr * 2
print(f"New Array = {new_arr}")