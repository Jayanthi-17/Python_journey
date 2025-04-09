#print multiplication table using a for loop and while loop
#  num=int(input("enter a number: "))
 #for logic:
# for i in range(1,11):
#     print(num,"x",i,"=",(num*i))

#while logic
# num=int(input("enter a number: "))
# i=1
# while(i<=10):
#     print(f"{num} x {i}={num*i}")
#     i+=1

# write a program to greet all the persons in a list whose name starts with s
# l1=["jay","sur","sav","sath","sukhi","veer","lik"]
# for name in l1:
#     if name.startswith("s"):
#         print("hello",name)

# write a program to print whether a given number is prime or not?
# num=int(input("enter a number: "))
# for i in range(2,num):
#     if(num%i ==0):
#         print("not prime")
#         break
# else:
#         print("prime")

# write a program to find the sum of first n natural numbers using a while loop
# num=int(input("enter a numnber: "))
# sum=0
# i=0
# while(i<=num):
#     sum+=i
#     i+=1
# print(sum)

#write a program to calculate the factorial of a given number
num=int(input("enter a number: "))
p=1
for i in range(1,num+1):
    p=p*i
print(p)