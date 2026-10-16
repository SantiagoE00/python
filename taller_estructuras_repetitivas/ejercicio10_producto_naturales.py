# ==========================================================================
# EJERCICIO 10
# Escribir un programa que multiplique los 20 primeros numeros naturales.
# Ejemplo: (1*2*3*4*5...).
# ==========================================================================

print("=== PRODUCTO DE LOS 20 PRIMEROS NUMEROS NATURALES ===")

# Hasta que numero se va a multiplicar
limite = 20

# El producto empieza en 1 (no en 0), porque cualquier numero por 0 da 0
producto = 1

# El ciclo for va de 1 a 20 y en cada vuelta multiplica el producto
# por el numero actual
for numero in range(1, limite + 1):
    producto *= numero
    print(f"Hasta {numero}: {producto}")

print(f"El producto de los {limite} primeros numeros naturales es: {producto}")
