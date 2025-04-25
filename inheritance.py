#pass = "Do nothing, but syntactically correct."

class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"the name of the employee is {self.name} and the age is {self.age}")
    
class programmer(employee):
    def lang(self,languages):
        self.languages=languages
        print(f"the languages known by the {self.name} are {self.languages}")

a=employee("jayanthi",20)
b=programmer(a.name,a.age)# if u want to use the same name as that of parent class else programmer(josh,19) is also acceptable as arguments
a.show()
b.lang("python,java")