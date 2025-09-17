import pandas as pd

df = pd.read_csv("Exercises/Pandas_03/paises.csv", delimiter=';')

avg_literacy = df.groupby('Region')['Literacy (%)'].mean()

print("Mean:\n", avg_literacy)