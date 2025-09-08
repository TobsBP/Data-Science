import pandas as pd

seriesAno1 = {'Java': 16.25, 'C': 16.04, 'Python': 9.85}
seriesAno2 = {'C': 16.21, 'Python': 12.12, 'Java': 11.68}

seriesAno1 = pd.Series(seriesAno1, index=['Java', 'C', 'Python'])
seriesAno2 = pd.Series(seriesAno2, index=['Java', 'C', 'Python'])

totalAno1 = seriesAno1.sum()
totalAno2 = seriesAno2.sum()

print(f'Total from the first year: {totalAno1}')
print(f'Total from the second year: {totalAno2}')