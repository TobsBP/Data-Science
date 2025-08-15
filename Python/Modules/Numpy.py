import numpy as np

numbers = np.array([1, 2, 3, 4, 5]) # Mutable array

numbers[:3]  # Slicing the array

numbers_modfied = numbers[2:] # Slicing from index 2 to the end

length_of_array = len(numbers_modfied)  # Getting the length of the sliced array

ones = np.ones((2, 3))  # Creating a 2x3 array of ones

print(ones)