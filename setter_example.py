''' create a class "employee" and add salary and increment properties to it.
write a method "salaryafterincrement" method with a @property decorator with a setter which changes the value of increment based on the salary'''

class Employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
    @property
    def salaryafterincrement(self):
        return self.salary*(1+self.increment)
    @salaryafterincrement.setter
    def salaryafterincrement(self,new_salary):
        increment=(new_salary-self.salary)/self.salary
e=Employee(5000,0.3)
# print(e.salaryafterincrement)
# e.salaryafterincrement=6500
print(e.increment)
print(e.salaryafterincrement)



