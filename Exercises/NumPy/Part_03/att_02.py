import numpy as np

path = "/home/tobias/Documentos/Data-Science/Data/space.csv"

ds = np.loadtxt(path, delimiter=';', skiprows=1, dtype=str, encoding='utf-8')

cost_col = ds[:,6]

cost_col = cost_col.astype(float)

total_cost = np.sum(cost_col > 0)

print(total_cost)