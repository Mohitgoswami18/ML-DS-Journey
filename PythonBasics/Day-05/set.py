my_set = {1, 2, 3, 4, 5}

print("\nOriginal Set:", my_set)
my_set.add(6)
print("After add(6):", my_set)

my_set.remove(3)
print("After remove(3):", my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# Converting list to set to remove duplicates
dup_list = [1, 2, 2, 3, 3, 4]
unique = set(dup_list)
print("Unique from list:", unique)
