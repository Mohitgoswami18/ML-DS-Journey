# Creating sets
s = {1, 2, 3, 4}
s2 = set([1, 2, 2, 3])   # {1, 2, 3}
empty_set = set()        # {} is NOT empty set → it's a dict

# Sets are unordered so we cant use indexing
s = {10, 20, 30}
for value in s:
    print(value)

s = {1, 2, 3}
s.add(4)
s.update([5, 6, 7])
s.remove(3)  
s.discard(10)
s.pop()
s.clear()


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union: {1,2,3,4,5,6}
print(a & b)   # Intersection: {3,4}
print(a - b)   # Difference: {1,2}

nums = {5, 2, 9, 1}

print(len(nums))   # 4
print(min(nums))   # 1
print(max(nums))   # 9
print(sum(nums))   # 17

#  Set Comprehension is same as that of list in python


# These are immutable cateogary of sets
fs = frozenset([1, 2, 3]) 
