import sys
import csv
import numpy as np 
import pandas as pd 
from scipy.integrate import odeint
import matplotlib.pylab as plt
import sir_base

country = sys.argv[1] #'Italy'
starting_date = sys.argv[2] #'2/18/20'

df_population_2020 = pd.read_csv('world_population_2020.csv', error_bad_lines=False, quoting=csv.QUOTE_NONE)

url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'

df_confirmed = pd.read_csv(url_confirmed, error_bad_lines=False, quoting=csv.QUOTE_NONE)
df_deaths = pd.read_csv(url_deaths, error_bad_lines=False, quoting=csv.QUOTE_NONE)
df_recovered = pd.read_csv(url_recovered, error_bad_lines=False, quoting=csv.QUOTE_NONE)

# model

N = int(df_population_2020[df_population_2020['name']== country]['pop2020'] * 1000)
I = df_confirmed[df_confirmed['Country/Region'] == country][starting_date]
R = df_deaths[df_deaths['Country/Region'] == country][starting_date] + df_recovered[df_recovered['Country/Region'] == country][starting_date]
S = N - I - R 
sir0 = (S, I[I.index[0]], R[R.index[0]])

t = np.linspace(0, 100) # time points - 1 per day
sir = sir_base.model(sir_base.diff, sir0, t)

# plotting

plt.plot(t, sir[:, 0], label='S(t)', color='green')
plt.plot(t, sir[:, 1], label='I(t)', color='red')
plt.plot(t, sir[:, 2], label='R(t)', color='blue')

plt.title('{}'.format(country))
plt.xlabel('#days from {}'.format(starting_date))
plt.ylabel('N')
plt.legend()

# use scientific notation
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.show()