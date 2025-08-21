import numpy as np

path = "/home/tobias/Documentos/Data-Science/Data/space.csv"

ds = np.loadtxt(path, delimiter=';', skiprows=1, dtype=str, encoding='utf-8')

# Get the colluns
print(ds[0, ])

# Get only the collun cost
ds_cost = ds[1:,6]

# Transforming the values in float
ds_cost = ds_cost.astype(float)

# Get the median
print(ds_cost.mean())