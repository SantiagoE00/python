# Ejercicio 7: Promocion de llantas "Todo Terreno".
# Menos de 5 llantas -> $300.000 cada una
# De 5 a 10 llantas  -> $250.000 cada una
# Mas de 10 llantas  -> $200.000 cada una

print("=== PROMOCION LLANTAS TODO TERRENO ===")
cantidad = int(input("Ingrese la cantidad de llantas: "))

if cantidad < 5:
    precio_llanta = 300000
elif cantidad <= 10:
    precio_llanta = 250000
else:
    precio_llanta = 200000

total = cantidad * precio_llanta

print(f"Precio por cada llanta: ${precio_llanta:,}")
print(f"Total a pagar por {cantidad} llantas: ${total:,}")
