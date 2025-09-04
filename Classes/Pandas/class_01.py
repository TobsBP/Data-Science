import pandas as pd
import numpy as np

def divisor():
  return print("-"*17)

np.random.seed(10)

arr = {'a': 1, 'b': 2, 'c': 3}

ser = pd.Series(data=arr, index=['a','b','c'])

# print(ser)

cities = ['Ouro Fino', 'São Paulo', 'Borda da Mata']
population = [14.6, 65.6, 4]

city_series = pd.Series(population, index=cities)

# print(city_series.index) Return de name of the cities

arr_pd = pd.Series([1,2,3]).array

# print(pd.Series(arr_pd).values) Return the values only

odd_nums = {'a': 1, 'b': 3, 'c': 5}
pair_nums = {'a': 2, 'b': 4, 'c': 6}

ser_odd = pd.Series(odd_nums, index=['a','b','c'])
ser_pair = pd.Series(pair_nums, index=['a','b','c'])

df = pd.DataFrame(
  index = ['A', 'B', 'C', 'D', 'E'],
  columns = ['W', 'X', 'Y', 'Z'],
  data = np.random.randint(0, 50, [5, 4])
)

print(df)

divisor()

print(f'df[X][C]: {df['X']['C']}')

divisor()

print(df.iloc[0:2, :]) # 2 collumns and all the line

divisor()

print(df.loc[['A', 'B'], ['W', 'X', 'Y', 'Z']]) # Using loc, more easy

divisor()

print(df.loc[['A', 'B'], ['W', 'Z']]) # Using loc, more easy

divisor()