integers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
numbers = {"one": 1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}

numbers_inverse = {"1" : "one", "2": "two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9": "nine", "0":"zero"}

import re

def read_file_to_array(file_path):
	try:
		with open(file_path, 'r+') as file:
			lines = file.readlines()
			# Remove newline characters from the end of each line
			lines = [line.strip() for line in lines]
			return lines  # Return as a list (array)
	except FileNotFoundError:
		print(f"The file '{file_path}' was not found.")
		return []
	except Exception as e:
		print(f"An error occurred: {str(e)}")
		return []


lines = read_file_to_array("input.txt")

print(len(lines))

print(lines[0])

a = ""
b = ""
insg = 0


def check_sub_pos(string):
	ls = {}
	ls2 = []
	ls0 = {"one":[], "two":[], "three":[], "four":[], "five":[], "six":[], "seven":[], "eight":[], "nine":[], "zero":[]}
	for i, x in enumerate(numbers):
		for m in re.finditer(x, string):
			ls0[x].append(m.start())

	return ls0

from sys import stdin

digits = ('zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine')



lines = read_file_to_array("input.txt")

def findNumbers(line):
	numbers = []
	for i, c in enumerate(line):
		if c.isdigit():
			numbers.append(int(c))
			continue
		for n, name in enumerate(digits):
			if line[i:].startswith(name):
				numbers.append(n)
				break
	return numbers[0] * 10 + numbers[-1]


for line in lines:
	list = check_sub_pos(line)
	for i, c in enumerate(line):
		if c in integers:
			list[str(numbers_inverse[str(c)])].append(i)

	highest = -1

	for x in list:
		for y in list[x]:
			if y > highest:
				p = x
				highest = y

	#print(p)
	#print(numbers[str(p)])

	highest = 100

	for x in list:
		for y in list[x]:
			if y < highest:
				q = x
				highest = y

	print(line)
	print(list)
	print(q, p)
	u = int(str(numbers[q]) + str(numbers[p]))
	print(u, "u")
	insg += u
	if u != findNumbers(line):
		print("aaaaaaaaaaaaaaaaaaaaaaa")
		break
	print(insg, "insg")
	print()


print(insg)
print(53855)