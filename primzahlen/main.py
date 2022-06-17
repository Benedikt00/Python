max = 10**6

for x in range(2, max + 1 ):
    isPrime = True
    for y in range(2, int(x**0.5) + 1):
        if x % y == 0:
            isPrime = False
            break

    if isPrime:
        print(x)

