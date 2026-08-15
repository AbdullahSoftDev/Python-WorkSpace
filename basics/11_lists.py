# Creation
fruits = ["apple", "banana", "cherry"]
numbers = list(range(5))
mixed = [1, "hello", 3.14, True]

# Access
print(fruits[0])        # First
print(fruits[-1])       # Last
print(fruits[1:3])      # Slice

# Methods
fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("banana")
fruits.pop()
print(fruits.index("apple"))
print(fruits.count("apple"))
fruits.sort()
fruits.reverse()
fruits.clear()

# List operations
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
repeated = list1 * 3