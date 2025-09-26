import matplotlib.pyplot as plt
import pandas as pd

path = 'Exercises/MatplotLib/paises.csv'

data = pd.read_csv(path, delimiter=';', decimal=',', encoding='utf-8')

north_america = data[data['Region'] == 'NORTHERN AMERICA                   ']

countries = north_america['Country']
death_rate = north_america['Deathrate']
birth_rate = north_america['Birthrate']

plt.plot(countries, death_rate, 'o-b', label='Death Rate')
plt.plot(countries, birth_rate, 'o-r', label='Birth Rate')

plt.show()