def superposicion(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                return True 
    return False

longitud = int(input('Ingresa la longitud de tus lista '))
lista1 = []
lista2 = []
print("Lista 1")
for i in range (longitud):
	n1 = input('ingresa dato ')
	lista1.append(n1)
print("Lista 2")
for i in range (longitud):
	n2 = input('ingresa dato ')
	lista2.append(n2)

print(superposicion(lista1, lista2))