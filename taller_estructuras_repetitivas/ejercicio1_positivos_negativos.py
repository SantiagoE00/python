# ==========================================================================
# EJERCICIO 1
# Leer 20 numeros e imprimir cuantos son positivos, cuantos negativos y
# cuantos neutros.
# ==========================================================================

print("=== POSITIVOS, NEGATIVOS Y NEUTROS ===")

# Cantidad de numeros que se van a leer
totalNumeros = 20

# Contadores: empiezan en 0 y van sumando 1 cada vez que se encuentra un caso
cantidadPositivos = 0
cantidadNegativos = 0
cantidadNeutros = 0

# El ciclo for se repite 20 veces. range(1, totalNumeros + 1) va de 1 a 20,
# asi podemos mostrar "Numero 1", "Numero 2", etc.
for i in range(1, totalNumeros + 1):
    numero = float(input(f"Ingrese el numero {i}: "))

    # Revisamos de que tipo es el numero y sumamos 1 al contador que toca
    if numero > 0:
        cantidadPositivos += 1
    elif numero < 0:
        cantidadNegativos += 1
    else:
        # Si no es mayor ni menor que 0, entonces es 0 (neutro)
        cantidadNeutros += 1

# Cuando el ciclo termina, mostramos los resultados
print(f"Cantidad de positivos: {cantidadPositivos}")
print(f"Cantidad de negativos: {cantidadNegativos}")
print(f"Cantidad de neutros: {cantidadNeutros}")
