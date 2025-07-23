# Base class
class Animal:
    def __init__(self, name): #Constructor
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Creating objects
animal = Animal("Generic Animal")

animal.speak()  # Output: Generic Animal makes a sound.

