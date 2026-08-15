import json

# Write JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding"]
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Read JSON
with open('data.json', 'r') as f:
    loaded = json.load(f)
    print(loaded)

# JSON string
json_string = json.dumps(data, indent=4)
parsed = json.loads(json_string)