def suma (lista):
	contador = 0
	
	for i in lista:
		contador+=i
	return contador

def multi (lista):
	contador = 1
	for i in lista:
		contador*=i
	return contador


lista = []
num = int(input('longitud de la lista: '))

for i in range (num):
	num = int(input('ingrese numero: '))
	lista.append(num)

print(suma(lista))
print(multi(lista))