#write a program to find greatest of three numbers using function
# def greatestOfThree(a ,b,c) :
#     if(a>b and a>c):
#         print(f'{a} is the greatest of three')
#     elif(b>a and b>c):
#         print(f'{b} is the greatest of three')
#     else:
#         print(f'{c} is the greatest of three')
# greatestOfThree(10,12,15)
# greatestOfThree(21,19,15)

# #(or/optimal one)
# def greatestOfThree(a, b, c,d,e,f):
#     greatest = max(a, b, c,d,e,f)
#     print(f'{greatest} is the greatest of the three')

# Call the function
# greatestOfThree(10, 12, 15,54,74,96)

#write a python program using functions to convert celsius to fahrenhiet
#formula of Fahrenheit=(Celsius× 9/5​)+32

# def conversion(celsius):
#     fahrenheit= (celsius*9/5)+32
#     print(f'the fahrenheit percentage is: {fahrenheit} °F') 
#     celsius=int(input("Enter the celsius percent: "))

# conversion(52)

#how do u prevent a python print() function to print a new line at the end
#answer: By using end="" 
# print("a")
# print("a")
# print("a",end="")
# print("a",end="")
# print("a")

#write a recurssive function to print the sum of first n natural number?
#recursive method without taking input from user:
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n
# print(sum(85))

#recursive method with taking input from user:
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n

# num=int(input("Enter a number: "))
# result=sum(num)
# print(f'The Sum of {num} natural numbers are: {result}')


#general method:
# def sum_of_num(n):
#     total=0
#     for i in range(n+1):
# #         total=total+i
# #     return total

# # num=int(input("enter the number: "))
# # result=sum_of_num(num)
# # print(f'The sum of {num} natural numbers are: {result}')

# # write a python function to print the following pattern
# # ***
# # ** for n=3
# # *

# def pattern(n):
#     for i in range(n):
#         for j in range(n-i):
#             print("*",end=" ")
#         print()

# pattern(5)

# #write a python function to convert inches to cm:
# #cm=inches×2.54
# def inches_to_cm(inches):
#     cm=inches*2.54 
#     print(f' {inches} inches is equal to  : {cm} centimeters')

# inches_to_cm(10)

# #with user input:
# def inches_to_cm(inches):
#     cm=inches*2.54 
#     print(f' {inches} inches is equal to  : {cm} centimeters')

# inches=int(input("enter the length in inches: "))
# inches_to_cm(inches)


# write a python function to remove given word  from the list and strip it at a same time
# write a python function to print multiplication table of a given number:
def mul_n(n):
    for i in range(1,11):
        print(f'{n}x{i}={n*i}')
    
n=int(input("enter a number for multiplication table: "))
mul_n(n)
