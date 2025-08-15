import numpy as np

np.random.seed(10)

arr = np.random.randint(1, 51, (4 , 4))

print("Array:")
print(arr)

print("Median X:", np.median(arr, axis=0))
print("Median Y:", np.median(arr, axis=1))

print("Max value from X:", np.max(arr, axis=0))
print("Max value from Y:", np.max(arr, axis=1))

print("Quantity of each number:", np.unique(arr, return_counts=True)) 

unique_numbers, counts = np.unique(arr, return_counts=True)
print("Numbers that appear exactly 2 times:", unique_numbers[counts == 2])