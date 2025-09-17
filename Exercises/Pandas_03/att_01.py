import pandas as pd

df = pd.read_csv("Exercises/Pandas_03/paises.csv", delimiter=';')

oceania = df[df['Region'].str.contains('OCEANIA                            ')]

print("Country:\n", oceania['Country'])
print("Count:", oceania['Country'].count())