import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd

path_00 = "Data/airtravel.csv"
path_01 = "Data/co2_emissions.csv"

# --- DATASET 1: AIRTRAVEL ---
airtravel = pd.read_csv(path_00, delimiter=',', index_col='Date', parse_dates=True)
airtravel['Passengers'] = airtravel['Passengers'].astype(int) # Correção na atribuição

airtravel['Passengers'].plot(figsize=(8,6), title="Air Travel Passengers")

decomp_air = seasonal_decompose(airtravel['Passengers'], model='multiplicative', period=12)
decomp_air.plot()

## A) A série possui Tendência? Se sim, que tipo?
# R: Sim, possui uma Tendência Positiva e linear ao longo do tempo.

## B) A série possui Sazonalidade? Se sim, qual o período que ela acontece?
# R: Sim, possui Sazonalidade. O período é Anual, com picos claros nos meses de férias (Julho/Agosto) e baixas no início do ano.

## C) A série apresenta um Ciclo? Se sim, por qual razão?
# R: Não.

# --- DATASET 2: CO2 EMISSIONS ---
emissions = pd.read_csv(path_01, delimiter=',', index_col='Year', parse_dates=True)
emissions['CO2_Emissions'] = emissions['CO2_Emissions'].astype(float)

plt.figure()
emissions['CO2_Emissions'].plot(figsize=(8,6), title="CO2 Emissions")

decomp_co2 = seasonal_decompose(emissions['CO2_Emissions'], model='additive', period=1)
decomp_co2.plot()

## A) A série possui Tendência? Se sim, que tipo?
# R: Sim, possui uma Tendência Geral Negativa no longo prazo, indicando redução das emissões ao longo das décadas.

## B) A série possui Sazonalidade? Se sim, qual o período que ela acontece?
# R: Não. Como a frequência dos dados é Anual, não é possível observar sazonalidade.

## C) A série apresenta um Ciclo? Se sim, por qual razão?
# R: Sim. As flutuações irregulares correspondem a eventos externos globais.

plt.show()