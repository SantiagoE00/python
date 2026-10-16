# ==========================================================================
# EJERCICIO 8
# Tomando como base los resultados obtenidos en un laboratorio de analisis
# clinicos, un medico determina si una persona tiene anemia o no, lo cual
# depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo.
# Si el nivel de hemoglobina que tiene una persona es menor que el rango que
# le corresponde, se determina su resultado como positivo y en caso contrario
# como negativo. La tabla en la que el medico se basa es la siguiente:
#
#   EDAD                  NIVEL HEMOGLOBINA
#   0 - 1 mes             13   - 26   g%
#   > 1 y <= 6 meses      10   - 18   g%
#   > 6 y <= 12 meses     11   - 15   g%
#   > 1 y <= 5 anios      11.5 - 15   g%
#   > 5 y <= 10 anios     12.6 - 15.5 g%
#   > 10 y <= 15 anios    13   - 15.5 g%
#   mujeres > 15 anios    12   - 16   g%
#   hombres > 15 anios    14   - 18   g%
#
# Nota: como la tabla mezcla meses y anios, el programa pregunta en que
# unidad esta la edad y la convierte toda a meses para comparar.
# ==========================================================================

print("=== DIAGNOSTICO DE ANEMIA ===")
edad = float(input("Ingrese la edad: "))
unidad = input("La edad esta en (1) meses o (2) anios? ").strip()
hemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))

# Se pasa la edad a meses para comparar todo en la misma unidad
if unidad == "2":
    edadMeses = edad * 12
else:
    edadMeses = edad

if edadMeses <= 1:
    minimo = 13
elif edadMeses <= 6:
    minimo = 10
elif edadMeses <= 12:
    minimo = 11
elif edadMeses <= 60:      # hasta 5 anios
    minimo = 11.5
elif edadMeses <= 120:     # hasta 10 anios
    minimo = 12.6
elif edadMeses <= 180:     # hasta 15 anios
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
