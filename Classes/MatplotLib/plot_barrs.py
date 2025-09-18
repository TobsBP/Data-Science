import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = 'Classes/MatplotLib/paises.csv'

dfCountrys = pd.read_csv(path, delimiter= ';')

BiggestCountrys = dfCountrys.nlargest(5, 'GDP ($ per capita)')

BiggestCountrys['Country']

#Barrs plot

plt.bar(BiggestCountrys['Country'], BiggestCountrys['GDP ($ per capita)'])

plt.show()