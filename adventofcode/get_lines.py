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

