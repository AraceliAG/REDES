def max (n1, n2, n3):
	if n1>n2:
		return f"larsgest number: { n1} "
	elif n2>n3:
		return f"largest number: {n2} "
	else:
		return f"largest number: {n3} "


n1 = int (input ("enter number 1: "))
n2 = int (input("enter number 2: "))
n3 = int (input("enter number 3: "))
print(max(n1, n2, n3))