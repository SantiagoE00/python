# ==========================================================================
# EJERCICIO 9
# Calcular el promedio de edades de hombres, mujeres y de todo un grupo de
# alumnos.
# ==========================================================================

print("=== PROMEDIO DE EDADES DEL GRUPO ===")

# Cantidad de alumnos del grupo; la digita el usuario
totalAlumnos = int(input("Ingrese la cantidad de alumnos: "))

# Acumuladores de edades y contadores para hombres y mujeres
sumaEdadHombres = 0
cantidadHombres = 0
sumaEdadMujeres = 0
cantidadMujeres = 0

# El ciclo for se repite una vez por cada alumno
for i in range(1, totalAlumnos + 1):
    print(f"--- Alumno {i} ---")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (M = hombre, F = mujer): ").strip().upper()

    # Mientras el sexo no sea M ni F, se vuelve a pedir
    while sexo != "M" and sexo != "F":
        print("Dato no valido. Escriba M o F.")
        sexo = input("Ingrese el sexo (M = hombre, F = mujer): ").strip().upper()

    # Sumamos la edad y contamos al alumno segun su sexo
    if sexo == "M":
        sumaEdadHombres += edad
        cantidadHombres += 1
    else:
        sumaEdadMujeres += edad
        cantidadMujeres += 1

# Calculamos los promedios (si no hay nadie, el promedio queda en 0
# para no dividir entre 0)
if cantidadHombres > 0:
    promedioHombres = sumaEdadHombres / cantidadHombres
else:
    promedioHombres = 0

if cantidadMujeres > 0:
    promedioMujeres = sumaEdadMujeres / cantidadMujeres
else:
    promedioMujeres = 0

# El promedio del grupo usa la suma de todas las edades entre todos los alumnos
if totalAlumnos > 0:
    promedioGrupo = (sumaEdadHombres + sumaEdadMujeres) / totalAlumnos
else:
    promedioGrupo = 0

print(f"Promedio de edad de los hombres: {promedioHombres:.2f}")
print(f"Promedio de edad de las mujeres: {promedioMujeres:.2f}")
print(f"Promedio de edad de todo el grupo: {promedioGrupo:.2f}")
