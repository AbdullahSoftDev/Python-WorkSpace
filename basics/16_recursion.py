# Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Binary search
def binary_search(arr, target):
    if not arr:
        return -1
    mid = len(arr) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr[:mid], target)
    return binary_search(arr[mid+1:], target)