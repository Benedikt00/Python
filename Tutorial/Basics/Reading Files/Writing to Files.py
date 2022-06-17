employee_file = open("employees.txt", "a")
i = 1
while i <= 2:
    employee_file.write("\nToby - Human Resources")
    i += 1
else:
    employee_file.close

employee_file = open("employees1.txt", "w") #erstellt ein neues dokument und schreibt darin mann kann auch z.b html code erstellen
employee_file.write("aölskjfvboasiru<üäcjkgifosakldgut93rwqopdklsfjtg")

#import time
#time.sleep(2) #verzögert um 5 sekunden
#import os
# #os.remove("employees1.txt") #löscht die Datei
