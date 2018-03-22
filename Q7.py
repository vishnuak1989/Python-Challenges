input_str = input("Enter two single digit numbers separated by comma")
dimensions = input_str.split(',')
rownum = int(dimensions[0])
columnnum = int(dimensions[1])
matrix = [[0 for col in range(columnnum)] for row in range(rownum)]
for row in range(rownum):
	for col in range(columnnum):
		matrix[row][col] = row*col

print (matrix)

