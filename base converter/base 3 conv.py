run = True
num = ""
i = 1
b10 = input("Input a number from base 10: ")

b10 = int(b10)

nextnum = b10


while run:


    vor = nextnum
    nextnum = vor // 3
    nextrem = vor % 3


    print(str(nextnum) + " " + str(nextrem))


    num = str(nextrem) + num

    if nextnum == 0:
        run = False

print(num)





