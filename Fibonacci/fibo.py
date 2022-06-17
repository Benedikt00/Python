to = input("Enter which Fibonacci Number do you want to see: ")

i = 0
j = 1
y = 1
max = 1
run = True


while run == True:
    y = i + j
    i = j
    j = y
    max += 1
    if max <= int(to) - 1:
        run = True
    else:
        run = False
print(y)