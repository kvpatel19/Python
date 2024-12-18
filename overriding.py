class DemoA:
    def display(self):
        print("hello good morning")
class DemoB(DemoA):
    def display(self):
        super().display()
        print("i am overriding method")
obj=DemoB()
obj.display()
