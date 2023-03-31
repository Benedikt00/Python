from math import sin

f = lambda x : x

f2 = lambda x, y: x + y

height, width = 14, 14



def draw_function(f_x):
	num = 0
	leinwand = []
	
	for i in range(height):
		fu = []
		for j in range(width):
			fu.append(" ")
		leinwand.append(fu)


	for i in range(height):
		y = round(f_x(i))
		if 0 <= y < height:
			leinwand[y][i] = "*"
			print(i, y)
			num += 1
	
	for x in reversed(leinwand):
		for y in x:
			print(y + "  ", end="")
		print()




draw_function(f)

