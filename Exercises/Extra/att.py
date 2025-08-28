import numpy as np

path = "/home/tobias/Documentos/Data-Science/Exercises/Extra/paises.csv"

ds = np.loadtxt(path, delimiter=';' , skiprows=1, dtype=str, encoding='utf-8')

# print(ds[0,0:4])

regions = ds[0:,1]

unique_regions = np.unique(regions)

# print(unique_regions)

literacy = ds[0:,9]

literacy = literacy.astype(float)

media_litera = np.mean(literacy)

# print(media_litera)

norte_count = np.sum(np.char.find(ds, "NORTHERN AMERICA") != -1)

# print(norte_count)

rendas = ds[0:,9]

america_index = np.where(regions == "LATIN AMER. & CARIB    ")

rendas_america = rendas[america_index]

local = ds[0:,0]

country = local[america_index]

maior= np.argmax(rendas_america)

# print(country[maior])