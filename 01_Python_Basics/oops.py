class Human: #Baic class in python
    def __init__(self, name): #constructor of the human class
        self.name = name

human1 = Human("Mohit") #object of the human class
print(human1.name)

# Encapsulation 
# _variable_name = protected, __variable_name = private

class Vehicle: 
    def __init__(self, __mode):
        self.__mode = __mode # this is now a private variable
        print("This is the contructor of the parent class")

    def _get_mode (self):
        return self.__mode

class Car(Vehicle): # Inheritance
    def __init__(self, company, mode):
        super().__init__(mode)
        self.company = company

    
vehicle1 = Vehicle("Road")
print(vehicle1._get_mode())

car2 = Car("honda", "water")
print(car2.company, car2._get_mode())

class Utils:
    @staticmethod   #this is a static method
    def count(data):
        return data+1

