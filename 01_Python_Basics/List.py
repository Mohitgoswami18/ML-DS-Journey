# Creating a list
numbers = [10, 20, 30, 40]
mixed = [10, "Python", 3.14, True]
empty_list = []

data = [10, 20, 30, 40, 50]
print(data[0]) 
print(data[-1]) 
print(data[1:4])
data[0] = 100
data.append(60)     
data.insert(1, 15) 

data.pop()         
data.pop(1)          
data.remove(30)      

for value in data:
    print(value)

# list comprehension
squared = [x**2 for x in data]
cubes = [x**3 for x in range(1,10) if not(x%2)]
print(cubes)

a = [1,2,3]
b = [4,5]
c = a + b #this is called concatenation of lists

print (a * 2) #this is called repetition

# Nested Lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2]) 

# mathematical operations on list 
sample_list = [1,2,3,6,5,4,3]
print(max(sample_list), min(sample_list), sum(sample_list))
sample_list.sort() #sort in ascending order
sample_list.sort(reverse=True) #sort in descending order
sample_list.sort(key=lambda x: x%10) #sorting with custom key
print(sample_list)

sorted_sample_list = sorted(sample_list)
print(sorted_sample_list)