# A string is a sequence of characters enclosed in single ('), double (") or triple quotes (''' or """).
# This is also known as docs string used for documenting purposes
'''
Strings are immutable (cannot be changed after creation).
'''
s1 = "Machine Learning"
s2 = 'AI'
s3 = """Deep Learning is powerful"""

s = "Python"

print(s[0])     
print(s[-1])    
print(s[0:4])   

s = "Python"
# s[0] = "J"  
s = "J" + s[1:]  
print(s)


s = " Machine Learning "

print(s.lower())      # " machine learning "
print(s.upper())      # " MACHINE LEARNING "
print(s.strip())      # "Machine Learning" (removes spaces)
print(s.replace("Machine", "Deep"))  # " Deep Learning "
print(s.split())      # ['Machine', 'Learning']
print("-".join(["ML", "AI"]))  # "ML-AI"
print(s.find("Learn"))  # 9 (index of substring)
print(s.count("a"))     # count of 'a'

name = "Alice"
score = 95

# here the string inside print is formate string
print(f"{name} scored {score} in ML")
