import pandas as pd
import numpy as np

df = pd.DataFrame(
  index = ['A', 'B', 'C', 'D', 'E'],
  columns = ['W', 'X', 'Y', 'Z'],
  data = np.random.randint(0, 50, [5, 4])
)

print(df)

content_d = df.loc['D']

print(f'Median from line D {content_d.mean()}')

content_e = df.iloc[4]

print(f'Sum from line E {content_e.sum()}')