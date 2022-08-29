# place = " Pune"
# state = " Maharashtra"
# info = "I am from  "
# print(info.format(place))

# ## replace
# name = "Scott Billy"
# name1 = name.replace('l','m')
# print(name1)

# print(name1.strip())

# #reverse string
# name = "Scott Billy"[::-1]
# print(name)

#check palindrome

str = "Mom"

def palindrome(string):
    string = string.lower().replace(' ','')
    return string == string[::-1]

print(palindrome(str))

###Lower and upper

str = "HELLO WORLD"
print(str.lower())



