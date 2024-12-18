class Human:
    def __init__(self,name,age,gender):
        self.name=name
        self._age=age
        self.__gender=gender
    def showmember(self):
        print("gender is:",self.__gender)
obj=Human("kriyanshi",20,"female")
print("name is:",obj.name)
print("age is :",obj._age)
#print("genedr is:",obj.__gender)
obj.showmember()
