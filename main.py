"""main"""
import pygame
import numpy as np
import networkx as nx
import matplotlib as plt

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Animation with SIR Model")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Number of people
NUM_Persons = 50

# SIR Parameters
INFECTION_RADIUS = 20
INFECTION_PROBABILITY = 0.03
RECOVERY_TIME = 300


# Particle class
class Person:
    """
    person class that represents a person in a pandemic
    """

    def __init__(self):
        self.x = np.random.randint(0, WIDTH)
        self.y = np.random.randint(0, HEIGHT)
        self.radius = 3
        self.color = WHITE
        self.speed_x = np.random.uniform(-0.1, 0.1)
        self.speed_y = np.random.uniform(-0.1, 0.1)
        self.infected = False

    def move(self):
        """
        moves the vertex in a direction
        """
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off edges
        if self.x <= 0 or self.x >= WIDTH:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= HEIGHT:
            self.speed_y *= -1

    # Modify the draw method of the Person class to change the color of infected particles
    def draw(self):
        """
        draws the vertexes with its correspomding color in pyagame window
        """
        if self.infected:
            color = RED
        else:
            color = WHITE
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)


# Create people
people = [Person() for _ in range(NUM_Persons)]

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
        pygame.draw.line(screen, WHITE, (int(vertex1.x), int(vertex1.y)),
                         (int(vertex2.x), int(vertex2.y)))
        # Check if one is infected and the other is not, then infect based on the infection probability
        if vertex1.infected and not vertex2.infected:
            infect = np.random.rand() * 0.1
            if infect < INFECTION_PROBABILITY:
                vertex2.infected = True
        elif vertex2.infected and not vertex1.infected:
            infect = np.random.rand() * 0.1
            if infect < INFECTION_PROBABILITY:
                vertex1.infected = True


'''
def infect(threshold, p1, p2):
    """
    Infects people within a certain distance threshold with a given probability.
    :param threshold: The distance threshold for infection.
    :param p1: First particle.
    :param p2: Second particle.
    """
    distance = calculate_distance(p1, p2)
    if distance < threshold:
        if p1.color == RED:  # Check if person1 is infected
            if np.random.rand() < INFECTION_PROBABILITY:
                p2.infected = True  # Infect p2
'''

timer = pygame.time
# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move people
    for particle in people:
        particle.move()
        particle.draw()

        # Infect people
    for i, person1 in enumerate(people):
        for j, person2 in enumerate(people[i + 1:]):
            if i != j:
                draw_edge_and_infect(person1, person2, INFECTION_RADIUS)

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
