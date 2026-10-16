# ==========================================================================
# EJERCICIO 9
# Calcular el promedio de edades de hombres, mujeres y de todo un grupo de
# alumnos.
# (Con menu de opciones)
# ==========================================================================

# Indica si ya se registraron los alumnos. Al inicio no hay datos.
datosIngresados = False

# Opcion que elige el usuario
opcion = ""

# El menu se repite MIENTRAS el usuario no elija la opcion 4 (Salir)
while opcion != "4":
    print("\n=== MENU - PROMEDIO DE EDADES ===")
    print("1. Registrar los alumnos del grupo")
    print("2. Ver el promedio de edad de hombres y de mujeres")
    print("3. Ver el promedio de edad de todo el grupo")
    print("4. Salir")
    opcion = input("Elija una opcion: ").strip()

    if opcion == "1":
        # Cantidad de alumnos del grupo; la digita el usuario
        totalAlumnos = int(input("Ingrese la cantidad de alumnos: "))

        # Acumuladores y contadores en cero
        sumaEdadHombres = 0
        cantidadHombres = 0
        sumaEdadMujeres = 0
        cantidadMujeres = 0

        # El ciclo for se repite una vez por cada alumno
        for i in range(1, totalAlumnos + 1):
            print(f"--- Alumno {i} ---")
            edad = int(input("Ingrese la edad: "))
            sexo = input("Ingrese el sexo (M = hombre, F = mujer): ").strip().upper()

            # Mientras el sexo no sea M ni F, se vuelve a pedir
            while sexo != "M" and sexo != "F":
                print("Dato no valido. Escriba M o F.")
                sexo = input("Ingrese el sexo (M = hombre, F = mujer): ").strip().upper()

            # Sumamos la edad y contamos al alumno segun su sexo
            if sexo == "M":
                sumaEdadHombres += edad
                cantidadHombres += 1
            else:
                sumaEdadMujeres += edad
                cantidadMujeres += 1

        datosIngresados = True
        print("Alumnos registrados correctamente.")

    elif opcion == "2":
        if datosIngresados:
            # Si no hay hombres o mujeres, el promedio queda en 0
            if cantidadHombres > 0:
                promedioHombres = sumaEdadHombres / cantidadHombres
            else:
                promedioHombres = 0

            if cantidadMujeres > 0:
                promedioMujeres = sumaEdadMujeres / cantidadMujeres
            else:
                promedioMujeres = 0

            print(f"Promedio de edad de los hombres: {promedioHombres:.2f}")
            print(f"Promedio de edad de las mujeres: {promedioMujeres:.2f}")
        else:
            print("Primero debe registrar los alumnos (opcion 1).")

    elif opcion == "3":
        if datosIngresados:
            # Suma de todas las edades entre todos los alumnos
            if totalAlumnos > 0:
                promedioGrupo = (sumaEdadHombres + sumaEdadMujeres) / totalAlumnos
            else:
                promedioGrupo = 0
            print(f"Promedio de edad de todo el grupo: {promedioGrupo:.2f}")
        else:
            print("Primero debe registrar los alumnos (opcion 1).")

    elif opcion == "4":
        print("Programa finalizado.")

    else:
        print("Opcion no valida. Intente de nuevo.")
