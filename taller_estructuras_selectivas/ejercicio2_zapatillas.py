# Ejercicio 2: Total a pagar por la compra de zapatillas.
# 3 o mas zapatillas -> 20% de descuento; menos de 3 -> 10% de descuento.

print("=== COMPRA DE ZAPATILLAS ===")
cantidad = int(input("Ingrese la cantidad de zapatillas: "))
precio = float(input("Ingrese el precio de cada zapatilla: "))

valor_compra = cantidad * precio

if cantidad >= 3:
    descuento = valor_compra * 0.20
else:
    descuento = valor_compra * 0.10

valor_pagar = valor_compra - descuento

print(f"Valor de la compra: ${valor_compra:,.2f}")
print(f"Valor del descuento: ${descuento:,.2f}")
print(f"Valor a pagar: ${valor_pagar:,.2f}")
