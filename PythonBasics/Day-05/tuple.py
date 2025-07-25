my_tuple = (10, 20, 30, 40)

print("Original Tuple:", my_tuple)
print("Accessing index 2:", my_tuple[2])
print("Length of tuple:", len(my_tuple))
print("Check if 30 in tuple:", 30 in my_tuple)
print("Slicing [1:3]:", my_tuple[1:3])

# Tuple unpacking
a, b, c, d = my_tuple
print("Unpacked Values:", a, b, c, d)

# Nested tuple
nested = (1, (2, 3), 4)
print("Nested Tuple Access (1,1):", nested[1][1])
