import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = 'Classes/MatplotLib/paises.csv'

dfCountrys = pd.read_csv(path, delimiter= ';')

CountrysNoCoast = dfCountrys[dfCountrys['Coastline (coast/area ratio)'] == 0]

qtNoCoast = len(CountrysNoCoast)

qtCoast = len(dfCountrys) - qtNoCoast

plt.pie([qtNoCoast, qtCoast], labels=['Countrys no coast', 'Countrys with coast'], autopct='%1.1f%%')

plt.show()