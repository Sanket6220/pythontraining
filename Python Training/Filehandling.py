# f = open('Test.txt','r')
# line = f.read()
# print(type(line))
# print(line)


f = open('Test.txt','r')
line = f.readline() 
counter = 0
while line:
    counter = counter+1
    print("Record number: ",counter)
    id = line[0:3]
    print("ID = " ,id)
    name = line[4:9]
    print("Name = " ,name)
    Dept = line[10:14]
    print("Dept = " ,Dept)
    Loc = line[15:24]
    print("Location = " ,Loc)
    
    Email = line[4:9]+line[15:19]+line[31:39]
    print("Email = " ,Email)
    Salary = int(line[24:30])
    print("Salary = " ,Salary)
    if(Loc == 'Chennai'):
        newSalary = Salary+(0.1*Salary)
    elif(Loc == 'Pune'):
        newSalary = Salary+(0.15*Salary)
    else:
        newSalary = Salary+(0.2*Salary)
    print("New Salary = ",newSalary)
    print("*******************\n")
    line = f.readline()
f.close()
print("*********ALL RECORDS ***********")