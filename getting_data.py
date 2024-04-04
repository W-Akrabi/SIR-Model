"""
Module for getting and performing calculations on data.
This module provides functions to read data from a CSV file and calculate global infection rate, mortality rate, and recovery rate
from the data. It also includes functionality to calculate infection rate, mortality rate, and recovery rate for each country
present in the dataset.

Functions:
    calculate_global_rates: Calculate global infection rate, mortality rate, and recovery rate from the provided CSV file.
"""
import pandas as pd


def calculate_global_rates(csv_file) -> tuple[float, float, float]:
    """Made a function to read from all the data in the file and give the global infection, mortality and recovery rate
       of all countries in dataset"""
    reader = pd.read_csv(csv_file)
    global_total_cases = reader['TotalCases'].sum()
    global_population = reader['Population'].sum()
    global_infection_rate = global_total_cases / global_population
    global_total_deaths = reader['TotalDeaths'].sum()
    global_mortality_rate = global_total_deaths / global_total_cases
    global_total_recovered = reader['TotalRecovered'].sum()
    global_recovery_rate = global_total_recovered / global_total_cases

    return global_infection_rate, global_mortality_rate, global_recovery_rate


global_infect, global_mortality, global_recovery = calculate_global_rates('worldometer_data.csv')
print("Global Infection Rate:", global_infect)
print("Global Recovery Rate:", global_recovery)
print("Global Mortality Rate:", global_mortality)
# Country wise Data
df = pd.read_csv('worldometer_data.csv')
df['Infection Rate'] = df['TotalCases'] / df['Population']
df['Mortality Rate'] = df['TotalDeaths'] / df['TotalCases']
df['Recovery Rate'] = df['TotalRecovered'] / df['TotalCases']
# print(df[['Country/Region', 'Infection Rate', 'Mortality Rate', 'Recovery Rate']])
# uncomment above line to get country wise stats.'''
