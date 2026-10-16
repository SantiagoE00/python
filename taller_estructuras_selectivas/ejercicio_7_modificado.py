# ==========================================================================
# EJERCICIO 7 MODIFICADO
#
# EJERCICIO ORIGINAL:
#   En una llantera se ha establecido una promocion de las llantas marca
#   "Todo Terreno", dicha promocion consiste en lo siguiente:
#   Si se compran menos de cinco llantas el precio es de $300.000 cada una,
#   de $250.000 si se compran de cinco a 10 y de $200.000 si se compran
#   mas de 10. Obtener la cantidad de dinero que una persona tiene que
#   pagar por cada una de las llantas que compre.
#
# LO QUE SE LE AGREGO:
#   1. Validar la cantidad: si es 0 o negativa, muestra un error.
#   2. Forma de pago:
#        - Efectivo -> 5% de descuento adicional sobre el total.
#        - Tarjeta  -> sin descuento adicional.
#        - Otra     -> forma de pago no valida.
#   3. Se muestra el subtotal, el descuento y el total a pagar.
# ==========================================================================


# --------------------------------------------------------------------------
# PARTE 1: PEDIR LA CANTIDAD DE LLANTAS
# --------------------------------------------------------------------------

# Mostramos un titulo en pantalla
print("=== PROMOCION LLANTAS TODO TERRENO ===")

# Pedimos la cantidad. input() devuelve texto, por eso usamos int()
# para convertirlo en numero entero y poder compararlo.
cantidad = int(input("Ingrese la cantidad de llantas: "))


# --------------------------------------------------------------------------
# PARTE 2: VALIDAR LA CANTIDAD (NUEVO)
# --------------------------------------------------------------------------
# Si la cantidad es 0 o negativa no tiene sentido hacer la compra,
# entonces mostramos un error y no se calcula nada mas.

if cantidad <= 0:
    print("Error: la cantidad de llantas debe ser mayor que 0.")

else:
    # Todo lo que esta dentro de este else solo se ejecuta
    # si la cantidad es valida (mayor que 0).

    # ----------------------------------------------------------------------
    # PARTE 3: DECIDIR EL PRECIO DE CADA LLANTA (igual que el original)
    # ----------------------------------------------------------------------
    # Python revisa las condiciones de arriba hacia abajo y entra SOLO
    # en la primera que sea verdadera.

    if cantidad < 5:
        # Entra aqui si compra de 1 a 4 llantas
        precioLlanta = 300000

    elif cantidad <= 10:
        # Entra aqui si NO fue menor que 5, pero si es hasta 10.
        # O sea, compra de 5 a 10 llantas.
        precioLlanta = 250000

    else:
        # Entra aqui si ninguna condicion anterior se cumplio.
        # O sea, compra mas de 10 llantas.
        precioLlanta = 200000

    # Calculamos el subtotal: precio de una llanta por la cantidad
    subtotal = cantidad * precioLlanta

    # ----------------------------------------------------------------------
    # PARTE 4: PEDIR LA FORMA DE PAGO (NUEVO)
    # ----------------------------------------------------------------------
    # .strip() quita espacios de sobra y .lower() pasa todo a minusculas,
    # asi da igual si el usuario escribe "Efectivo", "EFECTIVO" o "efectivo".
    formaPago = input("Forma de pago (efectivo / tarjeta): ").strip().lower()

    # ----------------------------------------------------------------------
    # PARTE 5: DESCUENTO SEGUN LA FORMA DE PAGO (NUEVO)
    # ----------------------------------------------------------------------

    if formaPago == "efectivo":
        # Pagando en efectivo se descuenta el 5% del subtotal
        descuento = subtotal * 0.05

    elif formaPago == "tarjeta":
        # Pagando con tarjeta no hay descuento
        descuento = 0

    else:
        # Si escribe otra cosa, se avisa y no se aplica descuento
        print("Forma de pago no valida. No se aplica descuento.")
        descuento = 0

    # El total es el subtotal menos el descuento
    total = subtotal - descuento

    # ----------------------------------------------------------------------
    # PARTE 6: MOSTRAR LOS RESULTADOS
    # ----------------------------------------------------------------------
    # La f antes de las comillas permite meter variables dentro de {}.
    # El :, dentro de las llaves pone separador de miles (300000 -> 300,000).
    # El :.0f quita los decimales.

    print(f"Precio por cada llanta: ${precioLlanta:,}")
    print(f"Subtotal ({cantidad} llantas): ${subtotal:,}")
    print(f"Descuento por forma de pago: ${descuento:,.0f}")
    print(f"Total a pagar: ${total:,.0f}")
