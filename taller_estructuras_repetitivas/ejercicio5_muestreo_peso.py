# ==========================================================================
# EJERCICIO 5
# Una persona debe realizar un muestreo con 50 personas para determinar el
# promedio de peso de los ninos, jovenes, adultos y ancianos que existen en
# su zona. Las categorias se determinan de acuerdo a la siguiente tabla:
#
#   CATEGORIA     EDAD
#   Ninos         0 - 12
#   Jovenes       13 - 29
#   Adultos       30 - 59
#   Ancianos      60 en adelante
# ==========================================================================

print("=== MUESTREO DE PESO POR CATEGORIA ===")

# Cantidad de personas del muestreo
totalPersonas = 50

# Para cada categoria necesitamos dos cosas:
# - un acumulador para sumar los pesos
# - un contador para saber cuantas personas hay
sumaPesoNinos = 0
cantidadNinos = 0
sumaPesoJovenes = 0
cantidadJovenes = 0
sumaPesoAdultos = 0
cantidadAdultos = 0
sumaPesoAncianos = 0
cantidadAncianos = 0

# El ciclo for se repite una vez por cada persona
for i in range(1, totalPersonas + 1):
    print(f"--- Persona {i} ---")
    edad = int(input("Ingrese la edad: "))
    peso = float(input("Ingrese el peso (kg): "))

    # Segun la edad, sumamos el peso y contamos la persona en su categoria
    if edad <= 12:
        sumaPesoNinos += peso
        cantidadNinos += 1
    elif edad <= 29:
        sumaPesoJovenes += peso
        cantidadJovenes += 1
    elif edad <= 59:
        sumaPesoAdultos += peso
        cantidadAdultos += 1
    else:
        sumaPesoAncianos += peso
        cantidadAncianos += 1

# Calculamos cada promedio. Si en una categoria no hubo nadie, el promedio
# queda en 0, porque no se puede dividir entre 0.
if cantidadNinos > 0:
    promedioNinos = sumaPesoNinos / cantidadNinos
else:
    promedioNinos = 0

if cantidadJovenes > 0:
    promedioJovenes = sumaPesoJovenes / cantidadJovenes
else:
    promedioJovenes = 0

if cantidadAdultos > 0:
    promedioAdultos = sumaPesoAdultos / cantidadAdultos
else:
    promedioAdultos = 0

if cantidadAncianos > 0:
    promedioAncianos = sumaPesoAncianos / cantidadAncianos
else:
    promedioAncianos = 0

# Mostramos los resultados
print(f"Promedio de peso de ninos ({cantidadNinos}): {promedioNinos:.2f} kg")
print(f"Promedio de peso de jovenes ({cantidadJovenes}): {promedioJovenes:.2f} kg")
print(f"Promedio de peso de adultos ({cantidadAdultos}): {promedioAdultos:.2f} kg")
print(f"Promedio de peso de ancianos ({cantidadAncianos}): {promedioAncianos:.2f} kg")
