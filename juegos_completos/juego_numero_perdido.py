import random


def guardar_puntaje(nombre_usuario, racha):
    with open("puntajes.txt", "a") as archivo:
        archivo.write(f"Jugador: {nombre_usuario} - Racha alcanzada: {racha}/5\n")
    print("¡Puntuación guardada con éxito!")


def mostrar_puntajes():
    print("\n------------------------------------")
    print("   HISTORIAL DE PUNTAJES RÉCORD     ")
    print("------------------------------------")
    try:
        with open("puntajes.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido == "":
                print("El archivo está vacío. ¡Sé el primero en anotar tu récord!")
            else:
                print(contenido)
    except FileNotFoundError:
        print("Aún no hay puntuaciones registradas.")
    print("------------------------------------\n")


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

    menu_interno = True

    while menu_interno:
        print("\n==========================================")
        print("      JUEGO: EL NÚMERO PERDIDO            ")
        print("==========================================")
        print("1. Iniciar Juego")
        print("2. Ver Puntaje Récord")
        print("3. Salir al Menú Principal")
        opcion_sub = input("Ingresa tu opción (1, 2 o 3): ")

        if opcion_sub == "1":
            racha_aciertos = 0
            perdio = False

            print("\n==========================================")
            print("          ¡QUE COMIENCE EL JUEGO!         ")
            print("Reglas: Adivina el número que falta.")
            print("¡Llega a 5 aciertos seguidos para ganar!")
            print("==========================================\n")

            while not perdio and racha_aciertos < 5:
                pregunta_actual = random.choice(preguntas)

                print(f"Racha actual: {racha_aciertos}/5")
                print(f"¿{pregunta_actual['base']} x ___ = {pregunta_actual['resultado']}?")

                try:
                    respuesta_usuario = int(input("Ingresa tu respuesta: "))
                except ValueError:
                    print("¡Error! Por favor, ingresa un número válido.\n")
                    continue

                if respuesta_usuario == pregunta_actual["incognita"]:
                    print("¡CORRECTO! Excelente.\n")
                    racha_aciertos += 1
                else:
                    print("\n¡HAS PERDIDO!")
                    print(f"El número correcto era el {pregunta_actual['incognita']}.")
                    perdio = True 

            if racha_aciertos == 5:
                print("¡FELICITACIONES! Completaste el desafío con éxito. ⭐")

            print(f"\nTuviste una racha de {racha_aciertos} aciertos.")
            quiere_guardar = input("¿Querés guardar tu puntuación récord? (S/N): ")
            if quiere_guardar.upper() == "S":
                nombre = input("Ingresa tu nombre: ")
                guardar_puntaje(nombre, racha_aciertos)

        elif opcion_sub == "2":
            mostrar_puntajes()

        elif opcion_sub == "3":
            print("Volviendo al menú principal del sistema...")
            menu_interno = False

        else:
            print("Opción inválida. Por favor, elige 1, 2 o 3.")