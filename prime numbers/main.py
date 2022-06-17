s = input("Check if this number is prime: ")
max = int(s)

for x in range(max , max+ 1 ):
    isPrime = True
    for y in range(2, int(x**0.5) + 1):
        if x % y == 0:
            isPrime = False
            break

    if isPrime:
        print("Is prime")
    else:
        print("is not prime")



