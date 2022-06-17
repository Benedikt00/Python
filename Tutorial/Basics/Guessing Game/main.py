sw = "Giraffe"
guess = ""
tg = 0
gl = 3
oof = False


while guess != sw and not(oof):
    if tg < gl:
        guess = input("Enter guess: ")
        tg += 1
    else:
        oof = True

if oof == True:
    print("Loser")
else:
    print("It's right")