import numpy as np

path = "/home/tobias/Documentos/Data-Science/Data/space.csv"

ds = np.loadtxt(path, delimiter=';', skiprows=1, dtype=str, encoding='utf-8')

companies_col = ds[:,1]

companies, counts = np.unique(companies_col, return_counts=True)

for i in range(len(companies)):
    print(f"{companies[i]}: {counts[i]} missions")