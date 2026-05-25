import random

def num_conflicts(state):
    """Return the number of attacking queen pairs in the given state."""
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:                   # same row
                conflicts += 1
            if abs(state[i] - state[j]) == abs(i - j): # same diagonal
                conflicts += 1
    return conflicts


def get_neighbors(state):
    """
    Generate all single-move neighbours of the current state.
    A neighbour changes the row of exactly one queen.

    Returns a list of (conflicts, neighbour_state) sorted by
    (conflicts, neighbour_state) for deterministic tie-breaking.
    """
    n = len(state)
    neighbors = []
    for col in range(n):
        for row in range(n):
            if row != state[col]:
                neighbor = list(state)
                neighbor[col] = row
                c = num_conflicts(neighbor)
                neighbors.append((c, neighbor))
    neighbors.sort(key=lambda x: (x[0], x[1]))
    return neighbors


def random_state(N, rng):
    """
    Generate a completely random starting state for N-Queens.

    Args:
        N (int): Board size.
        rng:     a random.Random instance (for reproducibility).

    Returns:
        list[int]: A list of N integers each in [0, N-1].
    """
    return [rng.randint(0, N - 1) for _ in range(N)]


def random_neighbor(state, rng):
    """
    Pick a random single-move neighbour using the supplied RNG.

    Args:
        state: current state (list of ints)
        rng:   a random.Random instance (for reproducibility)

    Returns a new state list.
    """
    n = len(state)
    col = rng.randint(0, n - 1)
    row = rng.randint(0, n - 1)
    while row == state[col]:
        row = rng.randint(0, n - 1)
    neighbor = list(state)
    neighbor[col] = row
    return neighbor
