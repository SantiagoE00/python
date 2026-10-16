# ==========================================================================
# EJERCICIO 5
# Una persona debe realizar un muestreo con 50 personas para determinar el
# promedio de peso de los ninos, jovenes, adultos y ancianos que existen en
# su zona. Las categorias se determinan de acuerdo a la siguiente tabla:
#
#   CATEGORIA     EDAD
#   Ninos         0 - 12
#   Jovenes       13 - 29
#   Adultos       30 - 59
#   Ancianos      60 en adelante
# (Con menu de opciones)
# ==========================================================================

# Cantidad de personas del muestreo
totalPersonas = 50

# Indica si ya se hizo el muestreo. Al inicio no hay datos.
datosIngresados = False

# Opcion que elige el usuario
opcion = ""

# El menu se repite MIENTRAS el usuario no elija la opcion 4 (Salir)
while opcion != "4":
    print("\n=== MENU - MUESTREO DE PESO ===")
    print("1. Registrar las 50 personas del muestreo")
    print("2. Ver el promedio de peso por categoria")
    print("3. Ver cuantas personas hay en cada categoria")
    print("4. Salir")
    opcion = input("Elija una opcion: ").strip()

    if opcion == "1":
        # Se empieza de cero: un acumulador y un contador por categoria
        sumaPesoNinos = 0
        cantidadNinos = 0
        sumaPesoJovenes = 0
        cantidadJovenes = 0
        sumaPesoAdultos = 0
        cantidadAdultos = 0
        sumaPesoAncianos = 0
        cantidadAncianos = 0

        # El ciclo for se repite una vez por cada persona
        for i in range(1, totalPersonas + 1):
            print(f"--- Persona {i} ---")
            edad = int(input("Ingrese la edad: "))
            peso = float(input("Ingrese el peso (kg): "))

            # Segun la edad, sumamos el peso y contamos la persona
            if edad <= 12:
                sumaPesoNinos += peso
                cantidadNinos += 1
            elif edad <= 29:
                sumaPesoJovenes += peso
                cantidadJovenes += 1
            elif edad <= 59:
                sumaPesoAdultos += peso
                cantidadAdultos += 1
            else:
                sumaPesoAncianos += peso
                cantidadAncianos += 1

        datosIngresados = True
        print("Muestreo registrado correctamente.")

    elif opcion == "2":
        if datosIngresados:
            # Si en una categoria no hubo nadie, el promedio queda en 0
            # para no dividir entre 0
            if cantidadNinos > 0:
                promedioNinos = sumaPesoNinos / cantidadNinos
            else:
                promedioNinos = 0

            if cantidadJovenes > 0:
                promedioJovenes = sumaPesoJovenes / cantidadJovenes
            else:
                promedioJovenes = 0

            if cantidadAdultos > 0:
                promedioAdultos = sumaPesoAdultos / cantidadAdultos
            else:
                promedioAdultos = 0

            if cantidadAncianos > 0:
                promedioAncianos = sumaPesoAncianos / cantidadAncianos
            else:
                promedioAncianos = 0

            print(f"Promedio de peso de ninos: {promedioNinos:.2f} kg")
            print(f"Promedio de peso de jovenes: {promedioJovenes:.2f} kg")
            print(f"Promedio de peso de adultos: {promedioAdultos:.2f} kg")
            print(f"Promedio de peso de ancianos: {promedioAncianos:.2f} kg")
        else:
            print("Primero debe registrar el muestreo (opcion 1).")

    elif opcion == "3":
        if datosIngresados:
            print(f"Ninos: {cantidadNinos}")
            print(f"Jovenes: {cantidadJovenes}")
            print(f"Adultos: {cantidadAdultos}")
            print(f"Ancianos: {cantidadAncianos}")
        else:
            print("Primero debe registrar el muestreo (opcion 1).")

    elif opcion == "4":
        print("Programa finalizado.")

    else:
        print("Opcion no valida. Intente de nuevo.")
