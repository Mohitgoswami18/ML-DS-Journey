# Creating tuple
t1 = (10, 20, 30)
t2 = ("Python", 3.14, True)

# Single element tuple → needs a comma
single = (5,)

t = (10, 20, 30, 40, 50)

print(t[0])     
print(t[-1])   
print(t[1:4])  

# Tuples are immutable unlike list in python

# Traversing in tuple
t = (10, 20, 30)
for value in t:
    print(value)

# Concatenation
a = (1, 2)
b = (3, 4)
c = a + b  

# Repetition
a * 3 
print(a)

t = (1, 2, 2, 3, 4)

print(t.count(2))
print(t.index(3))
print(max(t), min(t), sum(t))

# Tuple Unpacking
point = (4, 5)
x, y = point
print(x, y) 

t = (1, 2, 3, 4, 5)
a, *b, c = t
print(a, b, c)  # 1 [2, 3, 4] 5

# nested tuples 
matrix = ((1, 2), (3, 4), (5, 6))
print(matrix[1][0])
