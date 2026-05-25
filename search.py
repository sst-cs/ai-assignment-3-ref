import math
import random
from utils import num_conflicts, get_neighbors, random_neighbor


def hill_climbing(N, initial_state):
    """
    Steepest-Ascent Hill Climbing for N-Queens.

    Move to the neighbour with the fewest conflicts at each step.
    Stop when no neighbour strictly improves the current state.

    Args:
        N (int): Number of queens.
        initial_state (list[int]): Starting configuration.

    Returns:
        list[int]: State at the local minimum found.
    """
    # TODO: Implement Hill Climbing using get_neighbors() from utils.py
    pass


def simulated_annealing(N, initial_state, T=30.0, cooling_rate=0.995, seed=42):
    """
    Simulated Annealing for N-Queens.

    At each step pick a random neighbour. Accept it if better; otherwise
    accept with probability e^(-delta/T). Cool: T *= cooling_rate each step.
    Stop when T < 1e-3. Return the BEST state seen during the search.

    Args:
        N (int): Number of queens.
        initial_state (list[int]): Starting configuration.
        T (float): Initial temperature.
        cooling_rate (float): Multiplicative cooling factor per step.
        seed (int): Seed for a local random.Random instance.

    Returns:
        list[int]: Best state found.
    """
    # TODO: Implement Simulated Annealing using random_neighbor() from utils.py
    pass
