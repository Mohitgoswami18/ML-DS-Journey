student = {
    "name": "Alice",
    "age": 21,
    "course": "Python"
}

print("Original Dictionary:", student)
print("Access 'name':", student["name"])
print("Using get():", student.get("age"))
print("All keys:", student.keys())
print("All values:", student.values())

# Adding and updating
student["grade"] = "A"
student["age"] = 22
print("Updated Dictionary:", student)

# Removing an item
student.pop("course")
print("After pop('course'):", student)

# Loop through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"{key} -> {value}")
