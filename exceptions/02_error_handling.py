# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age too high")
    return age

# Exception chaining
try:
    validate_age(-5)
except ValueError as e:
    raise RuntimeError("Validation failed") from e

# Assertions
def process_number(num):
    assert num > 0, "Number must be positive"
    return num ** 2

# Context manager with error handling
class ManagedResource:
    def __enter__(self):
        print("Resource acquired")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released")
        if exc_type:
            print(f"Error: {exc_val}")
        return False

with ManagedResource():
    raise ValueError("Error in block")