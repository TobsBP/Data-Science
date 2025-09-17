import pandas as pd
import numpy as np

df = pd.DataFrame(
  index = ['A', 'B', 'C', 'D', 'E'],
  columns = ['W', 'X', 'Y', 'Z'],
  data = np.random.randint(0, 50, [5, 4])
)

content = df['X']

content = content[content < 30] 

print(content.mean())