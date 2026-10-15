# Ejercicio 6: Pago de la pension de un alumno.
# Promedio >= 4.0 -> 30% de descuento sobre la pension.
# Promedio < 4.0  -> paga la pension completa mas el 10% de IVA.

print("=== PAGO DE PENSION ===")
pension = float(input("Ingrese el valor de la pension: "))
promedio = float(input("Ingrese el promedio del ultimo periodo: "))

if promedio >= 4.0:
    descuento = pension * 0.30
    total_pagar = pension - descuento
    print(f"Descuento del 30%: ${descuento:,.2f}")
else:
    iva = pension * 0.10
    total_pagar = pension + iva
    print(f"IVA del 10%: ${iva:,.2f}")

print(f"El alumno debe pagar: ${total_pagar:,.2f}")
