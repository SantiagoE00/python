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

Archivo: `parte_b_desempeno_aprendiz.py` (basado en el Ejercicio 1).

El programa original solo decía si el aprendiz **aprueba o reprueba** con una sola condición (`promedio >= 70`). Lo transformé para que **clasifique el desempeño** del aprendiz y le diga qué debe hacer, lo que requiere varias decisiones con `if`, `elif` y `else`.

### ¿Qué condiciones utilicé?

1. `nota < 0 or nota > 100` (para cada nota): valida que las calificaciones estén en el rango permitido. Si alguna está fuera, muestra un error.
2. `promedio >= 90`: desempeño **Excelente**, recibe certificado de honor.
3. `promedio >= 70`: **Aprobado**, continúa con la siguiente competencia.
4. `promedio >= 60`: **En riesgo**, debe presentar plan de mejoramiento.
5. `else` (menor que 60): **Reprobado**, debe repetir la competencia.

### ¿Por qué las organicé de esa manera?

- Primero va la **validación de datos**, porque no tiene sentido calcular un promedio con notas imposibles (por ejemplo 120 o -5).
- Luego los rangos van **del valor más alto al más bajo**. Así cada `elif` solo se revisa si las condiciones anteriores fueron falsas, y no hace falta escribir los dos límites del rango. Por ejemplo, al llegar a `elif promedio >= 70` ya se sabe que el promedio es menor que 90, entonces ese bloque cubre exactamente el rango de 70 a 89.99.
- Si se pusieran en otro orden (por ejemplo `promedio >= 60` primero), un aprendiz con 95 entraría en esa condición y nunca llegaría a "Excelente". Por eso el orden importa.
- El `else` final atrapa todo lo que no cumplió ninguna condición (menos de 60), así ningún caso queda sin respuesta.

### ¿Qué ocurre si cambia uno de los valores de entrada?

Cambia el promedio y, por lo tanto, la rama que se ejecuta. Ejemplos probados:

| Notas | Promedio | Resultado |
|-------|----------|-----------|
| 95, 90, 92 | 92.33 | Excelente |
| 95, 90, **60** | 81.67 | Aprobado (bajar una nota lo saca de "Excelente") |
| 65, 60, 62 | 62.33 | En riesgo |
| 50, 55, 60 | 55.00 | Reprobado |
| **120**, 60, 62 | — | Error: nota fuera de rango (no se calcula el promedio) |

Basta con que una sola nota cambie para que el promedio cruce un límite (90, 70 o 60) y el programa tome una decisión distinta. Y si se ingresa un valor inválido, el programa lo detecta antes de hacer cualquier cálculo.
