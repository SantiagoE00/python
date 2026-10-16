# ==========================================================================
# EJERCICIO 3
# Una empresa quiere hacer una compra de varias piezas de la misma clase a una
# fabrica de bolsos. La empresa, dependiendo del monto total de la compra,
# decidira que hacer para pagar al fabricante:
#  - Si el monto total de la compra excede de $500.000 la empresa tendra la
#    capacidad de invertir de su propio dinero un 55% del monto de la compra,
#    pedir prestado al banco un 30% y el resto lo pagara solicitando un
#    credito al fabricante.
#  - Si el monto total de la compra no excede de $500.000 la empresa tendra
#    capacidad de invertir de su propio dinero un 70% y el restante 30% lo
#    pagara solicitando credito al fabricante.
# El fabricante cobra por concepto de intereses un 20% sobre la cantidad que
# se le pague a credito.
# Imprimir el valor invertido de su propio dinero, el valor prestado al banco
# y el valor del credito solicitado al fabricante, segun sea el caso.
#
# Nota: el 20% de intereses se aplica en los dos casos, porque en ambos se
# paga una parte a credito al fabricante.
# ==========================================================================

print("=== COMPRA A LA FABRICA DE BOLSOS ===")
cantidad = int(input("Ingrese la cantidad de bolsos: "))
precio = float(input("Ingrese el precio de cada bolso: "))

montoTotal = cantidad * precio

if montoTotal > 500000:
    dineroPropio = montoTotal * 0.55
    prestamoBanco = montoTotal * 0.30
    creditoFabricante = montoTotal - dineroPropio - prestamoBanco
else:
    dineroPropio = montoTotal * 0.70
    prestamoBanco = 0
    creditoFabricante = montoTotal * 0.30

intereses = creditoFabricante * 0.20

print(f"Monto total de la compra: ${montoTotal:,.2f}")
print(f"Valor invertido de dinero propio: ${dineroPropio:,.2f}")
print(f"Valor prestado al banco: ${prestamoBanco:,.2f}")
print(f"Valor del credito al fabricante: ${creditoFabricante:,.2f}")
print(f"Intereses del fabricante (20%): ${intereses:,.2f}")
print(f"Total a pagar al fabricante por el credito: ${creditoFabricante + intereses:,.2f}")
