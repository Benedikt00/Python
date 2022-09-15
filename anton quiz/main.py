import json
import os

print("----------Das Qiuz von Anton und Benedikt(super schwierig)--------------")


user = input("Bitte gib deinen Namen ein: ")

print("Starten!!!")
input()

fragen = [["Frage 1: \nWas ist das am dünnsten besiedelte Land der Erde?", "Venezuela", "Canada", "Russland", 3],
          ["Frage 2: \nWas ist die Hauptstadt der USA?", "Washington-DC", "New-York", "Los-Angeles", 1],
          ["Frage 3: \n Was ist das größte Stillgewässer der Erde?", "Kaspisches Meer", "Michigan See", "Wörthersee", 1],
          ["Frage 4: \n Welches Land ist am dichtesten Besiedelt?", "Indien", "Macau", "Singapur", 2],
          ["Frage 5: \n Welche Stadt hat am meisten Einwohner?", "New-York", "Peking", "Mexico-City", 3],
          ["Frage 6: \n Welches EU-Land hat die größte Fläche?", "Spanien", "Niederlande", "Frankreich", 3],
          ["Frage 7: \n Wo steht das größte gebäude der Erde", "Vereinigte Arabische Emerate", "Dubai", "Indonesien", 2],
          ["Frage 8: \n Welcher EU-Mitgliedsstaat hat die meisten Einwohner?", "Deutschland", "Frankreich", "Spanien", 1],
          ["Frage 9: \n Welcher Bundesstaat der USA ist der größte?", "Alaska", "Texas", "Washington", 1],
          ["Frage 10: \n Welches Land ist das größte in Nordamerika?", "Mexico", "USA", "Canada", 3]
          ]

score = 0

def print_question(frage):
    print(frage[0])
    print("1: " + frage[1])
    print("2: " + frage[2])
    print("3: " + frage[3])

def check_answer(frage, answer, score):
    if answer == frage[-1]:
        print("Correct")
        score += 1
        return score
    else:
        print("Incorrect")
        return score

for frage_ in fragen:
    print_question(frage_)
    answer = input("Antwort: ")
    score = check_answer(frage_, int(answer), score)
    input()
    os.system('cls')
    
print("Dein Score ist: ", score)


with open("scores.json", "r") as f:
    inhalt = f.read()
    f.close()

inhalt = json.loads(inhalt)
inhalt[user] = str(score)

with open("scores.json", "w") as f:
    f.truncate(0)
    f.write(json.dumps(inhalt))

#def print_scores(inhalt):
#    print("Score Board: ")



