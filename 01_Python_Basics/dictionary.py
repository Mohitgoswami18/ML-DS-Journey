# Empty dictionary
d = {}

# With data
student = {"name": "Alice", "age": 20, "grade": "A"}

student = {"name": "Alice", "age": 20}

print(student["name"])
print(student.get("age"))
print(student.get("score", "Not Found")) 

student["age"] = 21        
student["college"] = "IITD"  
print(student)


student.pop("grade", None) 
student.pop("name", "Alice")
student.popitem()          
del student["age"]        
student.clear() 
print(student)      

data = {"a": 1, "b": 2, "c": 3}
for key in data:
    print(key)

for value in data.values():
    print(value)

for key, value in data.items():
    print(key, value)


d = {"x": 10, "y": 20}

print(d.keys())    # return list of keys
print(d.values())  # return list of values
print(d.items())   # return list of key value pair
# Merge two dicts
d.update({"z": 30})

# Dictionary comprehension same as that of the list comprehension

# Nested Dictionaries
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 21, "grade": "B"}
}

print(students["Alice"]["grade"])  # A
