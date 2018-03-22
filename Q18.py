import re
passwords=[]
str = input("Enter Passwords seperated by comma \n")
passwords= str.split(',')
corr_passwords=[]
for password in passwords:
	if len(password)>6 and len(password)<12:
		if re.search("[a-z]",password):
			if re.search("[0-9]",password):
				if re.search("[A-Z]",password):
					if re.search("[$#@]",password):
						if not re.search("\s",password):
							corr_passwords.append(password)
print("The list of passwords that meet the criteria are:\n")							
print(",".join(corr_passwords))
