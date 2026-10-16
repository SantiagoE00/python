# ==========================================================================
# EJERCICIO 3
# Suponga que se tiene un conjunto de calificaciones de un grupo de 20
# alumnos. Realizar un algoritmo para calcular el promedio y la calificacion
# mas alta y mas baja de todo el grupo.
# (Con menu de opciones)
# ==========================================================================

# Cantidad de alumnos del grupo
totalAlumnos = 20

# Esta variable dice si ya se ingresaron las calificaciones.
# Empieza en False (falso) porque al inicio no hay datos.
datosIngresados = False

# Guardamos la opcion que elige el usuario. Empieza vacia.
opcion = ""

# El menu se repite MIENTRAS el usuario no elija la opcion 4 (Salir)
while opcion != "4":
    print("\n=== MENU - CALIFICACIONES DEL GRUPO ===")
    print("1. Ingresar las calificaciones de los 20 alumnos")
    print("2. Ver el promedio del grupo")
    print("3. Ver la calificacion mas alta y la mas baja")
    print("4. Salir")
    opcion = input("Elija una opcion: ").strip()

    if opcion == "1":
        # Cada vez que se elige esta opcion se empieza de cero
        sumaCalificaciones = 0
        notaMasAlta = None
        notaMasBaja = None

        # El ciclo for se repite una vez por cada alumno
        for i in range(1, totalAlumnos + 1):
            calificacion = float(input(f"Calificacion del alumno {i}: "))

            # Sumamos la calificacion al acumulador
            sumaCalificaciones += calificacion

            # Si es la primera nota o es mayor que la mas alta, se guarda
            if notaMasAlta is None or calificacion > notaMasAlta:
                notaMasAlta = calificacion

            # Si es la primera nota o es menor que la mas baja, se guarda
            if notaMasBaja is None or calificacion < notaMasBaja:
                notaMasBaja = calificacion

        # Calculamos el promedio y marcamos que ya hay datos
        promedio = sumaCalificaciones / totalAlumnos
        datosIngresados = True
        print("Calificaciones registradas correctamente.")

    elif opcion == "2":
        # Solo se puede mostrar si antes se ingresaron los datos
        if datosIngresados:
            print(f"Promedio del grupo: {promedio:.2f}")
        else:
            print("Primero debe ingresar las calificaciones (opcion 1).")

    elif opcion == "3":
        if datosIngresados:
            print(f"Calificacion mas alta: {notaMasAlta}")
            print(f"Calificacion mas baja: {notaMasBaja}")
        else:
            print("Primero debe ingresar las calificaciones (opcion 1).")

    elif opcion == "4":
        print("Programa finalizado.")

    else:
        # Si escribe algo que no es 1, 2, 3 o 4
        print("Opcion no valida. Intente de nuevo.")
