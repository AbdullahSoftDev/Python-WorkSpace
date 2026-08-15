# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default parameters
def greet_default(name="World"):
    return f"Hello, {name}!"

# Multiple parameters
def add(a, b):
    return a + b

# Variable arguments
def sum_all(*args):
    return sum(args)

# Keyword arguments
def person_info(**kwargs):
    return kwargs

# Lambda function
square = lambda x: x**2

# Function as argument
def apply(func, value):
    return func(value)

# Closure
def outer(x):
    def inner(y):
        return x + y
    return inner

# Decorator
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end - start}s")
        return result
    return wrapper