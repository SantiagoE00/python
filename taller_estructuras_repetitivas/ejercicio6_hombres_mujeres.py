# ==========================================================================
# EJERCICIO 6
# Calcular la cantidad de hombres y mujeres presentes en un salon de clases
# con un total de n personas.
# (Con menu de opciones)
# ==========================================================================

# Indica si ya se registraron las personas. Al inicio no hay datos.
datosIngresados = False

# Opcion que elige el usuario
opcion = ""

# El menu se repite MIENTRAS el usuario no elija la opcion 3 (Salir)
while opcion != "3":
    print("\n=== MENU - HOMBRES Y MUJERES EN EL SALON ===")
    print("1. Registrar las personas del salon")
    print("2. Ver la cantidad de hombres y mujeres")
    print("3. Salir")
    opcion = input("Elija una opcion: ").strip()

    if opcion == "1":
        # n es la cantidad total de personas; la digita el usuario
        n = int(input("Ingrese la cantidad de personas del salon: "))

        # Contadores en cero cada vez que se registra un salon
        cantidadHombres = 0
        cantidadMujeres = 0

        # El ciclo for se repite n veces, una por cada persona
        for i in range(1, n + 1):
            sexo = input(f"Sexo de la persona {i} (M = hombre, F = mujer): ").strip().upper()

            # Mientras el sexo no sea M ni F, se vuelve a pedir
            while sexo != "M" and sexo != "F":
                print("Dato no valido. Escriba M o F.")
                sexo = input(f"Sexo de la persona {i} (M = hombre, F = mujer): ").strip().upper()

            # Sumamos 1 al contador que corresponde
            if sexo == "M":
                cantidadHombres += 1
            else:
                cantidadMujeres += 1

        datosIngresados = True
        print("Personas registradas correctamente.")

    elif opcion == "2":
        if datosIngresados:
            print(f"Total de personas: {n}")
            print(f"Cantidad de hombres: {cantidadHombres}")
            print(f"Cantidad de mujeres: {cantidadMujeres}")
        else:
            print("Primero debe registrar las personas (opcion 1).")

    elif opcion == "3":
        print("Programa finalizado.")

    else:
        print("Opcion no valida. Intente de nuevo.")
