# PARTE B: Ejercicio modificado (basado en el Ejercicio 1).
#
# Original: el programa solo decia si el aprendiz APRUEBA o REPRUEBA
#           (una sola condicion: promedio >= 70).
#
# Nuevo problema: clasificar el desempeno del aprendiz segun su promedio
# y decir que debe hacer. Ahora se necesitan varias decisiones con if, elif y else:
#   - Notas fuera del rango 0 a 100 -> dato invalido
#   - Promedio >= 90                -> Excelente, recibe certificado de honor
#   - Promedio >= 70                -> Aprobado
#   - Promedio >= 60                -> Puede presentar plan de mejoramiento
#   - Promedio < 60                 -> Reprueba, debe repetir la competencia

print("=== CLASIFICACION DEL DESEMPENO DEL APRENDIZ ===")
nota1 = float(input("Ingrese la primera calificacion (0 a 100): "))
nota2 = float(input("Ingrese la segunda calificacion (0 a 100): "))
nota3 = float(input("Ingrese la tercera calificacion (0 a 100): "))

if nota1 < 0 or nota1 > 100 or nota2 < 0 or nota2 > 100 or nota3 < 0 or nota3 > 100:
    print("Error: todas las calificaciones deben estar entre 0 y 100.")
else:
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"Promedio: {promedio:.2f}")

    if promedio >= 90:
        print("Desempeno: EXCELENTE - Aprueba y recibe certificado de honor.")
    elif promedio >= 70:
        print("Desempeno: APROBADO - Puede continuar con la siguiente competencia.")
    elif promedio >= 60:
        print("Desempeno: EN RIESGO - Debe presentar un plan de mejoramiento.")
    else:
        print("Desempeno: REPROBADO - Debe repetir la competencia.")
