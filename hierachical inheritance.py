class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print(f"{self.name} ...says bhow...bhow..")
class puppy(Animal):
    def speak(self):
        print(f"{self.name} ...says bow...bow..")
dog=Dog("Dog")
puppy=puppy("puppy")
dog.speak()
puppy.speak()
