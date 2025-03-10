print('hello, World')
print (len('Hello, World'))
print(type('Hello, World'))
print (str(10))
print(int('10'))
print(float(10))
input('Aldo Santiago Fernandez Gomez: ')


first_name = 'Aldo Santiago'
last_name = 'Fernandez Gomez'
country = 'Mexico'
city = 'Aguascalientes'
age = 18
is_married = False 
Skills = ['Phython','work','sell everything']
personal_info = {
    'firstname':'Aldo Santiago',
    'lastname':'Fernandez Gomez',
    'country':'Mexico',
    'city':'Aguascalientes'
}
print('hello',',','world','!')


print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', Skills)
print('Person information: ', personal_info)


first_name, last_name, country, age, is_married = 'Aldo Santiago', 'Fernandez Gomez', 'Mexico', 18, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

first_name = input('what is your name')
age = input('how old are you? ')

print(first_name)
print(age)

num_one = 5
num_two = 4
first_name = "Aldo Santiago"
last_name = "Fernández gomez"
age = 18
country = "México"

print("Tipo de num_one:", type(num_one))
print("Tipo de num_two:", type(num_two))
print("Tipo de first_name:", type(first_name))
print("Tipo de last_name:", type(last_name))
print("Tipo de age:", type(age))
print("Tipo de country:", type(country))

length_first_name = len(first_name)
print("La longitud de mi primer nombre es:", length_first_name)


length_last_name = len(last_name)
print("La longitud de mi apellido es:", length_last_name)
print("¿La longitud del primer nombre es igual a la del apellido?", length_first_name == length_last_name)


total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Suma:", total)
print("Resta:", diff)
print("Producto:", product)
print("División:", division)
print("Resto:", remainder)
print("Exponente:", exp)
print("División entera:", floor_division)


radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)


user_radius = float(input("Ingresa el radio del círculo: "))
user_area_of_circle = 3.14 * user_radius ** 2
print("Área del círculo con radio ingresado:", user_area_of_circle)


first_name_input = input("Ingresa tu primer nombre: ")
last_name_input = input("Ingresa tu apellido: ")
country_input = input("Ingresa tu país: ")
age_input = input("Ingresa tu edad: ")

print("Tu nombre es:", first_name_input)
print("Tu apellido es:", last_name_input)
print("Tu país es:", country_input)
print("Tu edad es:", age_input)


import keyword
print("Palabras reservadas en Python:", keyword.kwlist)