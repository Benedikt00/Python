zahlen = [2, 54, 21, 68, 91, 4, 7]
friends = ["Rutter", "Marci", "Vogi", "Hogwart", "Vogi", "Witi", "Vogi"]

print(friends)
friends.append("Creed")  # hängt am ende an gegenteil .pop
friends.insert(2, "Kuchen")
friends.remove("Witi")
print(friends)

friends.pop()
print(friends)

zahlen.sort() #entwerde Zahlen oder Strings
print(zahlen)

friends2 = friends.copy()

friends.extend(zahlen)

print(friends.index(91))  # gibt den platz des strings aus
print(friends.count("Vogi"))

friends.reverse()
print(friends)

print(friends2)

friends.clear()
print(friends)