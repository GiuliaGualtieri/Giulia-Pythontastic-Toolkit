import numpy as np


def markovchain(n: int, start: int = 0):
    """
    Simulate a 1D random walk Markov chain.

    This function simulates a 1D random walk Markov chain for a given number of steps
    `n` starting from an initial position `start`. Each step is taken with equal
    probability in the positive or negative direction.

    Parameters:
        n (int): The number of steps in the Markov chain.
        start (int, optional): The initial position of the chain. Default is 0.

    Returns:
        list: A list containing the positions of the Markov chain at each step.

    Note:
        The random walk is performed with equal probability of moving in the positive
        or negative direction at each step.
    """
    x = []
    for _ in range(n):
        step = np.random.choice([-1, 1], p=[0.5, 0.5])
        start = start + step
        x.append(start)


def gamblersruinchain(start, first, last, n):
    """
    Simulate a gambler's ruin random walk.

    This function simulates a gambler's ruin random walk for a given number of steps
    `n`, starting from a specified initial position `start` and aiming to reach either
    the first or last position.

    Parameters:
        start: The initial position of the gambler.
        first: The position representing a win for the gambler.
        last: The position representing a loss for the gambler.
        n: The number of steps in the random walk.

    Returns:
        int: The final position of the gambler after the random walk.

    Note:
        The random walk is performed with equal probability of moving in the positive
        or negative direction at each step. If the gambler reaches either the first
        or last position, the walk stops.
    """
    for _ in range(n):
        if start == first or start == last:
            start = start
        else:
            step = np.random.choice([-1, 1], p=[0.5, 0.5])
            start = start + step
    return start
