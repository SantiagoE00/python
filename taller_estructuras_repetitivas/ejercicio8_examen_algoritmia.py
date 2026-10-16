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
# (Con menu de opciones)
# ==========================================================================

# Cantidad de estudiantes del grupo
totalEstudiantes = 23

# Indica si ya se ingresaron las notas. Al inicio no hay datos.
datosIngresados = False

# Opcion que elige el usuario
opcion = ""

# El menu se repite MIENTRAS el usuario no elija la opcion 3 (Salir)
while opcion != "3":
    print("\n=== MENU - EXAMEN DE ALGORITMIA ===")
    print("1. Ingresar las calificaciones de los 23 estudiantes")
    print("2. Ver la cantidad de estudiantes por rango de nota")
    print("3. Salir")
    opcion = input("Elija una opcion: ").strip()

    if opcion == "1":
        # Un contador por cada rango, en cero
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
                cantidadEntre50y70 += 1
            elif calificacion < 80:
                cantidadEntre70y80 += 1
            else:
                cantidadMayorIgual80 += 1

        datosIngresados = True
        print("Calificaciones registradas correctamente.")

    elif opcion == "2":
        if datosIngresados:
            print(f"Nota menor a 50: {cantidadMenor50}")
            print(f"Nota de 50 o mas pero menor que 70: {cantidadEntre50y70}")
            print(f"Nota de 70 o mas pero menor que 80: {cantidadEntre70y80}")
            print(f"Nota de 80 o mas: {cantidadMayorIgual80}")
        else:
            print("Primero debe ingresar las calificaciones (opcion 1).")

    elif opcion == "3":
        print("Programa finalizado.")

    else:
        print("Opcion no valida. Intente de nuevo.")
