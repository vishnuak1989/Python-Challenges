class multiplesClass:
	n = 70
	def multiplegen(self):
		#numberlist = range(self.n)
		val = []
		for i in range(self.n):
			if i>0 and i % 7 == 0:
				 val.append(i)
		return val		

obj = multiplesClass()
obj.n = int(input("Enter the number to which the multiples of 7 is to be listed"))
#obj.n = 100;
val = obj.multiplegen()
for value in val:
	print (value)

				
