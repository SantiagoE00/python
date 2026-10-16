# ==========================================================================
# EJERCICIO 2
# Leer 10 numeros negativos y convertirlos a positivos e imprimir la suma
# de dichos numeros.
# ==========================================================================

print("=== CONVERTIR NEGATIVOS A POSITIVOS ===")

# Cantidad de numeros que se van a leer
totalNumeros = 10

# Acumulador: aqui se van sumando los numeros ya convertidos a positivos
sumaPositivos = 0

# El ciclo for se repite 10 veces
for i in range(1, totalNumeros + 1):
    numero = float(input(f"Ingrese el numero negativo {i}: "))

    # Mientras el numero NO sea negativo, se vuelve a pedir.
    # Asi nos aseguramos de que solo entren numeros negativos.
    while numero >= 0:
        print("El numero debe ser negativo. Intente de nuevo.")
        numero = float(input(f"Ingrese el numero negativo {i}: "))

    # Para convertir un negativo en positivo se multiplica por -1
    numeroPositivo = numero * -1
    print(f"  {numero} convertido a positivo es {numeroPositivo}")

    # Sumamos el numero positivo al acumulador
    sumaPositivos += numeroPositivo

# Al terminar el ciclo mostramos la suma total
print(f"La suma de los numeros convertidos a positivos es: {sumaPositivos}")
