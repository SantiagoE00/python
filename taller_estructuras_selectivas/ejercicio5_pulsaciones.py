# ==========================================================================
# EJERCICIO 5
# Calcular el numero de pulsaciones que debe tener una persona por cada 10
# segundos de ejercicio aerobico; la formula que se aplica es:
#  - cuando el sexo es femenino: num. pulsaciones = (220 - edad) / 10
#  - si el sexo es masculino:    num. pulsaciones = (210 - edad) / 10
# ==========================================================================

print("=== CALCULO DE PULSACIONES ===")
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (F = femenino, M = masculino): ").strip().upper()

if sexo == "F":
    pulsaciones = (220 - edad) / 10
    print(f"Numero de pulsaciones cada 10 segundos: {pulsaciones:.1f}")
elif sexo == "M":
    pulsaciones = (210 - edad) / 10
    print(f"Numero de pulsaciones cada 10 segundos: {pulsaciones:.1f}")
else:
    print("Sexo no valido. Debe ingresar F o M.")
