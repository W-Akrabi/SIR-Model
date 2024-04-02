"""main"""
import pygame
import logic
import statistics
import plotly.graph_objects as go

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SIR Model Simulation")


# Number of people
num_persons = 50

# SIR Parameters
infection_radius = 20
infection_probability = 0.03
recovery_time = 100

# Create people
G = logic.community(num_persons)

# Main loop
running = True
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
paused = False

# Lists to track infection statistics over time
infected_counts = []
recovered_counts = []
susceptible_counts = []

while running:
    screen.fill(logic.black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Example: Use space bar to toggle pause
                paused = not paused

    if not paused:
        # Move people
        for person in G:
            person.move()
            person.draw(screen)

        # Infect people
        logic.simulate_one_time_step(G, infection_radius, infection_probability, recovery_time, screen)

        # Track infection statistics
        num_infected = sum(1 for person in G if person.infected)
        num_recovered = sum(1 for person in G if person.recovered)
        num_susceptible = num_persons - num_infected - num_recovered

        infected_counts.append(num_infected)
        recovered_counts.append(num_recovered)
        susceptible_counts.append(num_susceptible)

        # Check if time limit exceeded
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 10000:
            running = False

        clock.tick(300)
        pygame.display.flip()  # Optional delay for smoother animation

pygame.quit()

# Plot the infection statistics over time using Plotly
statistics.plot_sir_curve(infected_counts, recovered_counts, susceptible_counts)
