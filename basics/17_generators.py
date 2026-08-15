# Generator function
def count_down(n):
    while n > 0:
        yield n
        n -= 1

for num in count_down(5):
    print(num)

# Generator expression
squares = (x**2 for x in range(10))
for square in squares:
    print(square)

# Infinite generator
def infinite():
    num = 0
    while True:
        yield num
        num += 1