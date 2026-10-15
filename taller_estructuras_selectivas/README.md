# Taller: Estructuras Selectivas en Python

Fundamentos de Algoritmia – SENA
Aprendiz: Santiago Evanz Cabezas Cortes

## Parte a – Ejercicios del taller

| # | Archivo | Problema |
|---|---------|----------|
| 1 | `ejercicio1_aprueba_algoritmia.py` | Aprueba o reprueba según promedio de 3 notas (≥ 70) |
| 2 | `ejercicio2_zapatillas.py` | Descuento del 20% (3 o más) o 10% (menos de 3) en zapatillas |
| 3 | `ejercicio3_fabrica_bolsos.py` | Forma de pago a la fábrica de bolsos según el monto (> $500.000) |
| 4 | `ejercicio4_balota_supermercado.py` | Descuento según el color de la balota (rojo 15%, verde 20%) |
| 5 | `ejercicio5_pulsaciones.py` | Pulsaciones cada 10 segundos según sexo y edad |
| 6 | `ejercicio6_pension_alumno.py` | Pensión con 30% de descuento o con 10% de IVA según el promedio |
| 7 | `ejercicio7_llantas.py` | Precio de llantas según la cantidad comprada |
| 8 | `ejercicio8_anemia.py` | Diagnóstico de anemia según hemoglobina, edad y sexo |

Para ejecutar cualquiera: `python ejercicio1_aprueba_algoritmia.py`

**Nota sobre el ejercicio 3:** se aplica el 20% de intereses del fabricante en los dos casos, porque en ambos la empresa le paga una parte a crédito.

## Parte b – Ejercicio modificado

Archivo: `parte_b_entrada_cine.py` (basado en el **Ejercicio 7** de las llantas).

En el ejercicio original, el precio de cada llanta dependía de la **cantidad** que se compraba. Lo transformé en otro problema: un cine que cobra la entrada según la **edad** de la persona.

| Edad | Tipo de cliente | Precio |
|------|-----------------|--------|
| Menor de 12 | Niño | $8.000 |
| De 12 a 59 | Adulto | $15.000 |
| 60 o más | Adulto mayor | $10.000 |

### ¿Qué condiciones utilicé?

- `if edad < 12`: si la persona es niño, la entrada vale $8.000.
- `elif edad < 60`: si es adulto (de 12 a 59 años), vale $15.000.
- `else`: si es adulto mayor (60 años o más), vale $10.000.

### ¿Por qué las organicé de esa manera?

Las ordené de la edad **menor a la mayor**. Python revisa las condiciones de arriba hacia abajo y entra solo en la primera que se cumpla. Por eso, cuando llega a `elif edad < 60` ya sabe que la edad **no** es menor que 12, y no hace falta escribir `edad >= 12 and edad < 60`.

El `else` del final atrapa todos los casos que no cumplieron las condiciones anteriores (60 años o más), así ninguna edad queda sin precio.

### ¿Qué ocurre si cambia uno de los valores de entrada?

| Edad | Entradas | Resultado |
|------|----------|-----------|
| 8 | 2 | Niño, $8.000 c/u, total $16.000 |
| 11 | 1 | Niño, $8.000 (11 todavía es menor que 12) |
| 12 | 1 | Adulto, $15.000 (con un año más cambia de categoría) |
| 59 | 1 | Adulto, $15.000 |
| 60 | 2 | Adulto mayor, $10.000 c/u, total $20.000 |

- Si cambia la **edad**, puede cambiar la rama que se ejecuta y, con ella, el tipo de cliente y el precio. El cambio ocurre justo en los límites: con 11 años se cobra como niño y con 12 como adulto.
- Si cambia la **cantidad**, el precio de cada entrada sigue igual y solo cambia el total.
