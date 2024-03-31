import numpy as np
import matplotlib.pyplot as plt


def plot_infection_curve(infected_counts):
    """
    Plot the infection curve showing the number of infected individuals over time.
    Args:
    - infected_counts: List of integers representing the number of infected individuals at each iteration.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(infected_counts, color='red', linestyle='-', marker='o', markersize=4)
    plt.title('Infection Curve Over Time')
    plt.xlabel('Time Steps')
    plt.ylabel('Number of Infected Individuals')
    plt.grid(True)
    plt.show()


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
    plt.figure(figsize=(10, 6))
    plt.plot(infected_counts, label='Infected', color='red')
    if recovered_counts:
        plt.plot(recovered_counts, label='Recovered', color='green')
    if susceptible_counts:
        plt.plot(susceptible_counts, label='Susceptible', color='blue')
    plt.title('SIR Curve Over Time')
    plt.xlabel('Time Steps')
    plt.ylabel('Number of Individuals')
    plt.grid(True)
    plt.legend()
    plt.show()
