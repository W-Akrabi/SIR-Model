import pandas as pd


def calculate_global_rates(csv_file):
    """Made a function to read from all the data in the file and give the global infection, mortality and recovery rate
       of all countries in dataset"""
    df = pd.read_csv(csv_file)
    global_total_cases = df['TotalCases'].sum()
    global_population = df['Population'].sum()
    global_infection_rate = global_total_cases / global_population
    global_total_deaths = df['TotalDeaths'].sum()
    global_mortality_rate = global_total_deaths / global_total_cases
    global_total_recovered = df['TotalRecovered'].sum()
    global_recovery_rate = global_total_recovered / global_total_cases

    return global_infection_rate, global_mortality_rate, global_recovery_rate


global_infect, global_mortality, global_recovery = calculate_global_rates('worldometer_data.csv')
print(global_recovery)
print(global_infect)
print(global_mortality)
# Country wise Data
df = pd.read_csv('worldometer_data.csv')
df['Infection Rate'] = df['TotalCases'] / df['Population']
df['Mortality Rate'] = df['TotalDeaths'] / df['TotalCases']
df['Recovery Rate'] = df['TotalRecovered'] / df['TotalCases']
# print(df[['Country/Region', 'Infection Rate', 'Mortality Rate', 'Recovery Rate']])
