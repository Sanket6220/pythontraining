# a = [1 , 'Hello', 3 , 3.4 , 6]
# print(len(a))
# print("Values in the list")
# print(a)
# #printing without index
# for x in range(len(a)):
#     print("At index: ",x,"-->", a[x])
# #without index
# print("printing the values without index")
# for b in a :
#     print(b)

# grades = [12,13,43,88,345,24]
# grades.append(88)
# print(grades)

# #combining two list

# a = [1,2,3,4,5,6]
# b = [7 ,8, 9 ,0]

# c = a+ b 
# a.extend(b)
# print(c)
# print(a)
# print(b)

# print(grades.count(88))


### insert in list 

# a = [ 1 , " hello ", 12 , 15.5]
# print(a)

# a.insert (2,"Tommy")
# print(a)
# #insert at last
# a.insert(len(a), 999)
# print(a)
# #at 2nd last
# a.insert(-1,"negative")
# print(a)

####################
#print a particular index value

# grades = [12,13,43,88,345,24]
# print(grades[2])
# #modify the 2nd index value
# grades[2]= 99
# print(grades[2])

#########################

# grades = [12,13,43,88,345,24]
# print(grades[2])
# print("the length before deleting: ",len(grades))
# popped = grades.pop(2)
# print(grades[2])
# print("the length after deleting: ",len(grades))
# print("the deleted item: ",popped)
# print("the remaining in the list: ",grades)

# grades = [57 ,74 ,74 ,49,888,87,66, 89,89,74,888,99]
# uniq_grades = list(dict.fromkeys(grades))
# print(grades)
# print(uniq_grades)
# print(grades.index(74))
# uniq_grades.remove(888)
# print(uniq_grades)
# uniq_grades.insert(4,44)
# print (uniq_grades)

################
# index of value 
# grades = [57 ,74 ,74 ,49,888,87,66, 89,89,74,888,99]
# print(grades.index(74))
# print(grades[1])

# from itertools import product


# sum = 0
# pro = 1
# grades = [5 ,3 ,4 ,2]
# for x in range(0,len(grades)):
#     sum = sum + grades[x]
#     pro = pro*grades[x]
# print("sum is ",sum)
# print("product: ",pro)
