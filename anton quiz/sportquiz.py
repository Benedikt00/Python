import json
import os

print("----------Das Qiuz von Anton und Benedikt(super schwierig)--------------")

user = input("Bitte gib deinen Namen ein: ")

print("Starten!!!")
input()

fragen = [["Frage 1: In welchem Land spielen dies Spieler: Alaba, Schlager und Sabizer:", "Deutschland", "Östrerreich", "Schweiz", 2],
          ["Frage 2: Wieviele Championclegue-Tietel hat Real Madrid", "14", "13", "15", 1],
          ["Frage 3: Wer hat den Relord für den schnellsten Menschen der Welt:", "Karim Adelni", "Usain Bolt", "Alfonso Davis", 2],

          ["Frage 4: Wen nennt man auch La Pulga", "ronaldo", "Messi", "Neimar", 2],
          ["Frage 5: Wer hat die Basketball WM-2023 gewonnen", "Serbien", "Deutschland", "USA", 2],
          ["Frage 6: In welchem Pokal spielt Sturm Graz im moment", "UEFA-Championslegue", "UEFA-Konferenzlegue", "UEFA-Europalegue", 3],
          ["Frage 7: Welchen von diesen Sportarten gibt es wirklich", "Fußballfahrad", "Tippen", "Baumklettern", 1],
          ["Frage 8: Welches Land hat die meisten Fußballweltmeisterschaften", "Argentinien", "Deutschland", "Brasilien", 3],
          ["Frage 9: Welches Land hat die meisten Basketball WM-Tietel", "Argentinien", "Griechenland", "USA", 3],
          ["Frage 10 In welchem Land wurde due U-17 Weltmeisterschaft 2023 ausgetragen", "Spanien", "Türkei", "Indonesien", 3],
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

	while True:
		answer = input("Antwort: ")
		try:
			if int(answer) in [1, 2, 3]:
				score = check_answer(frage_, int(answer), score)
				break
		except ValueError:
			pass
		else:
			print("Answer Invalide")
	input()
	os.system('cls')

print("Dein Score ist: ", score)

with open("sj.json", "r") as f:
	inhalt = f.read()
	f.close()

inhalt = json.loads(inhalt)
inhalt[user] = str(score)

with open("sj.json", "w") as f:
	f.truncate(0)
	f.write(json.dumps(inhalt))


def print_scores(inhalt):
	print("Score Board: ")
	print(inhalt)

print_scores(inhalt)


