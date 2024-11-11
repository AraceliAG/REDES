vocales = 'aeiouAEIOU'

def vocal(a):
	if a in vocales:
		return True
	else:
		return False

a = input('Ingresa un carácter:  ')
print(vocal(a))