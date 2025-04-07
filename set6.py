#write a program to find the greater of 4 numbers entered by the user
# num1=int(input("enter the number 1: "))
# num2=int(input("enter the number 2: "))
# num3=int(input("enter the number 3: "))
# num4=int(input("enter the number 4: "))

#using max method also u can solve
# maximum= max(num1,num2,num3,num4)
# print(f"the greatest number is : {maximum}")

# if(num1>num2 and num1>num3 and num1>num4):
#     print(f"Number {num1} is greater ")
# elif(num2>num1 and num2>num3 and num2>num4):
#     print(f"Number {num2} is greater ")
# elif(num3>num1 and num3>num2 and num3>num4):
#     print(f"Number {num3} is greater ")
# else:
#     print(f"Number {num4} is greater ")

# write a program to find out whether a student has passed or failed if it requires a total of 40% and 33% marks in each subjectss.assume 3 subjects and take marks as input from user
# num1=int(input("enter the number 1: "))
# num2=int(input("enter the number 2: "))
# num3=int(input("enter the number 3: "))

# total_percentage=((num1+num2+num3)/3)*100
# if(total_percentage >=40 and num1>=33 and num2>=33 and num3>=33):
#     print("congragulations you are passed!😍")
# else:
#     print("you are failed😒")


# a spam comment is defined as a text containing following keywords: "click this" "buy now " "make a lot of money" "subscribe this" .write a program to detect these spams.

# l1="click this"
# l2="buy now"
# l3="make a lot of money"
# l4="subscribe this"
# comment=input("enter your comment: ")
# if((l1 in comment) or (l2 in comment) or (l3 in comment) or (l4 in comment)):
#     print("this is spam message")
# else:
#     print("not a spam message")

# write a program to find whether a given username contains less than 10 characters or not

# user_name=input("enter your user name: ")
# if(len(user_name)<=10):
#     print("yes")
# else:
#     print("no")

#write a program which finds out where a given name is present in list or not
# l1=["apple","mango ","grape","kiwi","chinni","josh","jay","dikshh","ravi","paul","mukkuu"]
# name=input("enter your name: ")
# if(name in l1):
#     print("yes in list!")
# else:
#     print("no in list")


# write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100=>Ex
# 80-90=>A
# 70-80=>B
# 60-70=>C
# 50-60=>B
# <50  =>F

# Marks=int(input("enter your marks: "))
# if(Marks>90 and Marks<=100):
#     print("Your Grade is \'A\'")
# elif(Marks>80 and Marks<=90):
#     print("Your Grade is \'B\'")
# elif(Marks>70 and Marks<=80):
#     print("Your Grade is \'C\'")
# elif(Marks>60 and Marks<=70):
#     print("Your Grade is \'D\'")
# elif(Marks>50 and Marks<=60):
#     print("Your Grade is \'E\'")
# elif(Marks>=0 and Marks<=50):
#     print("Your Grade is \'F\'")
# else:
#     print("you entered an invalid marks")

# write a program to find whether a given post is talking about jayanthi or not
post=input("enter about post: ")
if("jayanthi".lower() in post.lower()):
    print("post is talking about jayanthi!")
else:
    print("Not talking about jayanthi")