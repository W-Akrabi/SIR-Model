"""main"""
import pygame
import logic

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particle Animation with SIR Model")


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
current_time = pygame.time.get_ticks()
paused = False
while running and current_time - start_time < 20000:
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

        current_time = pygame.time.get_ticks()
        clock.tick(300)
        pygame.display.flip()  # Optional delay for smoother animation

pygame.quit()
