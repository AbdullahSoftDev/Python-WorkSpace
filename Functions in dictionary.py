std = {
    "Name": "Abdullah", 
    "Age": 25,
    "subjects": {
        "Math": 90,
        "Science": 85,
        "English": 88
        },
}
print(std["Name"])
print(std.get("Name2"))
std.update({"City" : "Gujranwala"})
print(std)