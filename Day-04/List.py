# Basic List Operations
lst = [10, 20, 30, 40, 50]

print("\nOriginal List:", lst)
print("Length of list:", len(lst))
print("Access index 2:", lst[2])
print("Slice [1:4]:", lst[1:4])
print("Sum of elements:", sum(lst))
print("Maximum:", max(lst))
print("Minimum:", min(lst))

# Modifying list
lst.append(60)
print("After append(60):", lst)

lst.insert(2, 25)
print("After insert at index 2:", lst)

lst.remove(40)
print("After removing 40:", lst)

lst.pop()
print("After pop():", lst)

lst.reverse()
print("After reverse():", lst)

lst.sort()
print("After sort():", lst)
