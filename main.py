#!/usr/bin/env python3
"""Organizador de actividades de una asociación, ejecutado por consola."""

# GUÍA PARA LA PRESENTACIÓN:
# 1. main() crea los datos iniciales y muestra el menú.
# 2. Cada opción llama a una función que realiza una tarea concreta.
# 3. Las actividades se guardan en una lista de diccionarios.
# 4. Las funciones de lectura comprueban los datos que escribe el usuario.
# Python primero define estas funciones; el programa arranca en el bloque final.


def leer_texto(mensaje):
    """Pide un texto y evita valores vacíos."""
    # mensaje es el texto que verá el usuario cuando se le pida un dato.
    # while True repite la petición hasta que se devuelve un valor válido.
    while True:
        # input() lee desde la consola; strip() quita espacios de los extremos.
        texto = input(mensaje).strip()
        # Una cadena vacía se considera falsa en un condicional.
        if texto:
            # return entrega el resultado a quien llamó a la función y termina.
            return texto
        print("El texto no puede estar vacío.")


def leer_entero(mensaje, minimo, maximo=None):
    """Pide un número entero dentro del intervalo permitido."""
    # None indica que no hay límite máximo si no se proporciona ese argumento.
    while True:
        try:
            # input() devuelve texto; int() intenta convertirlo a número entero.
            numero = int(input(mensaje))
        except ValueError:
            # Si se escribe algo como 'hola' o '2.5', la conversión falla.
            # Capturamos ese error para que el programa pueda seguir funcionando.
            print("Introduce un número entero.")
            # continue vuelve al comienzo del bucle y pide otro valor.
            continue
        # Rechazamos valores inferiores al mínimo o superiores al máximo,
        # comprobando el máximo solo cuando se ha definido.
        if numero < minimo or (maximo is not None and numero > maximo):
            if maximo is None:
                print(f"Introduce un número mayor o igual que {minimo}.")
            else:
                print(f"Introduce un número entre {minimo} y {maximo}.")
            continue
        return numero


def mostrar_actividades(actividades):
    """Muestra los datos y las plazas libres de cada actividad."""
    # 'not actividades' comprueba si la lista está vacía.
    if not actividades:
        print("No hay actividades registradas.")
        return
    # for recorre la lista. enumerate añade un número visible desde el 1.
    for numero, actividad in enumerate(actividades, start=1):
        # Accedemos a los datos del diccionario mediante sus claves entre [].
        plazas = actividad["maximo"] - actividad["inscritas"]
        # Las cadenas f permiten insertar valores dentro del texto usando {}.
        print(
            f"{numero}. {actividad['nombre']} | Tipo: {actividad['tipo']} | "
            f"Aforo máximo: {actividad['maximo']} | "
            f"Inscritas: {actividad['inscritas']} | Plazas libres: {plazas}"
        )


def anadir_actividad(actividades):
    """Registra una actividad sin participantes iniciales."""
    # Reutilizamos las funciones de lectura para validar todos los datos.
    nombre = leer_texto("Nombre de la actividad: ")
    tipo = leer_texto("Tipo de actividad: ")
    maximo = leer_entero("Aforo máximo: ", 1)
    # append() añade un diccionario al final de la lista recibida.
    # Al modificar esa misma lista, el cambio también se ve desde main().
    actividades.append({
        "nombre": nombre,
        "tipo": tipo,
        "maximo": maximo,
        "inscritas": 0,  # Toda actividad nueva comienza sin participantes.
    })
    print(f"Actividad '{nombre}' añadida correctamente.")


def inscribir_participante(actividades):
    """Inscribe a una persona siempre que quede una plaza libre."""
    # Mostramos los números de las actividades antes de pedir la selección.
    mostrar_actividades(actividades)
    if not actividades:
        return
    # len() cuenta las actividades y evita elegir un número inexistente.
    numero = leer_entero("Número de actividad (0 para cancelar): ", 0, len(actividades))
    if numero == 0:
        return
    # Las listas empiezan en la posición 0: la opción 1 corresponde al índice 0.
    actividad = actividades[numero - 1]
    # Comprobamos el aforo ANTES de aumentar el contador de inscripciones.
    if actividad["inscritas"] >= actividad["maximo"]:
        print("La actividad está completa. No se puede realizar la inscripción.")
    else:
        # += 1 suma una persona al contador guardado en el diccionario.
        actividad["inscritas"] += 1
        print(f"Inscripción realizada en '{actividad['nombre']}'.")


def consultar_disponibles(actividades):
    """Separa las actividades disponibles de las completas."""
    if not actividades:
        print("No hay actividades registradas.")
        return
    # Creamos dos listas temporales para agrupar los resultados.
    disponibles = []
    completas = []
    # Cada actividad va a un grupo según su número de inscritas y su aforo.
    for actividad in actividades:
        if actividad["inscritas"] < actividad["maximo"]:
            disponibles.append(actividad)
        else:
            completas.append(actividad)
    # Reutilizamos la función de mostrar para no repetir el formato de salida.
    # \n introduce un salto de línea en el texto mostrado por consola.
    print("\nActividades con plazas libres:")
    if disponibles:
        mostrar_actividades(disponibles)
    else:
        print("No hay actividades con plazas libres.")
    print("\nActividades completas:")
    if completas:
        mostrar_actividades(completas)
    else:
        print("No hay actividades completas.")


def main():
    # Esta es la función principal: coordina los datos y las opciones del menú.
    # [] define una lista y cada {} contiene un diccionario con cuatro claves.
    # Los datos están en memoria: al cerrar el programa no se guardan en disco.
    actividades = [
        {"nombre": "Taller de escritura", "tipo": "Cultural", "maximo": 10, "inscritas": 4},
        {"nombre": "Paseo por la ciudad", "tipo": "Social", "maximo": 15, "inscritas": 15},
        {"nombre": "Introducción a la fotografía", "tipo": "Formativa", "maximo": 8, "inscritas": 3},
    ]
    # El menú se repite después de cada operación hasta que se elige salir.
    while True:
        print("\n--- Organizador de actividades ---")
        print("1. Mostrar actividades")
        print("2. Añadir una actividad")
        print("3. Inscribir participante")
        print("4. Consultar disponibilidad")
        print("0. Salir")
        opcion = leer_entero("Elige una opción: ", 0, 4)
        # if/elif/else ejecuta únicamente la rama de la opción elegida.
        # Pasamos la misma lista a las funciones para consultar o modificarla.
        if opcion == 1:
            mostrar_actividades(actividades)
        elif opcion == 2:
            anadir_actividad(actividades)
        elif opcion == 3:
            inscribir_participante(actividades)
        elif opcion == 4:
            consultar_disponibles(actividades)
        else:
            print("¡Hasta pronto!")
            # Como la opción ya está validada, aquí solo puede ser 0.
            # break termina el bucle del menú y main() llega a su final.
            break


# Este bloque ejecuta main() solo si abrimos este archivo como programa.
# Si otro archivo lo importa, las funciones quedan disponibles sin abrir el menú.
if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        # Permite terminar con Ctrl+C o al cerrarse la entrada de consola
        # sin mostrar un mensaje técnico de error.
        print("\nPrograma finalizado.")
