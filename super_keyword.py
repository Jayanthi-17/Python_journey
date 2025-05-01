#The super() keyword in Python is used to call methods or constructors from a parent (super) class. It's especially useful when you want to extend the functionality of the parent class rather than completely overriding it.
class grandfather:
    def __init__(self):
        print("this is grandfather class")

class father(grandfather):
    def __init__(self):
        print("this is parent class")#this will be printed only when a super keyword is used in child class method
print("example check")#this will be executed because it is not part of constructor or method so it will execute
class child(father):
    def __init__(self):
        # super().__init__()
        print("this is child class")

obj=child()