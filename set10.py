#1)create a class "programmer" to store information of few programmers working at microsoft
# class programmer:
#     name1="Jayanthi"
#     salary1="120000"

#     name2="Joshna"
#     salary2 ="120000"

#     name3="samson"
#     salary="100000"

# employee = programmer()
# print(employee.name1,employee.name2,employee.name3)

#(or)

# class programmer:
#     company="Microsoft"
#     def __init__(self,name,salary,age):
#         self.name=name
#         self.salary=salary
#         self.age=age

# p=programmer("jayanthi",120000,20)
# print(p.name,p.salary,p.age,p.company)
# r=programmer("joshna",120000,19)
# print(r.name,r.salary,r.age,r.company)
# q=programmer("solomon",120000,30)
# print(q.name,q.salary,q.age,q.company)

# 2)write a class "calculator" capable of finding sqaure,cube and square root of a number
# class calculator:
#     def __init__(self,number):
#         self.number=number
#     def square(self):
#             print(f"the square of the number {self.number} is {self.number**2}")
#     def cube(self):
#             print(f"the cube of the number {self.number} is {self.number**3}")
#     def squareroot(self):
#             print(f"the square root of the number {self.number} is {self.number**0.5}")
    
        
# calc=calculator(5)
# calc.square()
# calc.cube()
# calc.squareroot()

#3)create a class attribute a;create an object from it and set 'a' directly using object.a=o.Does this change the class attribute
# class sample:
#     a=10

# obj=sample()
# obj.a=0
# print("the class attribute: ",sample.a)
# print("the object attribute: ",obj.a)

# 4)add a static method in program2 to greet a user
# class calculator:
#     def __init__(self,number):
#         self.number=number
#     @staticmethod
#     def greet():
#           print("welcome to the calc problem")
#     def square(self):
#             print(f"the square of the number {self.number} is {self.number**2}")
#     def cube(self):
#             print(f"the cube of the number {self.number} is {self.number**3}")
#     def squareroot(self):
#             print(f"the square root of the number {self.number} is {self.number**0.5}")
# calc=calculator(5)
# calc.greet()
# calc.square()
# calc.cube()
# calc.squareroot()

#5) write a class "train" with has methods to book a ticket,get staus(no of seats), and get fare information of train running under Indian railways
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
          print(f"the name of the railways is {self.name} and the number of seats available are {self.seats}")
    def cost(self):
         print(f"The cost of the ticket is {self.fare}")
    def bookTicket(self):
        if (self.seats > 0):
              print(f"The seats are available and your Ticket is booked")
              self=-1
        else:
            print("Sorry tickets are not available")      
passenger=Train("rajdhani",580,7)   
passenger.getStatus()  
passenger.cost()
passenger.bookTicket()