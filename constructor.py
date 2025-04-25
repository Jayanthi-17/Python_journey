class Student:
    def __init__(self, name, age):  # This is the constructor # also know about dunder methods
        self.name = name
        self.age = age

# Creating an object of the class
s1 = Student("Alice", 20)
print(s1.name)  # Alice
print(s1.age)   # 20
