"""
This file contains classes and functions for simulating a pandemic using Pygame.

Classes:
- Person: Represents an individual in the simulation.

Functions:
- community(num_persons): Creates a community of people based on a graph.
- calculate_distance(p1, p2): Calculates the Euclidean distance between two points.
- draw_edge_and_infect(vertex1, vertex2, threshold, infection_probability, recovery_time, screen):
    Draws an edge between two people and infects them based on proximity and infection probability.
- simulate_one_time_step(G, infection_radius, infection_probability, recovery_time, screen):
    Simulates one time step of epidemic spread.
- track_infections_over_time(people, num_iterations, infection_radius, infection_probability, recovery_time, screen):
    Tracks the number of infected individuals over the course of the simulation.

Constants:
- white: RGB color value for white.
- black: RGB color value for black.
- red: RGB color value for red.
- green: RGB color value for green.

Dependencies:
- pygame: Library for creating video games and multimedia applications.
- numpy: Library for numerical computations.

Note: This file relies on the 'graph_model' module for graph-related functionality.
"""
import pygame
import numpy as np
import graph_model

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)


class Person:
    """
    person class that represents a person in a pandemic
    """

    def __init__(self):
        self.x = np.random.randint(0, 800)
        self.y = np.random.randint(0, 600)
        self.radius = 3
        self.color = white
        self.speed_x = np.random.uniform(-1, 1)
        self.speed_y = np.random.uniform(-1, 1)
        self.infected = False
        self.recovered = False
        self.infection_timer = 0

    def move(self):
        """
        moves the vertex in a direction
        """
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off edges
        if self.x <= 0 or self.x >= 800:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= 600:
            self.speed_y *= -1

    # Modify the draw method of the Person class to change the color of infected particles
    def draw(self, red, green, white, screen):
        """
        draws the vertexes with its correspomding color in pyagame window
        """
        if self.infected:
            color = red
        elif self.recovered:
            color = green
        else:
            color = white
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)


# Create people
def community(num_persons) -> graph_model.Graph():
    """
    creates a community of people based on a graph
    :param num_persons:
    :return:
    """
    people = [Person() for _ in range(num_persons)]

    infected_particle = people[np.random.choice(len(people))]
    infected_particle.infected = True

    # Create graph to represent connections between people
    G = graph_model.Graph()

    # Add people as nodes to the graph
    for particle in people:
        G.add_node(particle)

    # Add edges between people based on distance
    for i, person1 in enumerate(people):
        for person2 in people[i + 1:]:  # Only iterate over people that come after person1
            G.add_edge(person1, person2)

    return G


def calculate_distance(p1, p2):
    """
    calculates the distance between two vertexes
    :param p1:
    :param p2:
    :return:
    """
    return np.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def draw_edge_and_infect(vertex1, vertex2, threshold: int, infection_probability, recovery_time, screen):
    """
    draws the edge between two people under a certain distance
    :param vertex1:
    :param vertex2:
    """
    distance = calculate_distance(vertex1, vertex2)
    if distance < threshold:  # Adjust the threshold distance as needed
        pygame.draw.line(screen, white, (int(vertex1.x), int(vertex1.y)),
                         (int(vertex2.x), int(vertex2.y)))
        # Check if one is infected and the other is not, then infect based on the infection probability
        infect = np.random.rand()
        if vertex1.infected and not vertex2.infected:
            if infect < infection_probability:
                vertex2.infected = True
        elif vertex2.infected and not vertex1.infected:
            if infect < infection_probability:
                vertex1.infected = True

        if vertex1.infected:
            vertex1.infection_timer += 1
            if vertex1.infection_timer >= recovery_time:
                vertex1.infected = False
                vertex1.recovered = True
                vertex1.infection_timer = 0

        if vertex2.infected:
            vertex2.infection_timer += 1
            if vertex2.infection_timer >= recovery_time:
                vertex2.infected = False
                vertex2.recovered = True
                vertex2.infection_timer = 0


def simulate_one_time_step(G, infection_radius, infection_probability, recovery_time, screen):
    """
    Simulates one time step of epidemic spread.
    :param G: List of Person objects representing individuals in the simulation.
    """
    for person1, person2 in G.edges:
        draw_edge_and_infect(person1, person2, infection_radius, infection_probability, recovery_time, screen)


def track_infections_over_time(people, num_iterations, infection_radius, infection_probability, recovery_time, screen):
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
        # Simulate one time step of the epidemic
        simulate_one_time_step(people, infection_radius, infection_probability, recovery_time, screen)
    return infected_counts