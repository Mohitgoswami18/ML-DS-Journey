# type conversion 
# they are of 2 types

# 1 -> implicit (automatic)
a = 2
b = 4
c = a/b
print(type(a), type(b), type(c))

# 2 -> explicit (manual)
a = "5"
print(type(a))

a = int(a) 
print(type(a)) 