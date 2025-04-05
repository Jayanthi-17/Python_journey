# write a python program to display a user entered name followed by good afternoon using input() function
name=input("enter your name: ")
print(f"good afternoon {name} how are you doing")

# write a program to fill in the letter template give below with name and date:

letter='''Dear <|name|>,
    you are selected
    <|Date|>'''

print(letter.replace("<|name|>","Jayanthi").replace("<|Date|>","17-nov"))


# write a program to detect double space in a String
val="hello welcome to my  world"#if no double space is there will return -1 else it will return the index of double space
print(val.find("  "))

# using escape sequence characters format the below string
letter="Dear Jayanthi,this python course is nice .Thanks!"

print("Dear \'Jayanthi\' \n\t" \
"This python course is nice.\nThankss\b")