
try:
    a =10/0
except ZeroDivisionError:
    print("Dividing by zero is not allowed")
else:
    print(a)
finally:
    print("went through the try block")
print("Hello")