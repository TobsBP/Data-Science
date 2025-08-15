import numpy as np

# Works with int, float, string, bool, but just one type of data
arr = np.array([0, 10, "Teste"])

print(arr)

mtz = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

print(mtz)

print(mtz.sum(axis=0))  # Sum by columns
print(mtz.sum(axis=1))  # Sum by rows

print("Number of rows:", mtz.shape[0])
print("Number of columns:", mtz.shape[1])