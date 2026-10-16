# Taller: Estructuras Repetitivas en Python

Fundamentos de Algoritmia – SENA
Aprendiz: Santiago Evanz Cabezas Cortes

Todos los ejercicios están comentados y usan **camelCase** para las variables (por ejemplo `cantidadPositivos`, `sumaPesoNinos`).

Los ejercicios **3, 5, 6, 7, 8, 9 y 11** tienen **menú de opciones**: un ciclo `while` muestra el menú hasta que el usuario elige *Salir*. Si se intenta ver un resultado antes de ingresar los datos, el programa avisa que primero se debe usar la opción 1.

| # | Archivo | Problema | Ciclo usado |
|---|---------|----------|-------------|
| 1 | `ejercicio1_positivos_negativos.py` | Contar positivos, negativos y neutros de 20 números | `for` |
| 2 | `ejercicio2_negativos_a_positivos.py` | Convertir 10 negativos a positivos y sumarlos | `for` + `while` (validación) |
| 3 | `ejercicio3_calificaciones_grupo.py` | Promedio, nota más alta y más baja de 20 alumnos | `for` |
| 4 | `ejercicio4_tabla_multiplicar.py` | Tabla de multiplicar de un número | `for` |
| 5 | `ejercicio5_muestreo_peso.py` | Promedio de peso por categoría de edad (50 personas) | `for` |
| 6 | `ejercicio6_hombres_mujeres.py` | Cantidad de hombres y mujeres en un salón de n personas | `for` + `while` (validación) |
| 7 | `ejercicio7_calcomanias_ibague.py` | Autos por color de calcomanía según el último dígito de la placa | `for` + `while` (validación) |
| 8 | `ejercicio8_examen_algoritmia.py` | Estudiantes por rango de nota (23 estudiantes, notas de 1 a 100) | `for` + `while` (validación) |
| 9 | `ejercicio9_promedio_edades.py` | Promedio de edad de hombres, mujeres y del grupo | `for` + `while` (validación) |
| 10 | `ejercicio10_producto_naturales.py` | Multiplicar los 20 primeros números naturales | `for` |
| 11 | `ejercicio11_datos_alumnos.py` | Datos de alumnos hasta que la edad sea 0 | `while` |

Para ejecutar cualquiera: `python ejercicio1_positivos_negativos.py`

**¿Cuándo usé `for` y cuándo `while`?**
- `for`: cuando se sabe de antemano cuántas veces se repite (20 números, 23 estudiantes, n personas).
- `while`: cuando no se sabe cuántas veces se repite. Por ejemplo, el ejercicio 11 sigue hasta que la edad sea 0, y las validaciones vuelven a pedir el dato mientras sea incorrecto.

## Parte c – Ejercicio modificado

Archivo: `ejercicio_2_modificado.py`

**Ejercicio original (2):** Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números.

| Modificación pedida | Qué se hizo |
|---------------------|-------------|
| Cambiar un ciclo `for` por un `while` | `for i in range(1, 11)` se cambió por `while contadorNegativos < totalNumeros`, y el contador se aumenta a mano con `contadorNegativos += 1`. |
| Modificar la condición de finalización | Antes terminaba siempre después de 10 números. Ahora termina cuando se completan 10 negativos **o** cuando el usuario digita 0. |
| Incorporar `break` o `continue` | `break`: si se digita 0, el ciclo se detiene de inmediato. `continue`: si se digita un positivo, se ignora y se vuelve a pedir otro número sin sumar ni contar. |

**¿Qué cambió en el comportamiento del programa?**

- Antes el usuario estaba obligado a ingresar exactamente 10 números negativos. Ahora puede terminar antes digitando 0, y el programa muestra la suma solo de los números que alcanzó a ingresar.
- Antes, si se ingresaba un número positivo, un `while` interno lo volvía a pedir. Ahora `continue` salta al inicio del ciclo; como el contador no aumenta, ese número no cuenta.
- Al final se muestra también **cuántos** números negativos se leyeron, porque ya no siempre son 10.

| Entradas | Resultado |
|----------|-----------|
| -2, 5, -3, -5, 0 | El 5 se ignora (`continue`), el 0 termina (`break`). Se leyeron 3 negativos, suma = 10 |
| Diez veces -1 | Termina al completar los 10. Se leyeron 10 negativos, suma = 10 |
