
#the file contains a word donkey multiple times .u need to write a program which replace this word with "######" by updating the same file.
with open("def.txt","a+") as f:
    f.seek(0)
    content=f.read()
    print(f"original content: {content}")
updated_content=content.replace("donkey","#######")
with open("def.txt","w") as f:
    f.write(updated_content)
print(f"updated content is: \n{updated_content}")

#repeat the above program for a list of such words to be censored
words_to_censor=["donkey","jerusalem","palm"]
with open("def.txt","a+") as f:
    f.seek(0)
    content=f.read()
    print(f"original content: {content}")

for word in words_to_censor:
    content=content.replace(word,"#######")

with open("def.txt","w") as f:
    f.write(content)
print(f"updated content is: \n{content}")




