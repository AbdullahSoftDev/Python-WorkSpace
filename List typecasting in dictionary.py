std = {
    "Name": "Abdullah", 
    "Age": 25,
    "subjects": {
        "Math": 90,
        "Science": 85,
        "English": 88
        },
    "address":(11,22,33,44,55),
    "Occupation": "Software Engineer",
    "Address": "123 Main St",
    "learning": "coding",
    "time": 55,
}
print(len(list(std.keys())))
print(len(std))
print(std.values())
p = list(std.items())
print(std.items())
print(p[3])