# Create module my_math.py
# In my_math.py:
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else None

# Import module
import my_math
print(my_math.add(5, 3))

from my_math import multiply, divide
print(multiply(4, 5))

# Import with alias
import my_math as mm
print(mm.subtract(10, 3))

# Import all
from my_math import *
print(add(2, 3))

# Reload module
import importlib
importlib.reload(my_math)