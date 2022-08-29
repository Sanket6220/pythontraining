f = open('Test.txt','r')
g = open('Text_Chen.txt','w')
e = open('Text_Ban.txt','w')
r = open('Text_rest.txt','w')
e.write("ID\t   Name\t    Dept\t   City\t      \tEmail    \t\tNew_Salary\n")
e.write("-----------------------------------------------------------------------\n")
g.write("ID\t   Name\t    Dept\t   City\t      \tEmail    \t\tNew_Salary\n")
g.write("-----------------------------------------------------------------------\n")
r.write("ID\t   Name\t    Dept\t   City\t      \tEmail    \t\tNew_Salary\n")
r.write("-----------------------------------------------------------------------\n")

counter = 0
line = f.readline()
while line:
    if line[15:24] == 'Bangalore':
        Salary = int(line[24:30])
        new_salary = Salary+(0.1*Salary)
        e.write(line[0:4]+'\t'+line[4:9]+'\t'+line[10:14]+'\t'+line[15:24]+'\t'+line[4:9]+line[15:19]+line[31:39]+'\t'+str(new_salary)+"\n")
    elif line[15:22] == 'Chennai':
        Salary = int(line[24:30])
        new_salary = Salary+(0.1*Salary)
        g.write(line[0:4]+'\t'+line[4:9]+'\t'+line[10:14]+'\t'+line[15:24]+'\t'+line[4:9]+line[15:19]+line[31:39]+'\t'+str(new_salary)+"\n")      
    else :
        Salary = int(line[24:30])
        new_salary = Salary+(0.1*Salary)
        r.write(line[0:4]+'\t'+line[4:9]+'\t'+line[10:14]+'\t'+line[15:24]+'\t'+line[4:9]+line[15:19]+line[31:39]+'\t'+str(new_salary)+"\n")
    line = f.readline()
f.close()
g.close()

