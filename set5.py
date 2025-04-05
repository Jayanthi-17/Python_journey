#write a program to create a dictionary of hindi words with values as their english translation.provide user with an option to look it up

words={
    "khana":"food",
    "pani": "water",
    "nachna":"dance",
    "ghana":"sing"
}
word=input("enter any word u want translation for: ")
print(words[word])

#write a program to input eight numbers from user and diplay the unique numbers(once)
numbers=set()
num1=input("enter a number: ")
numbers.add(num1)
num2=input("enter a number: ")
numbers.add(num2)
num3=input("enter a number: ")
numbers.add(num3)
num4=input("enter a number: ")
numbers.add(num4)
num5=input("enter a number: ")
numbers.add(num5)
num6=input("enter a number: ")
numbers.add(num6)
num7=input("enter a number: ")
numbers.add(num7)
num8=input("enter a number: ")
numbers.add(num8)

print(numbers)

# can we a set with 18 as an interger and '18' as a string? yes
# proof:

s={18,6,7,"18"}
print(type(s))

#what will be the length of the set
s=set()
s.add(1)
s.add(1.0)
s.add("1")
# print(len(s))# answer is 2 because in python 1==1.0 is mathematically true so answer is 2


#create an empty dictionary,allow 4 friends to enter there fav languages as keys and use key as there names.assume that the names are unique

friends ={}
name=input("enter the name: ")
lang=input("enter favourite language: ")
friends.update({name:lang})

name=input("enter the name: ")
lang=input("enter favourite language: ")
friends.update({name:lang})

name=input("enter the name: ")
lang=input("enter favourite language: ")
friends.update({name:lang})

name=input("enter the name: ")
lang=input("enter favourite language: ")
friends.update({name:lang})

print(friends)

# can u change the values in a list which is inside a set// answer is we can not do becoz indexing is not possible in set so how can we edit we cant.the other reason is actualy a list shouls not be included within a set
s={8,7,12,"jay",[1,2]}
print(s.add1)
