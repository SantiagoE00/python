# ==========================================================================
# EJERCICIO 2
# Calcular el total a pagar por la compra de zapatillas. Si se compran tres o
# mas zapatillas se aplica un descuento del 20% sobre el total de la compra y
# si son menos de tres zapatillas un descuento del 10%. Mostrar en pantalla el
# valor de la compra, el valor del descuento y el valor a pagar una vez
# aplicado el descuento.
# ==========================================================================

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
