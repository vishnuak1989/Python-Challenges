import math
cord=[0,0]
while True:
	pos= input("Enter Movement\n")
	if not pos:
		break
	input_array = pos.split(" ") 	
	position = int(input_array[1])
	direction = input_array[0]
	if direction == "UP":
		cord[0] += position
	elif direction == "DOWN":
		cord[0] -= position
	elif direction == "LEFT":
		cord[1] -= position
	elif direction == "RIGHT":
		cord[1] += position
	else:
		pass
print("final position")
print(cord)
print("Distance from (0,0)")
print (int(round(math.sqrt(cord[1]**2+cord[0]**2))))
		
		
		
		