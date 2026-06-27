import os
from juegos_completos import juego1
from juegos_completos import quiz_matematica
from juegos_completos import adivina_palabra
from juegos_completos import numero_perdido

# Solicitar nombre una sola vez al iniciar la app
os.system("cls")
print("==========================================")
print("           PLAY.IN EDUGAMES               ")
print("==========================================")
nombre_usuario = input("Ingrese su nombre: ")
if nombre_usuario == "":
    nombre_usuario = "Jugador"

while True:
    try:
        print("\n==========================================")
        print(f"   MENÚ PRINCIPAL - Bienvenido/a {nombre_usuario}")
        print("==========================================")
        print("1. Jugar: MathQuest (Imanol)")
        print("2. Jugar: Quiz de Matemática (Diego)")
        print("3. Jugar: Adivina la Palabra (Joel)")
        print("4. Jugar: El Número Perdido (Máximo)")
        print("5. Ver Puntajes (Quiz Matemática)")
        print("6. Ver Puntajes (Adivina la Palabra)")
        print("7. Ver Rankings Globales")
        print("0. Salir")
        print("==========================================")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            juego1.Init()
        elif opcion == 2:
            quiz_matematica.Init(nombre_usuario)
        elif opcion == 3:
            adivina_palabra.Init(nombre_usuario)
        elif opcion == 4:
            numero_perdido.juego_numero_perdido()
        elif opcion == 5:
            quiz_matematica.ver_puntajes()
        elif opcion == 6:
            adivina_palabra.ver_puntajes()
        elif opcion == 7:
            quiz_matematica.ranking_jugadores()
            adivina_palabra.ranking_jugadores()
        elif opcion == 0:
            print("\nGracias por jugar a Play.In EduGames. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

    except ValueError:
        print("Error: Por favor, ingrese un número válido del menú.")