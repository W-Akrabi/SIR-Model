def estimate_daily_infection_rate(data):
    """
  Estimates daily infection rate as difference between consecutive days in data.

  Args:
      data (list): List of total cases for each day.

  Returns:
      list: List of estimated daily infection rates.
  """
    if len(data) < 2:
        raise ValueError("Data requires at least two days of cases.")
    daily_rates = []
    for i in range(1, len(data)):
        daily_rates.append(data[i] - data[i - 1])
    return daily_rates


# Assuming you have historical data in a list
cases_data = [10, 25, 42, 68]

daily_infection_rates = estimate_daily_infection_rate(cases_data)
print(f"Daily Infection Rates: {daily_infection_rates}")
