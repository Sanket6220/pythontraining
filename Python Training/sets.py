# Set1 = {"hello","HELLO",45,90,True}
# Set2 = {"mark",False,55,100}
# y = Set1.update(Set2)
# x = Set1.union(Set2)
# print(Set1)
# print(x)

# ## adding item to the set
# Set1.add("Timmy")
# print(Set1)


# print("HELLO" in Set1)

Set1 = {"hello","HELLO",45,90,True}
Set2 = {"mark",False,55,45,"HELLO"}
print(Set1.difference(Set2))
print(Set1.intersection(Set2))
print(Set2-Set1)

Set1.remove("HELLO")
print(Set1)

Set1.discard("Sanket")
print(Set1)
n = Set2.pop()
print (n)
print(Set2)

Set1.clear()
print(Set1)

