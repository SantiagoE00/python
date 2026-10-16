# ==========================================================================
# EJERCICIO 8
# Un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un
# algoritmo que lea por cada estudiante la calificacion obtenida. Al
# finalizar calcule e imprima:
#   - La cantidad de estudiantes que obtuvieron una calificacion menor a 50.
#   - La cantidad de estudiantes que obtuvieron una calificacion de 50 o mas
#     pero menor que 70.
#   - La cantidad de estudiantes que obtuvieron una calificacion de 70 o mas
#     pero menor que 80.
#   - La cantidad de estudiantes que obtuvieron una calificacion de 80 o mas.
# La calificacion obtenida en el examen de algoritmia debe ser entre 1 y 100.
# ==========================================================================

print("=== RESULTADOS DEL EXAMEN DE ALGORITMIA ===")

# Cantidad de estudiantes del grupo
totalEstudiantes = 23

# Un contador por cada rango de calificacion
cantidadMenor50 = 0
cantidadEntre50y70 = 0
cantidadEntre70y80 = 0
cantidadMayorIgual80 = 0

# El ciclo for se repite una vez por cada estudiante
for i in range(1, totalEstudiantes + 1):
    calificacion = float(input(f"Calificacion del estudiante {i} (1 a 100): "))

    # Mientras la nota no este entre 1 y 100, se vuelve a pedir
    while calificacion < 1 or calificacion > 100:
        print("La calificacion debe estar entre 1 y 100.")
        calificacion = float(input(f"Calificacion del estudiante {i} (1 a 100): "))

    # Revisamos en que rango esta la nota y sumamos 1 a ese contador
    if calificacion < 50:
        cantidadMenor50 += 1
    elif calificacion < 70:
        # Ya sabemos que no es menor a 50, entonces esta entre 50 y 69.99
        cantidadEntre50y70 += 1
    elif calificacion < 80:
        # Ya sabemos que es 70 o mas, entonces esta entre 70 y 79.99
        cantidadEntre70y80 += 1
    else:
        cantidadMayorIgual80 += 1

print(f"Estudiantes con nota menor a 50: {cantidadMenor50}")
print(f"Estudiantes con nota de 50 o mas pero menor que 70: {cantidadEntre50y70}")
print(f"Estudiantes con nota de 70 o mas pero menor que 80: {cantidadEntre70y80}")
print(f"Estudiantes con nota de 80 o mas: {cantidadMayorIgual80}")
