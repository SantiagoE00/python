# Ejercicio 1: Determinar si un aprendiz aprueba o reprueba Algoritmia.
# Aprueba si el promedio de tres calificaciones es mayor o igual a 70.

print("=== APROBACION DE ALGORITMIA ===")
nota1 = float(input("Ingrese la primera calificacion: "))
nota2 = float(input("Ingrese la segunda calificacion: "))
nota3 = float(input("Ingrese la tercera calificacion: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"Promedio: {promedio:.2f}")

if promedio >= 70:
    print("El aprendiz APRUEBA Algoritmia")
else:
    print("El aprendiz REPRUEBA Algoritmia")
