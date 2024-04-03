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

Dependencies:
- pygame: Library for creating video games and multimedia applications.
- numpy: Library for numerical computations.

Note: This file relies on the 'graph_model' module for graph-related functionality.
"""
import pygame
import numpy as np
import python_ta
import graph_model


class Person:
    """
    person class that represents a person in a pandemic

    Instance attributes:

    Representation Invarients:
    """
    x: int
    y: int
    radius: int
    speed_x: float
    speed_y: float
    infected: bool
    recovered: bool
    infected_timer = int

    def __init__(self) -> None:
        self.x = np.random.randint(0, 800)
        self.y = np.random.randint(0, 600)
        self.radius = 3
        self.color = (255, 255, 255)  # white
        self.speed_x = np.random.uniform(-2, 2)
        self.speed_y = np.random.uniform(-2, 2)
        self.infected = False
        self.recovered = False
        self.infection_timer = 0

    def move(self) -> None:
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
    def draw(self, screen) -> None:
        """
        draws the vertexes with its correspomding color in pyagame window
        """
        if self.infected:
            color = (255, 0, 0)  # red
        elif self.recovered:
            color = (0, 255, 0)  # Green
        else:
            color = (255, 0, 0)  # white
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)


# Create people
def community(num_persons: int) -> graph_model.Graph():
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


def calculate_distance(p1: Person, p2: Person) -> float:
    """
    calculates the distance between two vertexes
    :param p1:
    :param p2:
    :return:
    """
    return np.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def draw_edge_and_infect(vertex1: Person, vertex2: Person, model_params: tuple[int, float, int], screen) -> None:
    """
    draws the edge between two people under a certain distance
    :param vertex1:
    :param vertex2:
    """
    threshold, infection_probability, recovery_time = model_params
    distance = calculate_distance(vertex1, vertex2)
    if distance < threshold:  # Adjust the threshold distance as needed
        pygame.draw.line(screen, (255, 0, 0), (int(vertex1.x), int(vertex1.y)),
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


def simulate_one_time_step(people: graph_model.Graph(), infection_radius: int, infection_probability: float,
                           recovery_time: int, screen) -> None:
    """
    Simulates one time step of epidemic spread.
    :param people: List of Person objects representing individuals in the simulation.
    """
    for person1, person2 in people.edges:
        draw_edge_and_infect(person1, person2, infection_radius, infection_probability, recovery_time, screen)


if __name__ == "__main__":
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
