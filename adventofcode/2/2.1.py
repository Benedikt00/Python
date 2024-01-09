import get_lines

lines = get_lines.read_file_to_array("input.txt")

lines_split = []

max = {"red" : 12, "green" : 13, "blue": 14}

for i, x in enumerate(lines):
	print(x)
	lines_split.append([])

	lines_split[i] = (x.split(':', 1)[-1])
	lines_split[i] = lines_split[i].split(';')
	#print(lines_split[i])
	for k, y in enumerate(lines_split[i]):
		lines_split[i][k] = lines_split[i][k].split(',')

		for l, z in enumerate(lines_split[i][k]):
			lines_split[i][k][l] = lines_split[i][k][l].strip().split(" ")
			lines_split[i][k][l] = {lines_split[i][k][l][1]: lines_split[i][k][l][0]}

	#print(lines_split[i])

#print(lines_split)

insg = 0

for i, line in enumerate(lines_split):
	#print(line)
	add = False
	for j, x in enumerate(line):

		for k, y in enumerate(x):
			key = list(y.keys())[0]

			if max[key] <= int(y[key]):

				add = True

	if add:
		insg += (i + 1)
		print(lines[i])
	else:
		pass
		print(i + 1, line)


#2913
print(insg)