import numpy as np
import matplotlib.pyplot as plt
from main import simulate_one_time_step


def track_infections_over_time(people, num_iterations):
    """
    Track the number of infected individuals over the course of the simulation.
    Args:
    - people: List of Person objects representing individuals in the simulation.
    - num_iterations: Number of iterations (time steps) to run the simulation.
    Returns:
    - List of integers representing the number of infected individuals at each iteration.
    """
    infected_counts = []
    for _ in range(num_iterations):
        num_infected = sum(person.infected for person in people)
        infected_counts.append(num_infected)
        simulate_one_time_step(people)  # Simulate one time step of the epidemic
    return infected_counts


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
