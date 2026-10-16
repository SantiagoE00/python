# ==========================================================================
# EJERCICIO 7
# En una llantera se ha establecido una promocion de las llantas marca
# "Todo Terreno", dicha promocion consiste en lo siguiente:
# Si se compran menos de cinco llantas el precio es de $300.000 cada una, de
# $250.000 si se compran de cinco a 10 y de $200.000 si se compran mas de 10.
# Obtener la cantidad de dinero que una persona tiene que pagar por cada una de
# las llantas que compre.
# ==========================================================================

print("=== PROMOCION LLANTAS TODO TERRENO ===")
cantidad = int(input("Ingrese la cantidad de llantas: "))

if cantidad < 5:
    precioLlanta = 300000
elif cantidad <= 10:
    precioLlanta = 250000
else:
    precioLlanta = 200000

total = cantidad * precioLlanta

print(f"Precio por cada llanta: ${precioLlanta:,}")
print(f"Total a pagar por {cantidad} llantas: ${total:,}")
