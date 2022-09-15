import datetime
import random
import matplotlib.pyplot as plt
import json

json_file = open("items.json")
items_to_get = json.load(json_file)
json_file.close()

x = []
y = []

for key in items_to_get:
    for data in items_to_get[key]["datensatz"]:
        x.append(data[0])
        y.append(data[1])

# plot
plt.plot(x, y)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()

