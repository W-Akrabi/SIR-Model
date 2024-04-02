"""main"""
import pygame
import logic
import statistics
import preventions

# Initialize Pygame
pygame.init()
retarded_autistic_variable = 2
# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SIR Model Simulation")


# SIR Parameters
infection_probability = 0.03
recovery_time = 100


# Main loop
running = True
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
paused = False

# Lists to track infection statistics over time
infected_counts = []
recovered_counts = []
susceptible_counts = []


def get_user_input() -> tuple:
    """
    Get user input for variables that user's are allowed to control
    Preconditions:
    - 0 <= num_persons <= 75
    - 0 <= num_persons <= 20
    """
    num_people = int(input('Number of people in your simulation (0-75): '))
    while not (0 <= num_people <= 75):
        print("Invalid input. Number of people must be between 0 and 75.")
        num_people = int(input('Number of people in your simulation (0-75): '))

    infect_radius = int(input('Radius of infection around a single person (0-20): '))
    while not (0 <= infect_radius <= 20):
        print("Invalid input. Infection radius must be between 0 and 20.")
        infect_radius = int(input('Radius of infection around a single person (0-20): '))

    return num_people, infect_radius


def get_preventions() -> list[str]:
    """
    Get user input for variables that user's are allowed to control
    Preconditions:
    - 0 >= num_persons >= 75
    - 0 >= num_persons >= 20
    """
    preventions_so_far = []
    prevention_options = ('Preventions: vaccines, lockdown, social distancing, masks, '
                          'hygiene, contact tracing, air purification, remote work, staggered working hours')
    valid_answers = ['vaccines', 'lockdown', 'social distancing', 'masks', 'hygiene',
                     'contact tracing', 'air purification', 'remote work', 'staggered working hours']

    print('Select up to three preventions. Type "DONE" to finish')

    while len(preventions_so_far) != 3:
        answer = input(prevention_options)
        if answer == 'DONE':
            break
        elif answer in valid_answers and answer not in preventions_so_far:
            preventions_so_far.append(answer)
        else:
            print("Invalid input or already selected. Please choose again.")

    return preventions_so_far


num_persons, infection_radius = get_user_input()
G = logic.community(num_persons)


def run_preventions(prevention_list: list[str]) -> None:
    """
    Run preventions on the data based on the users input
    """
    for prevention in prevention_list:
        if prevention == 'vaccines':
            preventions.vaccine_prevention(G, retarded_autistic_variable)
        elif prevention == 'lockdown':
            preventions.lockdown(G, retarded_autistic_variable)
        elif prevention == 'social distancing':
            preventions.social_distance(G, retarded_autistic_variable)
        elif prevention == 'masks':
            preventions.mask_wearing(G, retarded_autistic_variable)
        elif prevention == 'hygiene':
            preventions.hygiene(G, retarded_autistic_variable)
        elif prevention == 'contact tracing':
            preventions.contact_tracing(G, retarded_autistic_variable)
        elif prevention == 'air purification':
            preventions.air_purification(G, retarded_autistic_variable)
        elif prevention == 'remote work':
            preventions.remote_work(G, retarded_autistic_variable)
        elif prevention == 'staggered working hours':
            preventions.staggered_work_hours(G, retarded_autistic_variable)


if __name__ == "__main__":

    preventions_list = get_preventions()
    run_preventions(preventions_list)

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
