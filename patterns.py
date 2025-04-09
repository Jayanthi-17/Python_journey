# write a program to print the following pattern:
#    *
#   ***
#  ***** for n=3

# n=input("enter a character: ")

#this program prints the pattern like 
# ***
# ***
# ***
# ***
# for i in range(4):# outer loop is for rows
#     for j in range(3):#inner loop id for columns
#         print("*", end="")
#     print()

#this program prints the pattern like
# 
# *
# **
# ***
# **** 
# for i in range(5):
#     for j in range(i):# i means here 5 that means goes upto 4 values only i.e,0,1,2,3,4 ....if we want more that is till 5 then write "i+1"
#         print("*",end="")
#     print()


# this program will print print pattern like:
# ****
# ***
# **
# *

# for i in range(5):
#     for j in range(5-i):
#         print("*",end="")
#     print()

#print multiplication table in reverse order:
num=int(input("enter a number"))
for i in range(10,0,-1):
    print(f"{num}x{i}={num*i}")