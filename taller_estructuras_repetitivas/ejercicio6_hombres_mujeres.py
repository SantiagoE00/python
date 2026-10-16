# ==========================================================================
# EJERCICIO 6
# Calcular la cantidad de hombres y mujeres presentes en un salon de clases
# con un total de n personas.
# ==========================================================================

print("=== HOMBRES Y MUJERES EN EL SALON ===")

# n es la cantidad total de personas; la digita el usuario
n = int(input("Ingrese la cantidad de personas del salon: "))

# Contadores para hombres y mujeres
cantidadHombres = 0
cantidadMujeres = 0

# El ciclo for se repite n veces, una por cada persona
for i in range(1, n + 1):
    # .strip() quita espacios y .upper() pasa a mayuscula (m -> M)
    sexo = input(f"Sexo de la persona {i} (M = hombre, F = mujer): ").strip().upper()

    # Mientras el sexo no sea M ni F, se vuelve a pedir
    while sexo != "M" and sexo != "F":
        print("Dato no valido. Escriba M o F.")
        sexo = input(f"Sexo de la persona {i} (M = hombre, F = mujer): ").strip().upper()

    # Sumamos 1 al contador que corresponde
    if sexo == "M":
        cantidadHombres += 1
    else:
        cantidadMujeres += 1

print(f"Cantidad de hombres: {cantidadHombres}")
print(f"Cantidad de mujeres: {cantidadMujeres}")
