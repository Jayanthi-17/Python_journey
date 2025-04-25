#single inheritance
class Parent:
    def display1(self):
        print("parent class for single inheritance")
class child(Parent):
    def display2(self):
        print("child class for single inheritance")
obj1=child()# we are creating object for child class because the parent class properties are inherited into child class
obj1.display1()
obj1.display2()

#multiple inheritance
class father:
    def show1(self):
        print("father class for multiple inheritance")
class mother():
    def show2(self):
        print("mother class for multiple inheritance")
class child(father,mother):
    def show3(self):
        print("Child class for multiple inheritance")
obj2=child()
obj2.show1()
obj2.show2()
obj2.show3()

#multilevel inheritance
class computer_science:
    def sub1(self):
        print("computer science an outer(1) class example for multilevel inheritance")
class artificial_intelligence(computer_science):
    def sub2(self):
        print("artificial intelligence an outer(2) class example for multilevel inheritance ")
class machine_learning(artificial_intelligence):
    def sub3(self):
        print("Machine learning an outer(3) class example for multilevel inheritance")
mlobj=machine_learning()
mlobj.sub1()
mlobj.sub2()
mlobj.sub3()

#heirarichal inheritance
class venkateshwarlu_vijayalaxmi:
    parents="Venkateshwarlu_And_VijayaLaxmi"
    def fam1(self):
        print("this is parent class for heirarichal inheritance")
class jayanthi(venkateshwarlu_vijayalaxmi):
    def fam2(self):
        print(f"This is child 1 of parents {self.parents}class for heirarichal inheritance")
class joshna(venkateshwarlu_vijayalaxmi):
    def fam3(self):
        print(f"This is child 2 of parents{self.parents} class for heirarichal inheritance")
elder=jayanthi()
elder.fam2()
younger=joshna()
younger.fam3()

#hybrid inheritance 
class A:
    def methodA(self):
        print("Class A")

class B(A):
    def methodB(self):
        print("Class B")

class C(A):
    def methodC(self):
        print("Class C")

class D(B, C):
    def methodD(self):
        print("Class D")

obj = D()
obj.methodA()
obj.methodB()
obj.methodC()
obj.methodD()
