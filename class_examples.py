#create a class "pets" from a class "animals" and further create a class "dog" from "pets" and a method bark to class "dog".
class Animals:
    def show1(self):
        print("this is a animals class")
class Pets(Animals):
    def show2(self):
        print("this is a pets class")
class Dog(Pets):
    def bark(self):
        print("this is a dog class and dog barks as Bow-Bow ")
d=Dog()
d.show1()
d.show2()
d.bark()