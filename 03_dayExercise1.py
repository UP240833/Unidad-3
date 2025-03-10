edad = 18
altura = 1.68
base=int (input('Enter base'))
height=int (input('Enter height'))
area=int (0.5*base*height)
print('The area of the triangle is: ', area)

side_a=int (input('Enter side a'))
side_b=int (input('Enter side b'))
side_c=int (input('Enter side c'))
perimeter =int (side_a + side_b + side_c) 
print('The perimeter of the triangle is: ', perimeter)

length=int (input('Enter length'))
width=int (input('Enter width'))
area= int (length * width)
print('The area of the triangle is: ', area)

perimeter=int (2*(length + width))
print('The perimeter of the triangule is:', perimeter)

pi= 3.1416
radio= int (input('Ingresa el radio'))
area =int (pi*radio*radio)
print('The area of the circunference is:', area)
circunference= (2*pi*radio)
print('The circunference of the circle is', circunference)

slope = 2 
y_intercept = -2 
x_intercept = 1  

print("Pendiente:", slope)
print("Intersección en y:", y_intercept)
print("Intersección en x:", x_intercept)
import math


x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Pendiente:", slope)
print("Distancia euclidiana:", distance)

print("Las pendientes son iguales:", slope == 2)

for x in range(-5, 3):  
    y = x**2 + 6*x + 9
    print(f"Para x = {x}, y = {y}")

x_when_y_zero = -3
print("x cuando y es 0:", x_when_y_zero)
len_python = len('python')
len_dragon = len('dragon')

print("Longitud de 'python':", len_python)
print("Longitud de 'dragon':", len_dragon)
print("¿Son iguales las longitudes?", len_python == len_dragon)

found_in_both = 'on' in 'python' and 'on' in 'dragon'
print("¿Está 'on' en ambas palabras?", found_in_both)

sentence = "I hope this course is not full of jargon."
contains_jargon = 'jargon' in sentence
print("¿Está 'jargon' en la oración?", contains_jargon)

length_python = len('python')
float_length = float(length_python)
str_length = str(float_length)

print("Longitud de 'python' como float:", float_length)
print("Longitud de 'python' como string:", str_length)

def is_even(num):
    return num % 2 == 0

print("¿Es 4 par?", is_even(4))
print("¿Es 5 par?", is_even(5))

floor_division_check = (7 // 3) == int(2.7)
print("¿Es la división entera de 7 entre 3 igual a int(2.7)?", floor_division_check)


type_check = type('10') == type(10)
print("¿El tipo de '10' es igual al tipo de 10?", type_check)


int_check = int(float('9.8')) == 10
print("¿int('9.8') es igual a 10?", int_check)

horas = float(input("Ingresa las horas: "))
tasa_por_hora = float(input("Ingresa la tasa por hora: "))
pago_semanal = horas * tasa_por_hora
print("Tu ganancia semanal es:", pago_semanal)

años_vividos = int(input("Ingresa el número de años que has vivido: "))

segundos_vividos = años_vividos * 365 * 24 * 60 * 60  

print("Has vivido", segundos_vividos, "segundos.")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
