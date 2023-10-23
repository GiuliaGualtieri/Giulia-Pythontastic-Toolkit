"""
Decorators module.

Decorators are a powerful tool for modifying the behavior of functions in Python.
They allow you to add functionality to a function without modifying its source code.

"""

import time

# Measuring the execution time of a function using a decorator.
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.3f} seconds")
        return result
    return wrapper


# Logging the arguments and return value of a function using a decorator.
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.name} called with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.name} returned {result}")
        return result
    return wrapper


# Caching the return value of a function using a decorator.
def cache_result(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Using cached result for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper