
start_velocity = 1
end_velocity = 0.1
steps = 200

for x in range(200):
	v = (((2 * (start_velocity - end_velocity)) / pow(steps, 3)) * pow(x, 3)) - (
				((3 * (start_velocity - end_velocity)) / pow(steps, 2)) * pow(x, 2)) + start_velocity

	print(round(v, 2), " ", round(1/v, 2)/200*16*1000)


