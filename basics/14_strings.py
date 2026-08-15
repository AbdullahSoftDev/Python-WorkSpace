s = "Hello, Python!"

# Access
print(s[0])
print(s[-1])
print(s[7:13])

# Methods
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.strip())
print(s.replace("Python", "World"))
print(s.split(","))
print(",".join(["a", "b", "c"]))
print(s.startswith("Hello"))
print(s.endswith("!"))
print(s.find("Python"))
print(s.count("l"))
print(len(s))

# Formatting
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")
print("Name: {}, Age: {}".format(name, age))
print("Name: %s, Age: %d" % (name, age))