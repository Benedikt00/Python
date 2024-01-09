import get_lines

pz_input = get_lines.read_file_to_array("input.txt")

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#for el in pz_input:
#	print(el)

dt = "."

sum = 0

for i, line in enumerate(pz_input):
	print(line, end=" ")
	switch = False
	posis = []

	for j, char in enumerate(line):
		if char in nums:
			if not switch:
				posis.append([j])
			switch = True
		elif switch:
			switch = False
			posis[-1].append(j-1)

	if len(posis[-1]) == 1:
		posis[-1].append(len(line)-1)
		#print(posis)

	for numb in posis:
		#print(numb, end = " ")
		character_near = False
		if numb[0] > 0:
			if line[numb[0]-1] != dt:
				character_near = True

		if numb[-1] < len(line) - 1:
			if line[numb[-1]+1] != dt:
				character_near = True

		if i > 0:
			for j in range(numb[0]-1, numb[-1]+2):
				if (j > 0) and (j < len(line)-1):
					if pz_input[i-1][j] != dt:
						#print(pz_input[i-1][j], " ", numb)
						character_near = True

		if i < len(pz_input)-1:
			#print(numb, " numb")
			for j in range(numb[0]-1, numb[-1]+2):
				if (j > 0) and (j < len(line)-1):
					if pz_input[i+1][j] != dt:
						character_near = True

		if character_near:
			sx = ""
			for x in range(numb[0], numb[-1]+1):
				sx += line[x]
			print(int(sx), end=" ")

			sum += int(sx)
	#if i > 6:
	#	print(posis)
	#	break
	print()
#454869
print(sum)