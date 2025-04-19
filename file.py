# f=open("abc.txt")
# d=f.read()
# print(d)
# f.close()

# this program will open a file in write mode,if there is no file then it will create one .and then it will write the given string to the file
# sample="hey are u doing! hope all is GOOD!"
# # sample=input("enter ur string: ")
# # sample2=input("enter ur string: ")
# f=open("writing.txt","w+")
# var=f.write(sample)
# # f.append(sample2)
# f.seek(0)
# content=f.read()
# print(content)
# f.close()


# everytime we have to explicitly close the file. instead we can use other way that is using with statement
# with open("abc.txt","w+") as f:
#     print(f.write("jayanthi"))
#     f.seek(0)
#     var=f.read()
#     print(var)

#write a program to read a file from poem.txt and find out whether the word "twinkle" is present or not
# with open("poem.txt","w+") as f:
#     p=''' twinkle twinkle little star
#     how i womder what u want
#     up above the what so high
#     like a diamond in the sky!
    # '''
    # f.write(p)
    # f.seek(0)
    # poem=f.read()
    # if "twinkle" in poem:
    #     print("YES! twinkle word is present")
    # else:
    #     print("NO! twinkle word is not present")


#the game() function in a program lets a user play a game and returns the score as an interger .you need to read a file "hi-score.txt" which is either blank or contains the previous high score .you need a write a program to update the hi-score whnever the game function breaks the hi-score

import random
def game():
    print("you are playing a game...")
    score=random.randint(1,85)
    with open("hi-score.txt","r") as f:
        highscore=f.read()
        if (highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0
    print(f"your score is: {score}")
    if (score>highscore):
        with open("hi-score.txt","w") as f:
            f.write(str(score))
    return score

    
game()

