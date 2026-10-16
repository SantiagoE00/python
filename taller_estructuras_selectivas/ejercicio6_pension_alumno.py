# ==========================================================================
# EJERCICIO 6
# Se ha establecido un programa para estimular a los alumnos, el cual consiste
# en lo siguiente: si el promedio obtenido por un alumno en el ultimo periodo
# es mayor o igual que 4.0, se le hara un descuento del 30% sobre la pension;
# si el promedio obtenido es menor que 4.0 debera pagar la pension completa,
# la cual incluye el 10% de IVA. Obtener cuanto debe pagar un alumno.
# ==========================================================================

print("=== PAGO DE PENSION ===")
pension = float(input("Ingrese el valor de la pension: "))
promedio = float(input("Ingrese el promedio del ultimo periodo: "))

if promedio >= 4.0:
    descuento = pension * 0.30
    totalPagar = pension - descuento
    print(f"Descuento del 30%: ${descuento:,.2f}")
else:
    iva = pension * 0.10
    totalPagar = pension + iva
    print(f"IVA del 10%: ${iva:,.2f}")

print(f"El alumno debe pagar: ${totalPagar:,.2f}")
