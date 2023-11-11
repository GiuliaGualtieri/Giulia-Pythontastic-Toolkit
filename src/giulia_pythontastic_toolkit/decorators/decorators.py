"""
Decorators module.

Decorators are a powerful tool for modifying the behavior of functions in Python.
They allow you to add functionality to a function without modifying its source code.

"""

import time


# Measuring the execution time of a function using a decorator.
def measure_time(func):
    """
    Decorator to measure the execution time of a function.

    Args:
        func (function): The function to be measured.

    Returns:
        function: A wrapped function that measures and prints the execution time.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.3f} seconds")
        return result

    return wrapper


# Logging the arguments and return value of a function using a decorator.
def log_function(func):
    """
    Decorator to log the arguments and return value of a function.

    Args:
        func (function): The function to be logged.

    Returns:
        function: A wrapped function that logs function calls and their results.
    """

    def wrapper(*args, **kwargs):
        print(f"Function {func.name} called with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.name} returned {result}")
        return result

    return wrapper


# Caching the return value of a function using a decorator.
def cache_result(func):
    """
    Decorator to cache the return value of a function.

    Args:
        func (function): The function to be cached.

    Returns:
        function: A wrapped function that caches and returns results to avoid redundant computations.
    """
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Using cached result for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper
