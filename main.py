"""main"""
import pygame
import numpy as np
import networkx as nx
import itertools
import statistics

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particle Animation with SIR Model")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Number of people
num_persons = 50

# SIR Parameters
infection_radius = 20
infection_probability = 0.03
recovery_time = 100


# Particle class
class Person:
    """
    person class that represents a person in a pandemic
    """

    def __init__(self):
        self.x = np.random.randint(0, width)
        self.y = np.random.randint(0, height)
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
        if self.x <= 0 or self.x >= width:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= height:
            self.speed_y *= -1

    # Modify the draw method of the Person class to change the color of infected particles
    def draw(self):
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
people = [Person() for _ in range(num_persons)]

infected_particle = people[np.random.choice(len(people))]
infected_particle.infected = True

# Create graph to represent connections between people
G = nx.Graph()

# Add people as nodes to the graph
for particle in people:
    G.add_node(particle)

# Add edges between people based on distance
for i, person1 in enumerate(people):
    for person2 in people[i + 1:]:  # Only iterate over people that come after person1
        G.add_edge(person1, person2)


def calculate_distance(p1, p2):
    """
    calculates the distance between two vertexes
    :param p1:
    :param p2:
    :return:
    """
    return np.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def draw_edge_and_infect(vertex1, vertex2, threshold: int):
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


def simulate_one_time_step(G):
    """
    Simulates one time step of epidemic spread.
    :param G: List of Person objects representing individuals in the simulation.
    """
    for person1, person2 in G.edges():
        draw_edge_and_infect(person1, person2, infection_radius)


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


# Main loop
running = True
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
current_time = pygame.time.get_ticks()
paused = False
while running and current_time - start_time < 10000:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Example: Use space bar to toggle pause
                paused = not paused

    if not paused:
        # Move people
        for particle in people:
            particle.move()
            particle.draw()

        # Infect people
        simulate_one_time_step(G)

        current_time = pygame.time.get_ticks()
        clock.tick(280)
        pygame.display.flip()  # Optional delay for smoother animation

pygame.quit()

if __name__ == '__main__':
    # You can uncomment the following lines for code checking/debugging purposes.
    # However, we recommend commenting out these lines when working with the large
    # datasets, as checking representation invariants and preconditions greatly
    # increases the running time of the functions/methods.
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()

    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['E1136', 'W0221'],
        'extra-imports': ['csv', 'networkx'],
        'max-nested-blocks': 4
    })
