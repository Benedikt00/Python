import keyboard as kb
from time import sleep
import asyncio
import os


def clear_console():
    os.system('cls')





fragen = [[["Warum ist das Formalexerzieren für einen Feuerwehrmann wichtig?"],
          ["Formalexerzieren ist nicht wichtig, da das Image der Feuerwehr allein vom Erfolg der Einsätze abhängt"],
          ["Das Image der Feuerwehr hängt auch vom Auftreten jedes einzelnen Feuerwehrmitgliedes und der gesamten Feuerwehr bei den verschiedensten Anlässen in der Öffentlichkeit ab"],
          ["Weil als Feuerwehrmann Disziplin und Ordnung sonst zu wenig verinnerlicht werden"],
          [2]]]

run = True



def print_right_answer(element_in_fragen):
    print(str(fragen[element_in_fragen][0])[2:-2])

    for el in range(1, len(fragen[element_in_fragen])-1):
        select = "[ ]"
        if el in fragen[element_in_fragen][-1]:
            select = "[X]"
        print(" ",select, " ", str(fragen[element_in_fragen][el])[2:-2])



akf = 0
while run:

    if kb.is_pressed("q"):
        run = False

    print(str(fragen[akf][0])[2:-2])

    selected_answer = 0
    sec_bef = selected_answer
    for el in range(1, len(fragen[akf])-1):
        select = "[ ]"

        if selected_answer == 0:
            print(" ", select, " ", str(fragen[akf][el])[2:-2])
        elif el == selected_answer:
            select = "[X]"
            print(" ",select, " ", str(fragen[akf][el])[2:-2])
        else:
            select = "[X]"
            print(" ", select, " ", str(fragen[akf][el])[2:-2])


    if kb.is_pressed("3"):
        selected_answer += 1


    if kb.is_pressed("4"):
        selected_answer -= 1

    print(selected_answer)
    input("")

    clear_console()

    print("..................-------..........")








