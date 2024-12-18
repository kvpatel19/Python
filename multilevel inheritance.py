class Animal:
    def __init__(self,name):
        self.name=name
    def cansay(self,voice):
        print(f"hello i am{self.name} and i say{voice}...")
class Dog(Animal):
    def eat(self):
        print("dog eat's paydegree")
class puppy(Dog):
    def walk(self):
        print("puppy walks slowly slowly")
od=Dog("Dog")
od.cansay("bow bow...")
od.eat()
od=puppy("puppy")

od.walk()
            
