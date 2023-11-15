while True:
	num_in = input("Input your Number: ")
	last_int = str(num_in)[-1]
	if (last_int == "5") or (last_int == "0"):
		print(num_in, "ist Ganzzahlig ohne Rest durch 5 teilbar")
	else:
		print(num_in, "ist NICHT Ganzzahlig ohne Rest durch 5 teilbar")

	if input("Terminate[j/n]") == "j":
		break