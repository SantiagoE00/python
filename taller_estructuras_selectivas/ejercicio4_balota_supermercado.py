# Ejercicio 4: Descuento en el supermercado segun el color de la balota.
# Rojo -> 15%, verde -> 20%, otro color -> sin descuento.

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
