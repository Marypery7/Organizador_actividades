# Organizador_actividades
Programa en Python, ejecutado por consola, que ayuda a una asociación a registrar actividades
(talleres, encuentros, sesiones de lectura, actividades deportivas), consultar cuáles tienen
plazas libres y controlar el número de personas inscritas.

Proyecto realizado para el **Reto 3**.

## Equipo

- [Nombre integrante 1]
- [Nombre integrante 2]
- [Nombre integrante 3]

## Funcionalidades

1. **Lista inicial de actividades:** el programa arranca con tres actividades ficticias.
   Cada una guarda su nombre, tipo, número máximo de participantes y número de inscritas.
2. **Mostrar actividades:** muestra todas las actividades con sus datos y las plazas disponibles
   (aforo máximo menos personas inscritas).
3. **Añadir una actividad:** pide nombre, tipo y aforo máximo. Las inscritas empiezan en 0.
4. **Inscribir participantes:** permite inscribir a una persona en una actividad elegida.
   Antes de confirmar, comprueba que quedan plazas. Si está completa, muestra un mensaje
   y no permite la inscripción.
5. **Consultar disponibilidad:** separa las actividades con plazas libres de las completas.

## Actividades de ejemplo

| Actividad | Tipo | Máximo | Inscritas |
|---|---|---|---|
| Taller de escritura | Cultural | 10 | 4 |
| Paseo por la ciudad | Social | 15 | 15 |
| Introducción a la fotografía | Formativa | 8 | 3 |

## Cómo ejecutarlo

Requisitos: Python 3.8 o superior. No hace falta instalar librerías.

```bash
python3 main.py
```

(En Windows puede ser `python main.py` o `py main.py`).

## Elementos de Python utilizados

- **Variables:** para guardar datos y resultados (por ejemplo, las plazas disponibles).
- **Listas:** la lista `actividades` guarda todas las actividades.
- **Diccionarios:** cada actividad es un diccionario con las claves `nombre`, `tipo`,
  `maximo` e `inscritas`.
- **Condicionales (`if`, `elif`, `else`):** para elegir opciones del menú y comprobar si
  quedan plazas.
- **Bucles (`for`, `while`):** `for` para recorrer las actividades y `while` para repetir el menú.
- **Funciones propias:** el código se organiza en funciones como `mostrar_actividades()`,
  `anadir_actividad()`, `inscribir_participante()` y `consultar_disponibles()`.

## Pruebas realizadas

- [ ] Se muestran correctamente todas las actividades.
- [ ] Se puede añadir una actividad nueva.
- [ ] Se puede inscribir a una persona si quedan plazas.
- [ ] No se permite superar el aforo máximo.
- [ ] Las plazas disponibles se calculan correctamente.
- [ ] El programa distingue las actividades completas de las que tienen plazas libres.
- [ ] El programa funciona si no hay actividades registradas.

> Marcad cada casilla (`[x]`) cuando la hayáis probado.

## Ampliación opcional

[Si hacéis alguna ampliación, indicad aquí cuál: cancelar inscripción, buscar por tipo,
actividad con más participantes o resumen general. Si no, borrad este apartado.]

## Estructura del repositorio

```
├── main.py      # Programa principal
└── README.md    # Este archivo
```
