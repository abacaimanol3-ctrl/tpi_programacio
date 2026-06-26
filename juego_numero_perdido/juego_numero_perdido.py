import random


def juego_numero_perdido():
    preguntas = [
        {"base": 5, "incognita": 5, "resultado": 25},
        {"base": 7, "incognita": 3, "resultado": 21},
        {"base": 9, "incognita": 4, "resultado": 36},
        {"base": 3, "incognita": 8, "resultado": 24},
        {"base": 5, "incognita": 7, "resultado": 35},
        {"base": 7, "incognita": 6, "resultado": 42},
        {"base": 9, "incognita": 9, "resultado": 81},
        {"base": 3, "incognita": 7, "resultado": 21},
        {"base": 5, "incognita": 9, "resultado": 45},
        {"base": 7, "incognita": 8, "resultado": 56},
    ]

    jugando = True

    while jugando:
        racha_aciertos = 0
        perdio = False

        print("\n==========================================")
        print("¡BIENVENIDO AL JUEGO DEL NÚMERO PERDIDO!")
        print("Reglas: Adivina el número que falta.")
        print("¡Llega a 5 aciertos seguidos para ganar!")
        print("==========================================\n")

        while not perdio and racha_aciertos < 5:
            pregunta_actual = random.choice(preguntas)

            print(f"Racha actual: {racha_aciertos}/5")
            print(
                f"¿{pregunta_actual['base']} x ___ = {pregunta_actual['resultado']}?"
            )

            try:
                respuesta_usuario = int(input("Ingresa tu respuesta: "))
            except ValueError:
                print("¡Error! Por favor, ingresa un número o una opción válida.\n")
                continue

            if respuesta_usuario == pregunta_actual["incognita"]:
                print("¡CORRECTO! Excelente.\n")
                racha_aciertos += 1
            else:
                print("\n¡HAS PERDIDO!")
                print(
                    f"El número correcto era el {pregunta_actual['incognita']}."
                )
                perdio = True

        if racha_aciertos == 5:
            print("¡FELICITACIONES! Completaste el desafío con éxito. ⭐")

        while True:
            print("\n¿Qué deseas hacer?")
            print("1. Intentar de vuelta")
            print("2. Salir")
            opcion = input("Ingresa tu opción (1 o 2): ")

            if opcion == "1":
                break
            elif opcion == "2":
                print("Saliendo de la actividad...")
                jugando = False
                break
            else:
                print("Opción inválida. Por favor, elige 1 o 2.")