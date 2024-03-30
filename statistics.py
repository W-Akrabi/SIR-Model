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
