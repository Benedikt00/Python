import time
from time import sleep


a_file = open("data", "r")
lines = a_file.readlines()
listOfStrings = lines[-5:]


result = False
if len(listOfStrings) > 0 :
    result = all(elem == listOfStrings[0] for elem in listOfStrings)
if result :
    print("All Elements in List are Equal")
else:
    print("All Elements in List are Not Equal")

    time_object = time.localtime()
    local_date = time.strftime("%M", time_object)
while local_date == "1":
    time = True
    sleep(60)
else:
    time = False


while result or time:






