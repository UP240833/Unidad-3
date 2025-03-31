#exercise 1 

edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario >= 18:
    print("Eres lo suficientemente mayor para aprender a conducir.")
else:
    años_necesarios = 18 - edad_usuario
    print(f"Necesitas {años_necesarios} años más para aprender a conducir.")


mi_edad = int(input("Ingresa mi edad: "))


if mi_edad > edad_usuario:
    diferencia = mi_edad - edad_usuario
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
elif mi_edad < edad_usuario:
    diferencia = edad_usuario - mi_edad
    if diferencia == 1:
        print("Tú eres 1 año mayor que yo.")
    else:
        print(f"Tú eres {diferencia} años mayor que yo.")
else:
    print("Tenemos la misma edad.")


a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))


if a > b:
    print(f"{a} es mayor que {b}.")
elif a < b:
    print(f"{a} es menor que {b}.")
else:
    print(f"{a} es igual a {b}.")

#exercise 2 

puntaje = int(input("Ingresa el puntaje del estudiante: "))

if 80 <= puntaje <= 100:
    print("Grado: A")
elif 70 <= puntaje <= 89:
    print("Grado: B")
elif 60 <= puntaje <= 69:
    print("Grado: C")
elif 50 <= puntaje <= 59:
    print("Grado: D")
elif 0 <= puntaje <= 49:
    print("Grado: F")
else:
    print("Puntaje no válido.")

mes = input("Ingresa un mes: ").strip().lower()

if mes in ['septiembre', 'octubre', 'noviembre']:
    print("La estación es Otoño.")
elif mes in ['diciembre', 'enero', 'febrero']:
    print("La estación es Invierno.")
elif mes in ['marzo', 'abril', 'mayo']:
    print("La estación es Primavera.")
elif mes in ['junio', 'julio', 'agosto']:
    print("La estación es Verano.")
else:
    print("Mes no válido.")


fruits = ['banana', 'orange', 'mango', 'lemon']
nueva_fruta = input("Ingresa una fruta: ").strip().lower()

if nueva_fruta in fruits:
    print("Esa fruta ya existe en la lista.")
else:
    fruits.append(nueva_fruta)
    print("Lista de frutas modificada:", fruits)

    
person = {
    'first_name': 'Aldo',
    'last_name': 'Fernández',
    'age': 18,
    'country': 'México',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'durando street',
        'zipcode': '28393'
    }
}


if 'skills' in person:
  
    skills = person['skills']
    middle_index = len(skills) // 2
    middle_skill = skills[middle_index]
    print("Middle skill:", middle_skill)

  
    has_python_skill = 'Python' in skills
    print("Has Python skill:", has_python_skill)

    
    if skills == ['JavaScript', 'React']:
        print('He is a front end developer.')
    elif skills == ['Node', 'Python', 'MongoDB']:
        print('He is a backend developer.')
    elif skills == ['React', 'Node', 'MongoDB']:
        print('He is a fullstack developer.')
    else:
        print('Unknown title.')


if person['is_married'] and person['country'] == 'México':
    print(f"{person['first_name']} {person['last_name']} is married and lives in {person['country']}.")