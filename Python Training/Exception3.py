# try:
#      print(x)
# except Exception as e :
#     print("You encountered ",e,"exception.")
# else:
#     print("all is well")
# finally:
#     print("it is over")
# print(x)

try:
    age = 500
    if age>100:
        raise ValueError(age)
except ValueError:
        print("its is a ghost")
else:
    print("human")