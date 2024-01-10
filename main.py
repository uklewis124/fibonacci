import math

def fib(nth):
    """Returns the nth Fibonacci number."""
    return int(((1+math.sqrt(5))**nth-(1-math.sqrt(5))**nth)/(2**nth*math.sqrt(5)))