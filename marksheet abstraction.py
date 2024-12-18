from abc import ABC
class student(ABC):
    def __int__(self,m1,m2,m3,m4,m5,m6):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
        self.m6=m6
    def marksheet(self):
        pass
class Bca(student):
    def marksheet(self):
        print("m1 is",self.m1)
        print("m2 is",self.m2)
        print("m3 is",self.m3)
        print("m4 is",self.m4)
        print("m5 is",self.m5)
        print("m6 is",self.m6)
bca=Bca(34,54,67,32,27,19)
bca.marksheet()
        
        
