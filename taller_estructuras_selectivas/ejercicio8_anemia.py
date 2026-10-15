# Ejercicio 8: Determinar si una persona tiene anemia segun su nivel de
# hemoglobina, su edad y su sexo. Si la hemoglobina es menor que el limite
# inferior del rango que le corresponde, el resultado es POSITIVO.
#
# EDAD                  NIVEL HEMOGLOBINA
# 0 - 1 mes             13   - 26   g%
# > 1 y <= 6 meses      10   - 18   g%
# > 6 y <= 12 meses     11   - 15   g%
# > 1 y <= 5 anios      11.5 - 15   g%
# > 5 y <= 10 anios     12.6 - 15.5 g%
# > 10 y <= 15 anios    13   - 15.5 g%
# mujeres > 15 anios    12   - 16   g%
# hombres > 15 anios    14   - 18   g%

print("=== DIAGNOSTICO DE ANEMIA ===")
edad = float(input("Ingrese la edad: "))
unidad = input("La edad esta en (1) meses o (2) anios? ").strip()
hemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))

# Se pasa la edad a meses para comparar todo en la misma unidad
if unidad == "2":
    edad_meses = edad * 12
else:
    edad_meses = edad

if edad_meses <= 1:
    minimo = 13
elif edad_meses <= 6:
    minimo = 10
elif edad_meses <= 12:
    minimo = 11
elif edad_meses <= 60:      # hasta 5 anios
    minimo = 11.5
elif edad_meses <= 120:     # hasta 10 anios
    minimo = 12.6
elif edad_meses <= 180:     # hasta 15 anios
    minimo = 13
else:
    sexo = input("Ingrese el sexo (F = femenino, M = masculino): ").strip().upper()
    if sexo == "F":
        minimo = 12
    else:
        minimo = 14

print(f"Nivel minimo de hemoglobina para su edad: {minimo} g%")

if hemoglobina < minimo:
    print("Resultado: POSITIVO (tiene anemia)")
else:
    print("Resultado: NEGATIVO (no tiene anemia)")
