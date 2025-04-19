#write a program to generate multiplication table from 2 to 20 and write it to the different files. place these files in a folder for a 13 year old

def generatetable(n):
    table=""
    for i in range(1,11):
        table+=f"{n} x {i}= {n*i}\n"

    with open(f"tables/table-{n}.txt","w") as f:
        f.write(table)
    
for i in range(2,21):
    generatetable(i)
