import pickle

# Pickle object
data = {
    "name": "Alice",
    "age": 25,
    "scores": [85, 90, 88]
}

with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Unpickle
with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)
    print(loaded)