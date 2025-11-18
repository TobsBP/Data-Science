import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd

path = "Data/retail_index_br.csv"

dataset = pd.read_csv(path, delimiter=';', index_col='date', parse_dates=True)

dataset['retail_index'].astype(float)

dataset['retail_index'].plot(figsize=(8,6), title='Índice de volume de vendas no setor varejista brasileiro', xlabel='Data', ylabel='Índice', x_compat=True)

## The hight places are the "Sazionalidade"
## plt.show()

## Decomposing adition
decomposition = seasonal_decompose(dataset['retail_index'], model='additive')

decomposition.plot()
plt.tight_layout()
plt.show()