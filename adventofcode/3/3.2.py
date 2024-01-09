import get_lines

pz_input = get_lines.read_file_to_array("input.txt")

ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#for el in pz_input:
#	print(el)

dt = "."

sum = 0

for i, line in enumerate(pz_input):
	nums_for_line = []
	for j, char in enumerate(line):
		if char == "*":
			nums = []
			#check sideways
			if j > 0:
				if line[j-1] in ints:
					nums.append([])

					k = j-1
					while k >= 0:
						if line[k] in ints:
							nums[-1] += str(line[k])
						else:

							break
						k -= 1
					nums[-1].reverse()
					nums[-1] = int("".join(nums[0]))
			if j < len(line)-1:
				if line[j+1] in ints:
					nums.append([])
					k = j+1

					while k <= len(line)-1:
						#print(k)
						if line[k] in ints:
							nums[-1] += str(line[k])
						else:
							break
						k += 1
					nums[-1] = int("".join(nums[-1]))

			# up
			if i > 0:
				for x in range(j-1, j+2):
					if (x > 0) and (x < len(line) - 1):
						it = ""
						if pz_input[i-1][x] in ints:

							k = x - 1
							while k >= 0:
								if pz_input[i-1][k] not in ints:
									break
								k -= 1

							first_digit = k + 1

							k = x + 1
							while k <= len(line)-1:
								if pz_input[i - 1][k] not in ints:
									break
								k += 1
							last_digit = k - 1
							for o in range(first_digit, last_digit +1 ):
								it += pz_input[i-1][o]

						if it != "":
							if int(it) not in nums:
								nums.append(int(it))

			if i < len(line) - 1:
				for x in range(j-1, j+2):
					if (x > 0) and (x < len(line)-1):
						it = ""
						if pz_input[i+1][x] in ints:

							k = x - 1
							while k >= 0:
								if pz_input[i+1][k] not in ints:
									break
								k -= 1

							first_digit = k + 1

							k = x + 1
							while k <= len(line)-1:
								if pz_input[i + 1][k] not in ints:
									break
								k += 1
							last_digit = k - 1

							for o in range(first_digit, last_digit + 1):
								it += pz_input[i+1][o]

						if it != "":
							if int(it) not in nums:
								nums.append(int(it))

			if len(nums) > 1:
				nums_for_line.append(nums)
				#print(nums)
				sum += (nums[0] * nums[-1])

	print(line, end=" ")
	print(nums_for_line)
	#if i > 113:
	#	break

#88427264
#79386474 to low
print(sum)