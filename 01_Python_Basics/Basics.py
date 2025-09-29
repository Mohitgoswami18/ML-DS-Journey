# Variables in Python

# Integer
age = 20

# Float
height = 5.9

# String
name = "Mohit"

# Boolean
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# Type checking
print(type(name), type(age), type(height), type(is_student))

# Multiple assignment
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# Loops in Python

# For loop
print("For loop")
for i in range(1, 6):
    print(i, end=" ")

print("\n")

# While loop
print("While loop")
count = 5
while count > 0:
    print("Count:", count)
    count -= 1

# Break, continue, pass
print("\nBreak / Continue / Pass")
for i in range(1, 6):
    if i == 3:
        continue  # skip 3
    if i == 5:
        break    # stop loop
    print(i)

# Pass does nothing
for i in range(3):
    pass


# Functions in Python

# Simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Mohit"))

# Function with default argument
def power(num, exp=2):
    return num ** exp

print("Square of 4:", power(4))
print("Cube of 4:", power(4, 3))

# *args 
def add_numbers(*args):
    return sum(args)

print("Sum:", add_numbers(1, 2, 3, 4, 5))

# **kwargs
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Mohit", age=20, country="India")
