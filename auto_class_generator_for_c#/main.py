"""
                ZweiAHET[0].Vorname = "Benedikt";
                ZweiAHET[0].Nachname = "Simbürger";
                ZweiAHET[0].Alter = 15;
"""

names = ["Paul", "Johanna", "Christoph", "Matthias", "Kati", "Benedikt", "Johannes", "Marco", "Simone", "Vincent", "Daniel", "Elena"]
lastnames = ["Wernig", "Panzer", "wohleser", "Stözl", "Lindner", "Simbürger", "Rutter", "Schönfelder", "totora", "Sonne", "Ronacher", "Widmann"]
ages = [4, 5, 4, 6, 5, 6, 7, 5, 5, 6, 5, 7, 5, 6, 7]

for x in range(len(ages)):

    ages[x] = ages[x] + 10

for x in range(len(ages)):
    print(f"ZweiAHET[{x}].Vorname = \"{names[x]}\";\nZweiAHET[{x}].Nachname = \"{lastnames[x]}\";\nZweiAHET[{x}].Alter = {ages[x]};\n          "
          )
