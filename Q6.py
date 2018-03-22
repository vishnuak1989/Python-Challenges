import math
c = 50
h = 30
list_d = []
q=[]
d = input("Enter Values Seperated by Comma")
list_d = d.split(",")
listlen = len(list_d)
for x in list_d:
	q.append(str(int(round(math.sqrt((2*c*float(x))/h)))))
print (','.join(q))
