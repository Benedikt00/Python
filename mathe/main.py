
total = 0

for i in range(270):
    r = 11.8 + i * -22.2e-3

    if i > 4:
        print( u -(2 * r * 3.14159))
    u = 2 * r * 3.14159
    total += u
    #print(u)

print(total)
