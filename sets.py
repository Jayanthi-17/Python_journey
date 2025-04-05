# #set is a collection of non-repetitive elements
# s=set()# denotes an Empty set
# print(type(s))

# s={1,8,9,7,5,6,4}
# # print(len(s))
# print(s.add(12))
# # print(s.pop())
# # print(s.remove(5))
# print(s)

#METHODS :

a={1,2,3}
b={2,3,4}
print(a.union(b))#union opertion
print(a.intersection(b))#intersection
print(a.difference(b))#difference
print(a.symmetric_difference(b))#except common elements in both sets it will print all the remaining elements in both sets

c={5,6}
d={5,6,7}
print(c.issubset(d))
print(d.issuperset(c))
print(c.isdisjoint(d))
print(c.isdisjoint(a))