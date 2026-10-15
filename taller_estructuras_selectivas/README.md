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

Archivo: `Ejercicio7 Modificado.py`

Tomé el **Ejercicio 7** (promoción de llantas "Todo Terreno") y lo dejé igual, pero le agregué funciones nuevas:

1. **Validación de la cantidad:** si se ingresan 0 llantas o un número negativo, el programa muestra un error.
2. **Forma de pago:** pagando en efectivo se aplica un 5% de descuento adicional; con tarjeta no hay descuento; si se escribe otra forma de pago, avisa que no es válida.
3. **Resultados más completos:** muestra el precio por llanta, el subtotal, el descuento y el total a pagar.

### ¿Qué condiciones utilicé?

| Condición | Para qué sirve |
|-----------|----------------|
| `if cantidad <= 0` | Detecta una cantidad inválida y muestra error (nuevo) |
| `if cantidad < 5` | Menos de 5 llantas: $300.000 cada una (original) |
| `elif cantidad <= 10` | De 5 a 10 llantas: $250.000 cada una (original) |
| `else` | Más de 10 llantas: $200.000 cada una (original) |
| `if forma_pago == "efectivo"` | 5% de descuento sobre el subtotal (nuevo) |
| `elif forma_pago == "tarjeta"` | Sin descuento (nuevo) |
| `else` | Forma de pago no válida, sin descuento (nuevo) |

### ¿Por qué las organicé de esa manera?

- **Primero va la validación**, porque si la cantidad no es válida no tiene sentido calcular precios. Todo el resto del programa queda dentro del `else`, así solo se ejecuta cuando la cantidad es correcta.
- **Los rangos de precio van de la cantidad menor a la mayor.** Python entra solo en la primera condición que se cumpla, por eso al llegar a `elif cantidad <= 10` ya se sabe que la cantidad no es menor que 5, y no hace falta escribir `cantidad >= 5 and cantidad <= 10`.
- **La forma de pago va después del precio**, porque el descuento se calcula sobre el subtotal, y el subtotal depende del precio de cada llanta.
- Cada grupo termina en un `else`, para que ningún caso quede sin respuesta.

### ¿Qué ocurre si cambia uno de los valores de entrada?

| Cantidad | Forma de pago | Precio c/u | Subtotal | Descuento | Total |
|----------|---------------|------------|----------|-----------|-------|
| 0 | — | — | — | — | Error: cantidad inválida |
| 4 | efectivo | $300.000 | $1.200.000 | $60.000 | $1.140.000 |
| 4 | tarjeta | $300.000 | $1.200.000 | $0 | $1.200.000 |
| 10 | efectivo | $250.000 | $2.500.000 | $125.000 | $2.375.000 |
| 11 | tarjeta | $200.000 | $2.200.000 | $0 | $2.200.000 |

- Si cambia la **cantidad**, puede cambiar el precio por llanta. Por ejemplo, con 10 llantas cada una cuesta $250.000, pero con 11 baja a $200.000, y el total queda incluso más barato.
- Si cambia la **forma de pago** con la misma cantidad, solo cambia el descuento. Por ejemplo, 4 llantas en efectivo cuestan $60.000 menos que con tarjeta.
- Si la cantidad es **0 o negativa**, el programa no calcula nada y muestra el error.
