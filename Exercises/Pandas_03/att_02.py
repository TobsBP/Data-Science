import pandas as pd

df = pd.read_csv("Exercises/Pandas_03/paises.csv", delimiter=';')

max_pop = df.loc[df['Population'].idxmax(), ['Country', 'Region']]

print("Max:\n", max_pop)