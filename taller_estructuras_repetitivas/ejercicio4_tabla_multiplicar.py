# ==========================================================================
# EJERCICIO 4
# Calcular e imprimir la tabla de multiplicar de un numero cualquiera, el
# cual se digitara por teclado. Imprimir el multiplicando, el multiplicador
# y el producto.
# ==========================================================================

print("=== TABLA DE MULTIPLICAR ===")

# El multiplicando es el numero del que queremos la tabla
multiplicando = int(input("Ingrese el numero de la tabla: "))

# El multiplicador va cambiando de 1 a 10 dentro del ciclo for
for multiplicador in range(1, 11):
    # El producto es el resultado de la multiplicacion
    producto = multiplicando * multiplicador
    print(f"{multiplicando} x {multiplicador} = {producto}")
