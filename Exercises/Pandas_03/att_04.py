import pandas as pd

df = pd.read_csv("Exercises/Pandas_03/paises.csv", delimiter=';')

no_coast = df[df['Coastline (coast/area ratio)'] == 0]

no_coast[['Country']].to_csv('Exercises/Pandas_03/noCoast.csv')