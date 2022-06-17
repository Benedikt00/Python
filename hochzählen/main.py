run = True
num = ""
i = 1
b10 = input("Input a number from base 10: ")
ct = int(input("Pic a base to convert this to (2-9): "))
b10 = int(b10)

nextnum = b10


while run:


    vor = nextnum
    nextnum = vor // ct
    nextrem = vor % ct

    num = str(nextrem) + num

    if nextnum == 0:
        run = False

print(num)





