d={}#empty set
a={
    "name":"jayanthi",
    "grade":"O",
    "section":"B"
}
print(a.items())#prints both keys and values
print(a.keys())#prints keys in dictionary
print(a.values())#prints values in dictionary
print(a.get("grade"))# returns a value at a specified key(returns value for it)
print(a.get("grade1"))# return none 
print(a["grade1"])# returns key error
