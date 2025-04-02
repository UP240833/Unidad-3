
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [num for num in numbers if num <= 0]
print(negativos_y_ceros)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplanada = [num for sublist in list_of_lists for num in sublist[0]]
print(aplanada)


lista_tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(lista_tuplas)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
nueva_lista = [[pais[0].upper(), pais[0][:3].upper(), ciudad.upper()] for pais, ciudad in [item[0] for item in countries]]
print(nueva_lista)

lista_diccionarios = [{'country': pais[0].upper(), 'city': ciudad.upper()} for pais, ciudad in [item[0] for item in countries]]
print(lista_diccionarios)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_concatenados = [' '.join(name[0]) for name in names]
print(nombres_concatenados)

slope_intercept = lambda m, b, x: m * x + b
print(slope_intercept(2, 3, 5))  