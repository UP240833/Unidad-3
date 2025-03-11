# 1.crea una tupla sola 
empty_tuple = ()

# 2. Crear una tupla de hermanos y hermanas
brothers = ('John', 'Mike')
sisters = ('Anna', 'Emma')

# 3. Unir las tuplas de hermanos y hermanas
siblings = brothers + sisters

# 4. Contar el número de hermanos
number_of_siblings = len(siblings)

# 5. Modificar la tupla de hermanos para agregar padres
father = 'Robert'
mother = 'Linda'
family_members = siblings + (father, mother)

# 1. Desempaquetar hermanos y padres de los miembros de la familia
siblings, father, mother = family_members[:-2], family_members[-2], family_members[-1]

# 2. Crear tuplas de frutas, verduras y productos animales
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'egg')

# 3. Unir las tuplas de alimentos
food_stuff_tp = fruits + vegetables + animal_products

# 4. Cambiar la tupla a una lista
food_stuff_lt = list(food_stuff_tp)

# 5. Sacar el elemento(s) del medio
middle_item = food_stuff_lt[len(food_stuff_lt) // 2]  # Para longitud impar

# 6. Sacar los primeros tres y los últimos tres elementos
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# 7. Eliminar la tupla completamente
del food_stuff_tp

# Comprobar si un elemento existe en la tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

is_estonia_nordic = 'Estonia' in nordic_countries
is_iceland_nordic = 'Iceland' in nordic_countries

# Resumen de resultados
print("Número de hermanos:", number_of_siblings)
print("¿Estonia es un país nórdico?", is_estonia_nordic)
print("¿Islandia es un país nórdico?", is_iceland_nordic)