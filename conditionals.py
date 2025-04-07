#if-else

age=int(input("enter your age: "))
if(age>18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")



#if-else_elif_ladder

if(age>=0 and age<12):
    print("you are a child")
elif(age>12 and age<=19):
    print("you are a teenager")
elif(age>=20 and age<=30):
    print("you are a youth")
elif(age>30 and age<65):
    print("you are an adult")
elif(age>65 and age<120):
    print("you are an aged person")
else:
    print("you are entering an invalid age")
print("thank you!")