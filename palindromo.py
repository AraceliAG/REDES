def es_palindromo(palabra):
	if palabra[::-1].lower() == palabra.lower() :
		return True
	else:
		return False

palabra = input('Ingresa palabra a evaluar ')

print(es_palindromo(palabra))




