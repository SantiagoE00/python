# ==========================================================================
# EJERCICIO 2 MODIFICADO
#
# EJERCICIO ORIGINAL:
#   Leer 10 numeros negativos y convertirlos a positivos e imprimir la suma
#   de dichos numeros.
#
# MODIFICACIONES REALIZADAS:
#   1. Se cambio el ciclo for por un ciclo while.
#   2. Se modifico la condicion de finalizacion: el programa termina cuando
#      se completan los 10 numeros negativos O cuando el usuario digita 0.
#   3. Se uso break: si el usuario digita 0, el ciclo se detiene de una vez.
#   4. Se uso continue: si el usuario digita un numero positivo, se ignora
#      y se pasa directamente a pedir el siguiente numero.
# ==========================================================================

print("=== CONVERTIR NEGATIVOS A POSITIVOS (MODIFICADO) ===")
print("(Digite 0 si desea terminar antes de completar los 10 numeros)")

# Cantidad maxima de numeros negativos que se van a leer
totalNumeros = 10

# Contador de numeros negativos validos que se han leido.
# Con while, el contador se maneja a mano (el for lo hacia solo).
contadorNegativos = 0

# Acumulador para la suma de los numeros convertidos a positivos
sumaPositivos = 0

# El ciclo se repite MIENTRAS no se hayan leido los 10 negativos
while contadorNegativos < totalNumeros:
    numero = float(input(f"Ingrese el numero negativo {contadorNegativos + 1}: "))

    # BREAK: si el usuario digita 0, el ciclo se termina de inmediato
    if numero == 0:
        print("Se digito 0. Se termina la lectura de numeros.")
        break

    # CONTINUE: si el numero es positivo, no se tiene en cuenta.
    # continue salta el resto del codigo y vuelve al inicio del while,
    # sin sumar nada y sin aumentar el contador.
    if numero > 0:
        print("Ese numero es positivo, no se tiene en cuenta. Intente de nuevo.")
        continue

    # Si llega aqui, el numero si es negativo.
    # Para convertirlo en positivo se multiplica por -1
    numeroPositivo = numero * -1
    print(f"  {numero} convertido a positivo es {numeroPositivo}")

    # Sumamos el numero positivo al acumulador
    sumaPositivos += numeroPositivo

    # Aumentamos el contador. Si no se aumentara, el while nunca terminaria.
    contadorNegativos += 1

# Al salir del ciclo (por completar los 10 o por el break) se muestra el resultado
print(f"Cantidad de numeros negativos leidos: {contadorNegativos}")
print(f"La suma de los numeros convertidos a positivos es: {sumaPositivos}")
