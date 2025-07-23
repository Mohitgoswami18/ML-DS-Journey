# Function without argument
def greet():
    print("Hello from a function!")

greet()

# Function with argument
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Mohit")

# Function with return value
def square(x):
    return x * x

print("Square of 5 is:", square(5))


# Regular function
def add(a, b):
    return a + b

# Lambda version
add_lambda = lambda a, b: a + b

print("Regular function result:", add(2, 3))
print("Lambda function result:", add_lambda(2, 3))
