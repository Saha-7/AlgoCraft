class Employee:
    def __init__(self,name,age,experience):
        self.name=name
        self.age=age
        self.exp=experience


e1 = Employee('Pritam', 25, 1)
e2 = Employee('Rahul', 23, 2) 


print(getattr(e1,'age'))

setattr(e2,'age',24)
print(getattr(e2,'age'))

delattr(e2,'exp')
print(e2.__dict__)


print(hasattr(e1,'fullName'))
print(hasattr(e2,'age'))





