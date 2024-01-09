from sys import stdin

digits = ('zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine')

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


if '__main__' == __name__:
	print(sum(findNumbers(line) for line in lines))