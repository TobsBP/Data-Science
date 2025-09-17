import pandas as pd

df = pd.read_csv("Exercises/Pandas_03/paises.csv", delimiter=';')

def categ(deathrate):
  return 'Balanced' if deathrate < 9 else 'Urgent'

df['Humanitarian Help'] = df['Deathrate'].apply(categ)

print("Update:\n", df)