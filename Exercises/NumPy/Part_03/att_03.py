import numpy as np

path = "/home/tobias/Documentos/Data-Science/Data/space.csv"

ds = np.loadtxt(path, delimiter=';', skiprows=1, dtype=str, encoding='utf-8')

missions = ds[0:,2]

cont = np.sum(np.char.find(missions, "USA") != -1)

print(cont)