import numpy as np

path = "/home/tobias/Documentos/Data-Science/Data/space.csv"

ds = np.loadtxt(path, delimiter=';', skiprows=1, dtype=str, encoding='utf-8')

cases = ds[:, 7]

suc_cases = np.sum(cases == "Success")

print(suc_cases)