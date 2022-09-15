def jhshsd(r2, r3, r4, r5, r6, r7):
    eq = 1/(1/(r2+1/(1/r4)+(1/r6)))+ (1/(r3+1/(1/r5)+(1/r7)))
    return eq

rges = 18


def pv(pvz, x):
    return (x/100) * pvz


def test(x, y):
    return 1 / (1 / x) + (1 / y)


def teststh(x):

    perc_x_y = (40, 60)
    while True:
        y = ((perc_x_y[0] + perc_x_y[1]) / 100) * perc_x_y[1]
        if round(test(x, y), 1) == 18:
            print(x, " ", y)
            break
        x += 0.01


r2 = pv(20, 4 * rges)
r3 = pv(30, 4 * rges)
r4 = pv(30, 4*pv(20, 4 * rges))
r5 = pv(25, 4*pv(30, 4 * rges))
r6 = pv(70, 4*pv(20, 4 * rges))
r7 = pv(75, 4*pv(30, 4 * rges))

print(jhshsd(r2, r3, r4, r5, r6, r7))