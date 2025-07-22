# Operators in python

# Arithmatic operators
x = 10
y = 3

print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.333...
print(x // y)  # 3
print(x % y)   # 1
print(x ** y)  # 1000

# comparison operators 
x = 5
y = 10

print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= y)   # False
print(x <= y)   # True

# assignment operators 
x = 5
x += 3   # x = x + 3
print(x) # 8

# logical operators
x = True
y = False

print(x and y) # False
print(x or y)  # True
print(not x)   # False

# bitwise operators
x = 5   # 0101
y = 3   # 0011

print(x & y)  # 1
print(x | y)  # 7
print(x ^ y)  # 6
print(~x)     # -6
print(x << 1) # 10
print(x >> 1) # 2

# Membership operators 
lst = [1, 2, 3]
print(2 in lst)    # True
print(5 not in lst)# True

# identity operators
x = [1, 2]
y = x
z = [1, 2]

print(x is y)     # True
print(x is z)     # False
print(x is not z) # True
