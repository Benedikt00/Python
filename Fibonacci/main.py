
# 0 1 1 2 3 5 8

# i j y
#   i j y
#     i j y

max = input("Enter your Max Fibonacci number: ")

i = 0
j = 1
y = 1


while y <= int(max):
    print(y)

    y = i + j
    i = j
    j = y






