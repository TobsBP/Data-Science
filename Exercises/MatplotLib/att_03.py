import matplotlib.pyplot as plt
import pandas as pd

path = 'Data/space.csv'

data = pd.read_csv(path, delimiter=';')

missions = data[data['Company Name'] == 'Roscosmos']

success_cases = missions[missions['Status Mission'] == 'Success']

failure_cases = missions[missions['Status Mission'] == 'Failure']

plt.pie([len(success_cases), len(failure_cases)], labels=['Success', 'Failure'], autopct='%1.1f%%')

plt.show()