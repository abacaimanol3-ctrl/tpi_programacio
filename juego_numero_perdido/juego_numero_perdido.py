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

    racha_aciertos = 0

    print("\n--- VERSION BETA: JUEGO DEL NUMERO PERDIDO ---")

    while racha_aciertos < 5:
        pregunta_actual = random.choice(preguntas)

        print(f"Racha actual: {racha_aciertos}/5")
        print(
            f"¿{pregunta_actual['base']} x ___ = {pregunta_actual['resultado']}?"
        )

        respuesta_usuario = int(input("Ingresa tu respuesta: "))

        if respuesta_usuario == pregunta_actual["incognita"]:
            print("¡Bien!\n")
            racha_aciertos += 1
        else:
            print("")

    print("¡Ganaste la beta!")