# 1. Iterar de 0 a 10 usando un bucle for
print("Iterar de 0 a 10 usando for:")
for i in range(11): 
    print(i)

# Iterar de 0 a 10 usando un bucle while
print("\nIterar de 0 a 10 usando while:")
i = 0  
while i <= 10:  
    print(i)
    i += 1  

# 2. Iterar de 10 a 0 usando un bucle for
print("\nIterar de 10 a 0 usando for:")
for i in range(10, -1, -1): 
    print(i)

# Iterar de 10 a 0 usando un bucle while
print("\nIterar de 10 a 0 usando while:")
i = 10 
while i >= 0:  
    print(i)
    i -= 1  

# 3. Imprimir un patrón de triángulo
print("\nImprimir un triángulo:")
for i in range(1, 8): 
    print('#' * i)  

# 4. Crear una cuadrícula usando bucles anidados
print("\nCrear una cuadrícula:")
for i in range(8): 
    for j in range(7):  
        print('#', end=' ') 
    print()  
# 5. Imprimir los cuadrados de los números del 0 al 10
print("\nImprimir cuadrados:")
for i in range(11): 
    print(i, "x", i, "=", i * i) 

# 6. Iterar a través de una lista e imprimir los elementos
fruits = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] 
print("\nIterar a través de la lista de frutas:")
for fruit in fruits: 
    print(fruit)  

# 7. Imprimir solo los números pares del 0 al 100
print("\nImprimir números pares del 0 al 100:")
for i in range(101): 
    if i % 2 == 0:  
        print(i)  

# 8. Imprimir solo los números impares del 0 al 100
print("\nImprimir números impares del 0 al 100:")
for i in range(101): 
    if i % 2 != 0:  
        print(i) 
    
# Sumar todos los números del 0 al 100
total_sum = 0
for i in range(101):
    total_sum += i

print("The sum of all numbers is", total_sum)

# Sumar todos los números pares e impares del 0 al 100
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print("The sum of all evens is", sum_evens, "And the sum of all odds is", sum_odds)


countries = ['Finland', 'Ireland', 'Switzerland', 'Iceland', 'New Zealand', 'Thailand', 'Land']

land_countries = []
for country in countries:
    if 'land' in country:
        land_countries.append(country)

print("Países que contienen 'land':", land_countries)

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for fruit in fruits:
    reversed_fruits.insert(0, fruit)

print("Frutas en orden inverso:", reversed_fruits)


countries_data = {
    'countries': [
        {'name': 'China', 'languages': ['Mandarin'], 'population': 1400},
        {'name': 'India', 'languages': ['Hindi', 'English'], 'population': 1380},
        {'name': 'USA', 'languages': ['English'], 'population': 331},
        {'name': 'Indonesia', 'languages': ['Indonesian'], 'population': 273},
        {'name': 'Pakistan', 'languages': ['Urdu', 'English'], 'population': 225},
        {'name': 'Brazil', 'languages': ['Portuguese'], 'population': 213},
        {'name': 'Nigeria', 'languages': ['English', 'Hausa'], 'population': 206},
        {'name': 'Bangladesh', 'languages': ['Bengali'], 'population': 166},
        {'name': 'Russia', 'languages': ['Russian'], 'population': 146},
        {'name': 'Mexico', 'languages': ['Spanish'], 'population': 126},
    ]
}

total_languages = set()
for country in countries_data['countries']:
    for language in country['languages']:
        total_languages.add(language)

print("El total de lenguajes es:", len(total_languages))

language_count = {}
for country in countries_data['countries']:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]

print("Los 10 lenguajes más hablados son:")
for language, count in most_spoken_languages:
    print(f"{language}: {count} países")

most_populated_countries = sorted(countries_data['countries'], key=lambda x: x['population'], reverse=True)[:10]

print("Los 10 países más poblados son:")
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']} millones")