import numpy as np

one_arr = np.ones(8)

random_arr = np.random.randint(0, 10, 8)

sum_arr = one_arr + random_arr

if sum_arr.sum() >= 40:
    sum_arr = sum_arr.reshape(4, 2)
else:
    sum_arr = sum_arr.reshape(2, 4)

print(sum_arr)