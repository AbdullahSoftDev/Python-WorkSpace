from functools import reduce

# Map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Filter
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# Reduce
sum_all = reduce(lambda a, b: a + b, numbers)
print(sum_all)

# Combine
result = reduce(lambda a, b: a * b, filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))
print(result)