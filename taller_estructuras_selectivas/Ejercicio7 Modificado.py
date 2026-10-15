# ==========================================================================
# PARTE B - EJERCICIO MODIFICADO (basado en el Ejercicio 7 de las llantas)
#
# EJERCICIO ORIGINAL (7):
#   El precio de cada llanta dependia de la CANTIDAD de llantas compradas:
#   menos de 5 -> $300.000, de 5 a 10 -> $250.000, mas de 10 -> $200.000.
#
# EJERCICIO NUEVO:
#   Un cine cobra la entrada segun la EDAD de la persona:
#     - Menores de 12 anios (ninos)        -> $8.000
#     - De 12 a 59 anios (adultos)         -> $15.000
#     - De 60 anios en adelante (mayores)  -> $10.000
#   El programa pide la edad y la cantidad de entradas, y muestra
#   el tipo de cliente, el precio de cada entrada y el total a pagar.
#
# Se usan if, elif y else para decidir el precio segun la edad.
# ==========================================================================


# --------------------------------------------------------------------------
# PARTE 1: PEDIR LOS DATOS AL USUARIO
# --------------------------------------------------------------------------

# Mostramos un titulo en pantalla para que el usuario sepa que programa es
print("=== VENTA DE ENTRADAS AL CINE ===")

# Pedimos la edad. input() siempre devuelve texto, por eso usamos int()
# para convertirlo en numero entero y poder compararlo despues.
edad = int(input("Ingrese la edad de la persona: "))

# Pedimos cuantas entradas va a comprar (tambien la convertimos a entero)
cantidad = int(input("Ingrese la cantidad de entradas: "))


# --------------------------------------------------------------------------
# PARTE 2: DECIDIR EL PRECIO SEGUN LA EDAD (if, elif, else)
# --------------------------------------------------------------------------
# Python revisa las condiciones de arriba hacia abajo y entra SOLO en la
# primera que sea verdadera. Las demas ya no las revisa.

if edad < 12:
    # Entra aqui si la edad es menor que 12 (por ejemplo 5, 8 o 11)
    tipo_cliente = "Nino"
    precio_entrada = 8000

elif edad < 60:
    # Entra aqui si la edad NO fue menor que 12, pero si es menor que 60.
    # O sea, cubre las edades de 12 a 59.
    tipo_cliente = "Adulto"
    precio_entrada = 15000

else:
    # Entra aqui si ninguna condicion anterior se cumplio.
    # O sea, la edad es 60 o mas.
    tipo_cliente = "Adulto mayor"
    precio_entrada = 10000


# --------------------------------------------------------------------------
# PARTE 3: CALCULAR EL TOTAL
# --------------------------------------------------------------------------

# El total es el precio de una entrada por la cantidad de entradas
total = precio_entrada * cantidad


# --------------------------------------------------------------------------
# PARTE 4: MOSTRAR LOS RESULTADOS
# --------------------------------------------------------------------------
# La f antes de las comillas permite meter variables dentro de {}.
# El :, dentro de las llaves pone separador de miles (15000 -> 15,000).

print(f"Tipo de cliente: {tipo_cliente}")
print(f"Precio de cada entrada: ${precio_entrada:,}")
print(f"Total a pagar por {cantidad} entradas: ${total:,}")


# ==========================================================================
# COMO MODIFICARLO (por si el instructor pide un cambio):
#
# - Cambiar un precio: cambia el numero en "precio_entrada = ..." de la
#   rama que quieras. Ej: ninos a $7.000 -> precio_entrada = 7000
#
# - Cambiar una edad limite: cambia el numero de la condicion.
#   Ej: que ninos sean menores de 10 -> if edad < 10:
#
# - Agregar otra categoria: agrega otro elif ANTES del else.
#   Ej: estudiantes de 12 a 17 anios a $10.000:
#
#       elif edad < 18:
#           tipo_cliente = "Estudiante"
#           precio_entrada = 10000
#
#   (debe ir despues del "if edad < 12" y antes del "elif edad < 60",
#    porque las condiciones se revisan en orden, de la edad menor a la mayor)
# ==========================================================================
