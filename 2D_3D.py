class twoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show1(self):
        print(f"the 2D vector is {self.i}i + {self.j}j")

class threeDVector(twoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show2(self):
        print(f"the 3D vector is {self.i}i + {self.j}j + {self.k}k")
        

a=twoDVector(8,3)
b=threeDVector(5,7,9)
b.show1()
b.show2()