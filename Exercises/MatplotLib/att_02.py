import matplotlib.pyplot as plt
import pandas as pd

path = 'Data/space.csv'

data = pd.read_csv(path, delimiter=';')

data.columns = data.columns.str.strip()

usa_count = data[data['Location'].str.contains('USA')]['Company Name'].unique().size
china_count = data[data['Location'].str.contains('China')]['Company Name'].unique().size

labels = ['USA', 'China']
counts = [usa_count, china_count]

plt.bar(labels, counts)

plt.show()