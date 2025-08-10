class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        

e1 = Employee('Pritam', 25)
e2 = Employee('Rahul', 23)


#Instance variables
e1.name="Pritam Saha"

print(e1.__dict__)


## Instance method ##

class Student:
    def __init__(self,nam,age):
        self.name=nam
        self.age=age

    def change_data(self):
        self.name="Pritam Saha"
        self.marks = 80


s1=Student("",25)
print(s1.__dict__)

s1.change_data()
print(s1.__dict__)