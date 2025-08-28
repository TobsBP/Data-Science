import numpy as np

path = "/home/tobias/Documentos/Data-Science/Data/space.csv"

ds = np.loadtxt(path, delimiter=';', skiprows=1, dtype=str, encoding='utf-8')

companies = ds[0:,1]
costs = ds[0:,6]

cost_spacex = costs[companies == "SpaceX"]

cost_spacex = cost_spacex.astype(float)

max_cost = max(cost_spacex)

print(max_cost)