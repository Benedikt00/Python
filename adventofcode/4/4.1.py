import get_lines

lines = get_lines.read_file_to_array("input.txt")

inp = []

for x in lines:
	split_input = x.split("|")
	split_input[0] = split_input[0].split(":")[-1]

	for j, x in enumerate(split_input):
		split_input[j] = x.split()
	split_input.append(0)
	split_input.append(0)
	inp.append(split_input)

sum = 0

for w, ls in enumerate(inp):
	win = 0

	for winning_number in ls[0]:
		#print(winning_number)
		if winning_number in ls[1]:
			win += 1
	inp[w][-2] = win


for i, ls in enumerate(inp):
	for j in range(i + 1, i + inp[i][-2]+1):
		#print(ls, end=" ")
		inp[j][-1] += inp[i][-2]
		#print(j, inp[j][-2:11])

for x in range(len(inp)):
	print(inp[x])
	sum += inp[x][-1] + 1


print(sum)
