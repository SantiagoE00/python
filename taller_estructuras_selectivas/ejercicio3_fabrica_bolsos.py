# Ejercicio 3: Forma de pago de una compra a una fabrica de bolsos.
# Si el monto excede $500.000: 55% dinero propio, 30% prestamo al banco,
#   el resto (15%) a credito con el fabricante.
# Si no excede $500.000: 70% dinero propio y 30% a credito con el fabricante.
# El fabricante cobra 20% de intereses sobre lo que se paga a credito.

print("=== COMPRA A LA FABRICA DE BOLSOS ===")
cantidad = int(input("Ingrese la cantidad de bolsos: "))
precio = float(input("Ingrese el precio de cada bolso: "))

monto_total = cantidad * precio

if monto_total > 500000:
    dinero_propio = monto_total * 0.55
    prestamo_banco = monto_total * 0.30
    credito_fabricante = monto_total - dinero_propio - prestamo_banco
else:
    dinero_propio = monto_total * 0.70
    prestamo_banco = 0
    credito_fabricante = monto_total * 0.30

intereses = credito_fabricante * 0.20

print(f"Monto total de la compra: ${monto_total:,.2f}")
print(f"Valor invertido de dinero propio: ${dinero_propio:,.2f}")
print(f"Valor prestado al banco: ${prestamo_banco:,.2f}")
print(f"Valor del credito al fabricante: ${credito_fabricante:,.2f}")
print(f"Intereses del fabricante (20%): ${intereses:,.2f}")
print(f"Total a pagar al fabricante por el credito: ${credito_fabricante + intereses:,.2f}")
