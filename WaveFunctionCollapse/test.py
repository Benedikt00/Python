GridSize = [4, 4]

Positions = []
for i in range(GridSize[0]):
	dt = []
	for j in range(GridSize[1]):
		dt.append([])
	Positions.append(dt)

num = 0

for i, el in enumerate(Positions):
	for j, el2 in enumerate(el):
		Positions[i][j] = num
		num += 1

for el in Positions:
	print(el)

pos = [2, 2]

print(Positions[pos[0]][pos[1]])
print(Positions[pos[0]][pos[1] + 1])
print()

