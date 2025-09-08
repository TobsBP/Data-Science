import pandas as pd
import numpy as np

df = pd.DataFrame(
  index = ['A', 'B', 'C', 'D', 'E'],
  columns = ['W', 'X', 'Y', 'Z'],
  data = np.random.randint(0, 50, [5, 4])
)

print(df)

content = df.loc[['A', 'C', 'E'],['X', 'Y']]

print()

print(content)

columms = content.sum(axis=0)
lines = content.sum(axis=1)

print(f'Columms X and Y: \n{columms}')
print(f'Lines A, C and E: \n{lines}')