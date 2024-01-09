import get_lines

lines = get_lines.read_file_to_array("input.txt")

lines_split = []


for i, x in enumerate(lines):
	lines_split.append([])
	#print(x)
	lines_split[i] = (x.split(':', 1)[-1])
	lines_split[i] = lines_split[i].split(';')
	#print(lines_split[i])
	for k, y in enumerate(lines_split[i]):
		lines_split[i][k] = lines_split[i][k].split(',')
		dc1 = {}
		for l, z in enumerate(lines_split[i][k]):
			lines_split[i][k][l] = lines_split[i][k][l].strip().split(" ")
			dc1.update({lines_split[i][k][l][1]: lines_split[i][k][l][0]})
		lines_split[i][k] = dc1
	#print(lines_split[i])


#print(lines_split[0])

sum = 0

for i, el in enumerate(lines_split):
	print(el)
	rd_max = 0
	gr_max = 0
	bl_max = 0
	for j, col in enumerate(el):
		#print(col)
		if "red" in col:
			rd = int(col["red"])
			if rd > rd_max:
				rd_max = rd
		if "green" in col:
			gr = int(col["green"])
			if gr > gr_max:
				gr_max = gr
		if "blue" in col:
			bl = int(col["blue"])
			if bl > bl_max:
				bl_max = bl
	print(rd_max, gr_max, bl_max)
	sum += (rd_max * gr_max * bl_max)

print(sum)