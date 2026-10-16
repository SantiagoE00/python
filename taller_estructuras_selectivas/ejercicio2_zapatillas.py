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

valorCompra = cantidad * precio

if cantidad >= 3:
    descuento = valorCompra * 0.20
else:
    descuento = valorCompra * 0.10

valorPagar = valorCompra - descuento

print(f"Valor de la compra: ${valorCompra:,.2f}")
print(f"Valor del descuento: ${descuento:,.2f}")
print(f"Valor a pagar: ${valorPagar:,.2f}")
