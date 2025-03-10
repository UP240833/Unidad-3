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


radius = float(input("Introduce el radio del círculo: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius

print(f"Área del círculo: {area}")
print(f"Circunferencia del círculo: {circumference}")


m = 2  
b = -2 
x_intercept = -b / m  

print(f"Pendiente (m): {m}")
print(f"Intersección en x: {x_intercept}")
print(f"Intersección en y: {b}")


x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)
euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Pendiente entre los puntos (2, 2) y (6, 10): {slope}")
print(f"Distancia euclidiana entre los puntos (2, 2) y (6, 10): {euclidean_distance}")


print(f"La pendiente de la ecuación y = 2x - 2 es {m} y la pendiente entre los puntos es {slope}.")


x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3]
for x in x_values:
    y = x**2 + 6*x + 9
    print(f"Para x = {x}, y = {y}")


length_python = len('python')
length_dragon = len('dragon')
print(f"Longitud de 'python': {length_python}, Longitud de 'dragon': {length_dragon}")
print(f"¿La longitud de 'python' es igual a la de 'dragon'? {length_python == length_dragon}")


print(f"'on' está en 'python' y 'dragon'? {'on' in 'python' and 'on' in 'dragon'}")


sentence = "I hope this course is not full of jargon."
print(f"'jargon' está en la frase? {'jargon' in sentence}")

print(f"No hay 'on' en ambas palabras? {'on' not in 'dragon' and 'on' not in 'python'}")


length_python_float = float(length_python)
length_python_str = str(length_python_float)
print(f"Longitud de 'python' como float: {length_python_float}, como string: {length_python_str}")

def is_even(num):
    return num % 2 == 0

number_to_check = 4 
print(f"¿{number_to_check} es par? {is_even(number_to_check)}")


print(f"¿La división entera de 7 por 3 es igual a int(2.7)? {7 // 3 == int(2.7)}")

print(f"¿El tipo de '10' es igual al tipo de 10? {type('10') == type(10)}")