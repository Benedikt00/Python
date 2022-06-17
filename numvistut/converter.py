def convfrom10to(num, cto):

    run = True
    num2 = ""
    b10 = num
    nextnum = b10

    while run:

        vor = nextnum
        nextnum = vor // cto
        nextrem = vor % cto

        num2 = str(nextrem) + num2

        if nextnum == 0:
            run = False

    return int(num2)
j = 0
for i in range(100):
    j += 1
    print(convfrom10to(j, 9))




