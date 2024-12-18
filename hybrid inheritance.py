class Animal:
    def cansay(self):
        print(f"hello i am from animal class")
class Dog(Animal):
    def eat(self):
        print("dog eat's paydegree")
class puppy(Animal):
    def walk(self):
        print("puppy walks slowly slowly")
class bird(Dog,puppy):
    pass
    #def fly(self):
       # print("bird can fly in sky")
bird=bird()
bird.cansay()
bird.eat()
bird.walk()
#bird.fly()
            
