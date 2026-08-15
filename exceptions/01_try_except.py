# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    num = int("abc")
except (ValueError, TypeError):
    print("Invalid conversion")

# Specific exceptions
try:
    file = open('nonexistent.txt')
except FileNotFoundError as e:
    print(f"Error: {e}")

# Else clause
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Success: {result}")

# Finally
try:
    file = open('data.txt')
finally:
    file.close()

# Custom exception
class CustomError(Exception):
    pass

try:
    raise CustomError("Custom error occurred")
except CustomError as e:
    print(e)