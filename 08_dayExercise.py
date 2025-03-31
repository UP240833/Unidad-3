
dog = {}


dog['nombre'] = 'Bella'
dog['color'] = 'Marrón'
dog['raza'] = 'Pomerania'
dog['patas'] = 4
dog['edad'] = 1

estudiante = {}
estudiante['primer_nombre'] = 'Aldo'
estudiante['apellido'] = 'Fernández'
estudiante['género'] = 'Masculino'
estudiante['edad'] = 18
estudiante['estado_civil'] = 'Soltero'
estudiante['habilidades'] = ['Python', 'Análisis de Datos']
estudiante['país'] = 'Mexico.'
estudiante['ciudad'] = 'Aguascalientes'
estudiante['dirección'] = '123 uruguay calle'

longitud_estudiante = len(estudiante)
print("Longitud del diccionario estudiante:", longitud_estudiante)

habilidades = estudiante['habilidades']
print("Habilidades:", habilidades)
print("Tipo de dato de habilidades:", type(habilidades)) 

estudiante['habilidades'].append('Aprendizaje Automático')
estudiante['habilidades'].append('Comunicación')
print("Habilidades actualizadas:", estudiante['habilidades'])

claves_estudiante = list(estudiante.keys())
print("Claves del diccionario estudiante:", claves_estudiante)

valores_estudiante = list(estudiante.values())
print("Valores del diccionario estudiante:", valores_estudiante)

items_estudiante = list(estudiante.items())
print("Items del diccionario estudiante como lista de tuplas:", items_estudiante)


del estudiante['estado_civil']
print("Diccionario estudiante después de eliminar estado_civil:", estudiante)

del estudiante
print("Diccionario estudiante eliminado.")