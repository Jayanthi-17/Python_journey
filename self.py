class cseB:
    name="jayanthi"
    hallticketno="22D01A05B6"

    def getInfo(self):
        print(f"The name of the student is {self.name} ,bearing hallticket number {self.hallticketno}")
    @staticmethod
    def greet():
        print("Praise the Lord!")

student=cseB()
student.age=20
student.name="jayuuu"
# print(student.name,student.age,student.hallticketno)
student.getInfo()
student.greet()
