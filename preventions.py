import numpy as np


def vaccine_prevention(people, vaccine_effectiveness):
    """
    Apply vaccine prevention by reducing the infection probability for vaccinated individuals.
    :param people: List of Person objects.
    :param vaccine_effectiveness: Effectiveness of the vaccine (0 to 1).
    """
    for person in people:
        if person.infected and np.random.rand() > vaccine_effectiveness:
            person.infected = False  # Reduce infection probability based on vaccine effectiveness


def lockdown(people, lockdown_factor):
    """
    Apply lockdown by reducing the movement speed of individuals.
    :param people: List of Person objects.
    :param lockdown_factor: Factor to reduce movement speed (0 to 1).
    """
    for person in people:
        person.speed_x *= lockdown_factor  # Reduce movement speed
        person.speed_y *= lockdown_factor


def social_distance(people, distance_threshold):
    """
    Implement social distancing by increasing the distance between individuals.
    :param people: List of Person objects.
    :param distance_threshold: Minimum distance to maintain between individuals.
    """
    for i, person1 in enumerate(people):
        for person2 in people[i + 1:]:
            distance = np.sqrt((person2.x - person1.x) ** 2 + (person2.y - person1.y) ** 2)
            if distance < distance_threshold:
                # Adjust positions to increase distance
                angle = np.arctan2(person2.y - person1.y, person2.x - person1.x)
                move_x = (distance_threshold - distance) * np.cos(angle) / 2
                move_y = (distance_threshold - distance) * np.sin(angle) / 2
                person1.x -= move_x
                person1.y -= move_y
                person2.x += move_x
                person2.y += move_y


def hygiene(people, hygiene_effectiveness):
    """
    Apply hygiene practices by reducing the infection probability for individuals with good hygiene.
    :param people: List of Person objects.
    :param hygiene_effectiveness: Effectiveness of hygiene practices (0 to 1).
    """
    for person in people:
        if person.infected and np.random.rand() > hygiene_effectiveness:
            person.infected = False  # Reduce infection probability based on hygiene effectiveness


def mask_wearing(people, mask_effectiveness):
    """
    Implement mask wearing by reducing the infection probability for individuals wearing masks.
    :param people: List of Person objects.
    :param mask_effectiveness: Effectiveness of masks (0 to 1).
    """
    for person in people:
        if person.infected and np.random.rand() > mask_effectiveness:
            person.infected = False  # Reduce infection probability based on mask effectiveness


def contact_tracing(people, infected_threshold):
    """
    Implement contact tracing to identify and isolate individuals who have been in contact with infected individuals.
    :param people: List of Person objects.
    :param infected_threshold: Threshold for identifying infected individuals (0 to 1).
    """
    for person in people:
        if person.infected:
            for contact in person.contacts:
                if not contact.infected and np.random.rand() < infected_threshold:
                    contact.infected = True  # Infect contact based on threshold
                    # Implement further actions such as isolation or testing


def ventilation(people, ventilation_effectiveness):
    """
    Improve ventilation to reduce the concentration of infectious aerosols in indoor environments.
    :param people: List of Person objects.
    :param ventilation_effectiveness: Effectiveness of ventilation (0 to 1).
    """
    # Implement ventilation measures such as increasing airflow or using air purifiers
    pass


def staggered_work_hours(people, staggered_factor):
    """
    Implement staggered work hours to reduce the number of people present in a shared space at any given time.
    :param people: List of Person objects.
    :param staggered_factor: Factor to adjust work hours (0 to 1).
    """
    # Adjust work hours for individuals to stagger their arrival and departure times
    pass


def remote_work(people, remote_work_factor):
    """
    Encourage remote work to minimize physical interactions in workplaces.
    :param people: List of Person objects.
    :param remote_work_factor: Factor to increase remote work (0 to 1).
    """
    # Transition individuals to remote work where feasible
    pass
