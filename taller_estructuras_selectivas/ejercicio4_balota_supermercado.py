# ==========================================================================
# EJERCICIO 4
# En un supermercado se hace una promocion, mediante la cual el cliente obtiene
# un descuento dependiendo de un color que se escoge al azar. Si el color de la
# balota es rojo el descuento es del 15% sobre el total de la compra; si la
# balota es verde el descuento es del 20%. Si el color es diferente a los
# indicados no obtendra descuento. Imprimir el valor de la compra, el color de
# la balota, el descuento y el valor a pagar.
# ==========================================================================

print("=== PROMOCION DE LA BALOTA ===")
valor_compra = float(input("Ingrese el valor de la compra: "))
color = input("Ingrese el color de la balota: ").strip().lower()

if color == "rojo" or color == "roja":
    descuento = valor_compra * 0.15
elif color == "verde":
    descuento = valor_compra * 0.20
else:
    descuento = 0

valor_pagar = valor_compra - descuento

print(f"Valor de la compra: ${valor_compra:,.2f}")
print(f"Color de la balota: {color}")
print(f"Descuento: ${descuento:,.2f}")
print(f"Valor a pagar: ${valor_pagar:,.2f}")
