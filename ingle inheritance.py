class Animal:
    def __init__(self,name):
        self.name=name
    def cansay(self,voice):
        print(f"{self.name}can say{voice}...")
class Dog(Animal):
    def eat(self):
        print("dog eat's paydegree"")
od=Dog("Dog")
od.cansay("bow bow...")
od.eat()
            
