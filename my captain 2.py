terms_to_calculate=int(input("NUMBER:"))
n1, n2 = 0, 1
counted = 0
while counted < terms_to_calculate:
	print(n1)
	new_number = n1 + n2
	n1 = n2
	n2 = new_number
	counted += 1
