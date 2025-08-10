class Demo:
    pass

d1=Demo()

class Employee:
    '''This class is for maintaining Employee data'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        

e1 = Employee('Pritam', 25)
e2 = Employee('Rahul', 23)



print(isinstance(e1,Employee))

print(isinstance(d1,Employee))