# Creation
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access
print(person["name"])
print(person.get("age"))
print(person.get("country", "USA"))

# Methods
person["email"] = "alice@email.com"
person.update({"phone": "123-456"})
person.pop("age")
del person["city"]
keys = person.keys()
values = person.values()
items = person.items()

# Iteration
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}