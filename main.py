"""main"""
import statistics
import python_ta
import pygame
import graph_model
import logic
import preventions
import getting_data


def get_user_input() -> tuple:
    """
    Get user input for variables that user's are allowed to control
    Preconditions:
    - 0 <= num_persons <= 75
    - 0 <= num_persons <= 20
    """
    num_people = int(input('Number of people in your simulation (0-75): '))
    while not 0 <= num_people <= 75:
        print("Invalid input. Number of people must be between 0 and 75.")
        num_people = int(input('Number of people in your simulation (0-75): '))

    infect_radius = int(input('Radius of infection around a single person (0-20): '))
    while not 0 <= infect_radius <= 20:
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
    prevention_options = ('Preventions: \n-vaccines \n-lockdown \n-social distancing \n-masks '
                          '\n-infection tracing \n-remote work \n-staggered working hours')
    valid_answers = ['vaccines', 'lockdown', 'social distancing', 'masks',
                     'infection tracing', 'remote work', 'staggered working hours']

    print('\nSelect up to three preventions. Type "Done" to finish\n')

    while len(preventions_so_far) != 3:
        answer = input(prevention_options).lower().strip()
        if answer == 'done':
            break
        elif answer in valid_answers and answer not in preventions_so_far:
            preventions_so_far.append(answer)
        elif answer not in valid_answers:
            print("Invalid input. Please choose again. Type 'Done' to finish")
        else:
            print("Already Chosen. Please choose a different prevention. Type 'Done' to finish")

    return preventions_so_far


def run_preventions(prevention_list: list[str], p: graph_model.Graph(), dumb_variable: float, num_person: int) -> None:
    """
    Run preventions on the data based on the users input
    """
    for prevention in prevention_list:
        if prevention == 'vaccines':
            preventions.vaccine_prevention(p, dumb_variable)
        elif prevention == 'lockdown':
            preventions.lockdown(p, dumb_variable)
        elif prevention == 'masks':
            preventions.mask_wearing(p, dumb_variable)
        elif prevention == 'remote work':
            preventions.remote_work(p, dumb_variable, num_person)
        elif prevention == 'staggered working hours':
            preventions.staggered_work_hours(p, dumb_variable)


if __name__ == "__main__":
    retarded_autistic_variable = 0.5
    recovery_time = 100

    num_persons, infection_radius = get_user_input()
    G = logic.community(num_persons)

    # Lists to track infection statistics over time
    infected_counts = []
    recovered_counts = []
    susceptible_counts = []

    preventions_list = get_preventions()
    run_preventions(preventions_list, G, retarded_autistic_variable, num_persons)

    # Now that user input is gathered and preventions are applied, initialize Pygame
    pygame.init()
    # Screen dimensions
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("SIR Model Simulation")

    # Main loop
    running = True
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    paused = False

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Example: Use space bar to toggle pause
                    paused = not paused

        if not paused:
            if 'social distancing' in preventions_list:
                preventions.social_distance(G, 20, width, height)
            elif 'infection tracing' in preventions_list:
                preventions.infection_tracing(G, 0.5)
            # Move people
            for person in G:
                person.move(width, height)
                person.draw(screen)

            # Infect people
            for person1, person2 in G.edges:
                logic.draw_edge_and_infect(person1, person2, (infection_radius, recovery_time), screen)

            # Track infection statistics
            num_infected = sum(1 for p in G if p.infected)
            num_recovered = sum(1 for p in G if p.recovered)
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

    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 124
    })
