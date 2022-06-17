from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


#tags = doc.find_all(text=re.compile("\$.*", limit=1) #druckt das Dollarzeichen und was danach kommt

#tags = doc.find_all(class_="btn-item")

#tags = doc.find_all(["option"], text= "Undergraduate", value = "undergraduate")

#tag = doc.find_all(["p", "div"])
#tag['value'] = 'new value'
#print(tag.attrs)

tags = doc.find_all("input", type= "text")

for tag in tags:
 #   print(tag.strip()) #macht alles schöner
    tag['placeholder'] = "I changed you"

with open("changed.html", "w") as file:
    file.write(str(doc))


