# =================================================================
# JUEGO: QUIZ DE MATEMÁTICA
# DESARROLLADOR: DIEGO ZALAZAR (Adaptado para Play.In)
# =================================================================

# ---------------------------------
# GUARDAR PUNTAJE
# ---------------------------------
def guardar_puntaje(nombre, puntos):
    archivo = open("puntajes_matematica.txt", "a", encoding="utf-8")
    linea = nombre + " - " + str(puntos) + "\n"
    archivo.write(linea)
    archivo.close()


# ---------------------------------
# VER PUNTAJES
# ---------------------------------
def ver_puntajes():
    try:
        archivo = open("puntajes_matematica.txt", "r", encoding="utf-8")
        print("\n===== PUNTAJES GUARDADOS (MATH) =====")
        contenido = archivo.read()
        print(contenido)
        archivo.close()
    except FileNotFoundError:
        print("Todavía no hay puntajes guardados.")


# ---------------------------------
# RANKING DE JUGADORES
# ---------------------------------
def ranking_jugadores():
    try:
        archivo = open("puntajes_matematica.txt", "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        ranking = []
        for linea in lineas:
            linea_limpia = linea.strip()
            if linea_limpia == "":
                continue
            datos = linea_limpia.split(" - ")
            if len(datos) == 2:
                nombre = datos[0]
                puntos = int(datos[1])
                ranking.append([nombre, puntos])

        # ORDENAMIENTO BURBUJA
        largo = len(ranking)
        for i in range(largo):
            for j in range(i + 1, largo):
                jugador_actual = ranking[i]
                jugador_siguiente = ranking[j]
                if jugador_actual[1] < jugador_siguiente[1]:
                    temporal = ranking[i]
                    ranking[i] = ranking[j]
                    ranking[j] = temporal

        print("\n===== RANKING (MATH) =====")
        puesto = 1
        for jugador in ranking:
            nombre_j = jugador[0]
            puntos_j = jugador[1]
            print(str(puesto) + ".", nombre_j, "-", str(puntos_j), "puntos")
            puesto = puesto + 1

    except FileNotFoundError:
        print("No hay datos para mostrar.")


# ---------------------------------
# FUNCIÓN PRINCIPAL DEL JUEGO
# ---------------------------------
def Init(nombre):
    preguntas = [
        ["¿Cuánto es 5 x 4?", "20"],
        ["¿Cuánto es 18 / 3?", "6"],
        ["¿Cuánto es 7 + 8?", "15"],
        ["¿Cuánto es 12 - 5?", "7"],
        ["¿El número 11 es primo? (si/no)", "si"],
        ["¿Cuánto es 9 x 9?", "81"],
        ["¿Cuánto es 100 / 10?", "10"],
        ["¿Cuánto es 14 + 6?", "20"],
        ["¿Cuánto es 25 - 10?", "15"],
        ["¿Cuánto es 8 x 7?", "56"]
    ]

    puntos = 0
    print("\n===== QUIZ DE MATEMÁTICA =====")

    for elemento in preguntas:
        pregunta = elemento[0]
        respuesta_correcta = elemento[1]
        
        r = input(pregunta + " ")
        
        if r.lower() == respuesta_correcta.lower():
            print("Correcto")
            puntos = puntos + 1
        else:
            print("Incorrecto")

    print("\nPuntaje obtenido:", puntos)
    guardar_puntaje(nombre, puntos)