import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = 'Classes/MatplotLib/paises.csv'

dfCountrys = pd.read_csv(path, delimiter= ';')

BiggestCountrys = dfCountrys.nlargest(6, 'Area (sq. mi.)')

BiggestCountrys['Country']

#Scatter plot

plt.scatter(BiggestCountrys['Country'], BiggestCountrys['GDP ($ per capita)'], s=10000000)

plt.show()