# ==========================================================================
# EJERCICIO 7
# La oficina de transito de Ibague desea saber, de los n autos que entran a
# la ciudad de Ibague, cuantos entran con calcomania de cada color.
# Conociendo el ultimo digito de la placa de cada carro, se puede determinar
# el color de la calcomania utilizando la siguiente relacion:
#
#   DIGITO     COLOR
#   1 o 2      amarilla
#   3 o 4      rosa
#   5 o 6      roja
#   7 o 8      verde
#   9 o 0      azul
# ==========================================================================

print("=== CALCOMANIAS DE LOS AUTOS QUE ENTRAN A IBAGUE ===")

# n es la cantidad de autos; la digita el usuario
n = int(input("Ingrese la cantidad de autos: "))

# Un contador por cada color de calcomania
cantidadAmarilla = 0
cantidadRosa = 0
cantidadRoja = 0
cantidadVerde = 0
cantidadAzul = 0

# El ciclo for se repite una vez por cada auto
for i in range(1, n + 1):
    ultimoDigito = int(input(f"Ultimo digito de la placa del auto {i}: "))

    # Mientras el digito no este entre 0 y 9, se vuelve a pedir
    while ultimoDigito < 0 or ultimoDigito > 9:
        print("Debe ser un solo digito (0 a 9).")
        ultimoDigito = int(input(f"Ultimo digito de la placa del auto {i}: "))

    # Segun el digito, sumamos 1 al color que corresponde
    if ultimoDigito == 1 or ultimoDigito == 2:
        cantidadAmarilla += 1
    elif ultimoDigito == 3 or ultimoDigito == 4:
        cantidadRosa += 1
    elif ultimoDigito == 5 or ultimoDigito == 6:
        cantidadRoja += 1
    elif ultimoDigito == 7 or ultimoDigito == 8:
        cantidadVerde += 1
    else:
        # Los unicos que quedan son 9 y 0
        cantidadAzul += 1

print(f"Autos con calcomania amarilla: {cantidadAmarilla}")
print(f"Autos con calcomania rosa: {cantidadRosa}")
print(f"Autos con calcomania roja: {cantidadRoja}")
print(f"Autos con calcomania verde: {cantidadVerde}")
print(f"Autos con calcomania azul: {cantidadAzul}")
