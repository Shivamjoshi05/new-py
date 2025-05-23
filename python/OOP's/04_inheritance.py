class Animal:
    location = "India"
    def __init__(self,name):
        self.name= name
    def speak(self):
        print("Speaking Now......")
    
class Dog(Animal):
    def speak(self):
        super().speak() # we are using the speak 
        print("Woof!")

d = Dog("Robin")
d.speak()
print(d.location)