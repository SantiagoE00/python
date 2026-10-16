# ==========================================================================
# EJERCICIO 3
# Suponga que se tiene un conjunto de calificaciones de un grupo de 20
# alumnos. Realizar un algoritmo para calcular el promedio y la calificacion
# mas alta y mas baja de todo el grupo.
# ==========================================================================

print("=== CALIFICACIONES DEL GRUPO ===")

# Cantidad de alumnos del grupo
totalAlumnos = 20

# Acumulador para sumar todas las calificaciones
sumaCalificaciones = 0

# Variables para guardar la nota mas alta y la mas baja.
# Empiezan en None (vacias) porque todavia no hemos leido ninguna nota.
notaMasAlta = None
notaMasBaja = None

# El ciclo for se repite una vez por cada alumno
for i in range(1, totalAlumnos + 1):
    calificacion = float(input(f"Ingrese la calificacion del alumno {i}: "))

    # Sumamos la calificacion al acumulador
    sumaCalificaciones += calificacion

    # Si es la primera nota, o si es mayor que la mas alta guardada,
    # esta pasa a ser la nueva nota mas alta
    if notaMasAlta is None or calificacion > notaMasAlta:
        notaMasAlta = calificacion

    # Lo mismo para la mas baja, pero preguntando si es menor
    if notaMasBaja is None or calificacion < notaMasBaja:
        notaMasBaja = calificacion

# El promedio es la suma de las notas dividida entre la cantidad de alumnos
promedio = sumaCalificaciones / totalAlumnos

print(f"Promedio del grupo: {promedio:.2f}")
print(f"Calificacion mas alta: {notaMasAlta}")
print(f"Calificacion mas baja: {notaMasBaja}")
