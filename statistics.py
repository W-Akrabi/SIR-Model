import numpy as np
import plotly.graph_objects as go


def plot_infection_curve(infected_counts):
    """
    Plot the infection curve showing the number of infected individuals over time.
    Args:
    - infected_counts: List of integers representing the number of infected individuals at each iteration.
    """
    # Calculate decimal days passed
    days_passed = [i / 300 for i in range(len(infected_counts))]  # Assuming 300 iterations per day

    # Create Plotly figure
    fig = go.Figure()

    # Add infected curve
    fig.add_trace(go.Scatter(x=days_passed, y=infected_counts, mode='lines', name='Infected', line=dict(color='red')))

    # Update layout
    fig.update_layout(title='Infection Curve',
                      xaxis_title='Time (Days)',
                      yaxis_title='Number of Infected Individuals')

    # Show plot
    fig.show()


def calculate_infection_rate(infected_counts):
    """
    Calculate the average infection rate over the simulation.
    Args:
    - infected_counts: List of integers representing the number of infected individuals at each iteration.
    Returns:
    - Float: Average infection rate per iteration.
    """
    infection_rate = np.mean(np.diff(infected_counts))
    return infection_rate


def analyze_sir_simulation(infected_counts, recovered_counts, population):
    """
    Analyze various statistics from a SIR model simulation
    Args:
      infected_counts: List of integers representing number of infected individuals at each iteration
      recovered_counts: List of integers representing number of recovered individuals at each iteration (optional)
      population: Total population size
    """
    # Final Statistics
    peak_infected = max(infected_counts)
    total_recovered = sum(recovered_counts) if recovered_counts else 0
    percent_recovered = (total_recovered / population) * 100
    time_to_peak = infected_counts.index(peak_infected)

    # Rate Statistics
    max_infection_rate = np.max(np.diff(infected_counts))
    recovery_rate = np.mean(np.diff(recovered_counts)) if recovered_counts else 0

    # Print results
    print("Final Statistics:")
    print(f"Peak Number of Infected: {peak_infected}")
    print(f"Total Number Recovered: {total_recovered}")
    print(f"Percentage Recovered: {percent_recovered:.2f}%")
    print(f"Time to Peak Infection: {time_to_peak} iterations")

    print("\nRate Statistics:")
    print(f"Maximum Infection Rate: {max_infection_rate}")
    print(f"Recovery Rate: {recovery_rate}")


def plot_sir_curve(infected_counts, recovered_counts, susceptible_counts=None):
    """
    Plot the SIR curve showing susceptible, infected, and recovered individuals over time.
    Args:
      infected_counts: List of integers representing number of infected individuals at each iteration
      recovered_counts: List of integers representing number of recovered individuals at each iteration
      susceptible_counts: List of integers representing number of susceptible individuals at each iteration (optional)
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(len(infected_counts))),
                             y=infected_counts,
                             mode='lines',
                             name='Infected',
                             line=dict(color='red')))
    fig.add_trace(go.Scatter(x=list(range(len(recovered_counts))),
                             y=recovered_counts,
                             mode='lines',
                             name='Recovered',
                             line=dict(color='green')))
    fig.add_trace(go.Scatter(x=list(range(len(susceptible_counts))),
                             y=susceptible_counts,
                             mode='lines',
                             name='Susceptible',
                             line=dict(color='blue')))
    fig.update_layout(title='SIR Model Simulation',
                      xaxis_title='Time',
                      yaxis_title='Number of Individuals')
    fig.show()
