import numpy as np

even_arr = np.arange(0, 51, 2)

odd_arr = np.arange(100, 50, -2)

new_arr = np.concatenate([even_arr, odd_arr])

print(np.sort(new_arr))