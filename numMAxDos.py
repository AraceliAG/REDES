def max (n1, n2):
	if n1>n2:
		return f"larsgest number: { n1} "
	elif n1<n2:
		return f"largest number: {n2} "
	else:
		return f"equal number"


n1 = int (input ("enter number 1: "))
n2 = int (input("enter number 2: "))
print(max(n1, n2))