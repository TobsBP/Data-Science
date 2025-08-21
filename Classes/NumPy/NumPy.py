import numpy as np

# Works with int, float, string, bool, but just one type of data
arr = np.array([0, 10, "Teste"])

(arr)

mtz = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

(mtz)

(mtz.sum(axis=0))  # Sum by columns
(mtz.sum(axis=1))  # Sum by rows

("Number of rows:", mtz.shape[0])
("Number of columns:", mtz.shape[1])

# Class notes Part 2

mtz = np.arange(1,10, 1).reshape(3, 3)  # Create a 3x3 matrix

mtz                 # print the matrix

mtz[2]              # Extracting the third row

mtz[:, 1]           # Extracting the second column

mtz[:, 1:]          # Extracting the second and third columns

(mtz > 5)           # Extracting all elements bigger than 5, bool

(mtz[mtz > 5])      # Extracting all elements bigger than 5, int

(mtz[mtz %2 == 0])  # Extracting all elements pair

arr = np.array(['Goku', 'Gohan','Goten', 'Trunks', 'Bulma'])

print(arr)

print(np.char.find(arr, 'ha')) # Print the position in the string

print(np.char.find(arr, 'ha') >= 0) # Print the mask

print(arr[np.char.find(arr, 'ha') >= 0]) # Print with the mask

arr = np.char.upper(arr)

print(arr)