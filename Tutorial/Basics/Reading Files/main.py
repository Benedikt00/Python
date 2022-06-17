

employee_file = open("employees.txt", "r+") # r = read, w = overwrite all , a = add something at the end, r+ = r and w
print(employee_file.readable())
#print(employee_file.read()) das ganze dokument
#print(employee_file.readline()) liest eine Zeile
#print(employee_file.readlines()[0]) liest eine bestimmte Zeile in der Liste

for employee in employee_file.readlines():
    print(employee)



employee_file.close()
