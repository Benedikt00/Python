from bs4 import BeautifulSoup
import requests

url = "http://192.168.0.4"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")



print(doc.prettify())

#with open("index.html", "r") as f:
#    doc = BeautifulSoup(f, "html.parser")
#    tags = doc.find_all("p")[0]
#    print(tags.find_all("b"))





