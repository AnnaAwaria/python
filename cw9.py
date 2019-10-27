lista2 = [2, 5, 7, 10, 15, 20, 30]

print("liczba elementow: " + str(len(lista2)))

b = sum(lista2)

print("suma elementow: " + str(b))


def suma(lista):
    suma_elementow = 0
    for element in lista:

        suma_elementow += element
    return suma_elementow


print(suma([2, 5, 7, 10, 15, 20, 30]))

