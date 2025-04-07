#example of for loop
 for i in range(1,100):
    print("Jayanthi",i)

#example of while loop
 i=0
while(i<=50):
    print(i)
    i+=1

# example 2
l1=["jay","sh","hu","hy","yy"]
i=0
while(i<=4):
    print(l1[i])
    i+=1

# for-else loop
# else block will be executed when all the iterarions in for bock are exhausted

for i in range(1,11):
    print(i)
else:
    print("thank you jayuuu!")

for i in range(50):
    if(i%2!=0):
        continue
    print(i)
