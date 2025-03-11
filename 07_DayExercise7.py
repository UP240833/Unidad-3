# 1. Crear un conjunto de empresas de IT
it_companies = {'Google', 'Facebook', 'Microsoft', 'Apple', 'IBM'}

# 2. Encontrar la longitud del conjunto
length_of_it_companies = len(it_companies)

# 3. Agregar 'Twitter' al conjunto
it_companies.add('Twitter')

# 4. Insertar múltiples empresas de IT
it_companies.update({'Amazon', 'Netflix', 'Adobe'})

# 5. Eliminar una empresa del conjunto
it_companies.remove('Facebook')

# 6. Diferencia entre remove y discard
# remove() lanza un error si el elemento no existe, discard() no.

# Ejercicios: Nivel 2
A = {1, 2, 3}
B = {3, 4, 5}

# 7. Unir A y B
joined_set = A.union(B)

# 8. Encontrar la intersección de A y B
intersection_set = A.intersection(B)

# 9. Verificar si A es un subconjunto de B
is_subset = A.issubset(B)

# 10. Verificar si A y B son conjuntos disjuntos
are_disjoint = A.isdisjoint(B)

# 11. Unir A con B y B con A
joined_ab = A.union(B)
joined_ba = B.union(A)

# 12. Diferencia simétrica entre A y B
symmetric_difference = A.symmetric_difference(B)

# 13. Eliminar los conjuntos completamente
del A
del B

# Ejercicios: Nivel 3
# 14. Convertir edades a un conjunto y comparar longitudes
ages = [22, 22, 25, 30, 30, 30, 35]
ages_set = set(ages)
length_of_list = len(ages)
length_of_set = len(ages_set)

# 15. Contar palabras únicas en una oración
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
number_of_unique_words = len(unique_words)

# Imprimir resultados
print("Longitud de it_companies:", length_of_it_companies)
print("Número de palabras únicas:", number_of_unique_words)