# dict1 = {"age": 20 ,"Name": "Scott","dept":["cse","IT",'ECS'] }
# for x in dict1:
#     print(dict1[x])

# for x in dict1.items():
#     print(x)

# for x in dict1.values():
#     print(x)

# for x in dict1.keys():
#     print(x)

# dict1 = {"age": 20 ,"Name": "Scott","dept":"Cse","dept":"IT","Full Name":"Scott" }
# print(dict1)

# x = dict1["age"]
# print(x)

# x = dict1.items()
# print("adding value")
# dict1["Full Name"] = "Clerk"
# print(x)



# from os import remove


# dict1 = {"age": 20 ,"Name": "Scott","dept":"Cse","Full Name":"Scott" }

# del dict1["age"]
# dict1.pop("Full Name")

# print(dict1)


##Task 1
# print("........Task 1.........")
# dict1 = {}
# for x in range(5,11):
#     dict1[x] = x**2
# print(dict1)

# ##task 2
# print("........Task 2.........")
# keys = []
# values = []
# items = dict1.items()
# for x in items:
#     keys.append(x[0]),values.append(x[1])

# print(keys)
# print(values)

#  ## Task3
# print("........Task 3.........")
# x = zip(keys,values)
# dict3 = list(x)
# print(dict3)

# # ## Task 4
# print("........Task 4.........")
# n = 10 
# i = 0
# while(i<=n):
#     print(" "*(n - i)+"*" * i )
#     i+=1

# ## Task 5
# print("........Task 5.........")
# for i in range(1,101):
#     if( '7'or i%7 == 0 in str(i)):
#         print("I am perfect")
#     else:
#         print(i)

## Task 6
# print("........Task 6.........")
# num1 = 30
# num2 = 12
# num3 = 20
# num4 = 100
# num5 = 70
# if num1>num2:
#     if num1>num3:
#         if num1>num4:
#             if num1>num5:
#                 print(num1)
#             else:
#                 print(num5)
#         else:
#             if num4>num5:
#                 print(num4)
#             else:
#                 print(num5)
#     else:
#         if num3>num4:
#                 print(num4)
#         else:
#             print(num5)
# else:
#     if num3>num4:
#                 print(num3)
#     else:
#         print(num4)

# ## Task 7 
# print("........Task 7.........")
# list1= [5,True,"Hello",5.5]
# list2 =[]
# dict4 = {}
# for i in list1:
#     list2.append(type(i))
# dict4 = dict(zip(list1,list2))
# print(dict4.items())

# Task 8
# print("........Task 8.........")
# Stock ={"apple":78,"Orange":10,"Pears":5}
# Rates = {"apple":78,"Orange":40.5,"Pears":55,"Banana":10}
# order = {"apple":3,"Pears":6,"Orange":7,"pineapple":2}
# print(order)
# cost = {}
# orderList=[]
# orderCost=[]

# for i in order.keys():
#     orderList.append(i)

#     if(i in Stock.keys() and order[i]<Stock[i]):
#         orderCost.append(order[i]*Rates[i])
#         Stock[i]=Stock[i]-order[i]
#     elif(i in Stock.keys() and order [i]>Stock[i]):
#         orderCost.append(Stock[i]*Rates[i])
#         Stock[i]=0
#     else:
#         orderCost.append(0)
# cost =dict(zip(orderList,orderCost))
# print("Tptal Cost: ",cost.items())
# print("Updated stock: ",Stock.items())


# task 9
str = "I am sanket and I from pune,maharashtra."
dict1 = dict()
for i in str:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
for i in dict1.keys():
    if(dict1[i]>2):
        str = str.replace(i,'Z')
print(str)


print (str)