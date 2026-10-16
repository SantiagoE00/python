# ==========================================================================
# EJERCICIO 11
# Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final
# del programa se debera mostrar la cantidad de hombres, la cantidad de
# mujeres, la altura promedio, la cantidad de alumnos que tienen una altura
# mayor a 1.70 cm, la cantidad de alumnos que tiene una altura menor o igual
# a 1.50 cm. El programa debe finalizar cuando la edad sea igual a 0.
#
# Nota: las alturas se trabajan en metros (1.70 m y 1.50 m).
# (Con menu de opciones)
# ==========================================================================

# Indica si ya se registraron alumnos. Al inicio no hay datos.
datosIngresados = False

# Opcion que elige el usuario
opcion = ""

# El menu se repite MIENTRAS el usuario no elija la opcion 4 (Salir)
while opcion != "4":
    print("\n=== MENU - DATOS DE LOS ALUMNOS ===")
    print("1. Registrar alumnos (termina cuando la edad sea 0)")
    print("2. Ver la cantidad de hombres y mujeres")
    print("3. Ver la altura promedio y los alumnos por altura")
    print("4. Salir")
    opcion = input("Elija una opcion: ").strip()

    if opcion == "1":
        # Contadores y acumulador en cero
        cantidadHombres = 0
        cantidadMujeres = 0
        sumaAlturas = 0
        totalAlumnos = 0
        cantidadMayor170 = 0
        cantidadMenorIgual150 = 0

        # Pedimos la primera edad ANTES del ciclo, para saber si se entra
        edad = int(input("Ingrese la edad del alumno (0 para terminar): "))

        # El ciclo se repite MIENTRAS la edad sea diferente de 0
        while edad != 0:
            sexo = input("Ingrese el sexo (M = hombre, F = mujer): ").strip().upper()

            # Mientras el sexo no sea M ni F, se vuelve a pedir
            while sexo != "M" and sexo != "F":
                print("Dato no valido. Escriba M o F.")
                sexo = input("Ingrese el sexo (M = hombre, F = mujer): ").strip().upper()

            altura = float(input("Ingrese la altura en metros (ej: 1.65): "))

            # Contamos al alumno segun su sexo
            if sexo == "M":
                cantidadHombres += 1
            else:
                cantidadMujeres += 1

            # Sumamos la altura y contamos un alumno mas
            sumaAlturas += altura
            totalAlumnos += 1

            # Revisamos los dos rangos de altura que pide el ejercicio
            if altura > 1.70:
                cantidadMayor170 += 1
            elif altura <= 1.50:
                cantidadMenorIgual150 += 1

            # Pedimos la edad del siguiente alumno. Si es 0, el ciclo termina.
            print("---")
            edad = int(input("Ingrese la edad del alumno (0 para terminar): "))

        datosIngresados = True
        print(f"Se registraron {totalAlumnos} alumnos.")

    elif opcion == "2":
        if datosIngresados:
            print(f"Cantidad de hombres: {cantidadHombres}")
            print(f"Cantidad de mujeres: {cantidadMujeres}")
        else:
            print("Primero debe registrar los alumnos (opcion 1).")

    elif opcion == "3":
        if datosIngresados:
            # Si no se registro ningun alumno, el promedio queda en 0
            if totalAlumnos > 0:
                alturaPromedio = sumaAlturas / totalAlumnos
            else:
                alturaPromedio = 0
            print(f"Altura promedio: {alturaPromedio:.2f} m")
            print(f"Alumnos con altura mayor a 1.70 m: {cantidadMayor170}")
            print(f"Alumnos con altura menor o igual a 1.50 m: {cantidadMenorIgual150}")
        else:
            print("Primero debe registrar los alumnos (opcion 1).")

    elif opcion == "4":
        print("Programa finalizado.")

    else:
        print("Opcion no valida. Intente de nuevo.")
