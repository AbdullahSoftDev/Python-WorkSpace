# Basic
squares = [x**2 for x in range(10)]
print(squares)

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# Nested
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)

# Set comprehension
even_set = {x for x in range(10) if x % 2 == 0}
print(even_set)