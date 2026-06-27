# =================================================================
# JUEGO: ADIVINA LA PALABRA
# DESARROLLADOR: JOEL CEBALLOS
# =================================================================

def guardar_puntaje(nombre, puntos):
    archivo = open("puntajes_palabras.txt", "a", encoding="utf-8")
    linea = nombre + " - " + str(puntos) + "\n"
    archivo.write(linea)
    archivo.close()

def ver_puntajes():
    try:
        archivo = open("puntajes_palabras.txt", "r", encoding="utf-8")
        print("\n===== PUNTAJES GUARDADOS (PALABRAS) =====")
        contenido = archivo.read()
        print(contenido)
        archivo.close()
    except FileNotFoundError:
        print("Todavía no hay puntajes guardados.")

def ranking_jugadores():
    try:
        archivo = open("puntajes_palabras.txt", "r", encoding="utf-8")
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

        largo = len(ranking)
        for i in range(largo):
            for j in range(i + 1, largo):
                if ranking[i][1] < ranking[j][1]:
                    temporal = ranking[i]
                    ranking[i] = ranking[j]
                    ranking[j] = temporal

        print("\n===== RANKING (PALABRAS) =====")
        puesto = 1
        for jugador in ranking:
            print(str(puesto) + ".", jugador[0], "-", str(jugador[1]), "puntos")
            puesto += 1
    except FileNotFoundError:
        print("No hay datos para mostrar.")

def Init(nombre):
    palabras = [
        ["perro", "Animal que ladra"],
        ["escuela", "Lugar donde estudias"],
        ["argentina", "País donde vivimos"],
        ["computadora", "Máquina para programar"],
        ["futbol", "Deporte muy popular"],
        ["gato", "Animal que maúlla"],
        ["lapiz", "Se usa para escribir"],
        ["invierno", "Estación más fría del año"],
        ["biblioteca", "Lugar donde hay libros"],
        ["montaña", "Elevación natural del terreno"]
    ]

    print("\n===== ADIVINA LA PALABRA =====")
    opcion_numero = input("Elegí un número del 1 al 10 para tu palabra: ")
    
    if opcion_numero in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        indice = int(opcion_numero) - 1
    else:
        print("Opción inválida. Te asignamos la palabra número 1.")
        indice = 0

    elemento_elegido = palabras[indice]
    palabra = elemento_elegido[0]
    pista = elemento_elegido[1]

    intentos = 3
    puntos = 0
    print("Pista:", pista)

    while intentos > 0:
        respuesta = input("Tu respuesta: ")
        if respuesta.lower() == palabra.lower():
            puntos = intentos
            print("¡Correcto!")
            intentos = 0  
        else:
            intentos -= 1  
            if intentos > 0:
                print("Incorrecto. Te quedan", intentos, "intentos")

    print("La palabra era:", palabra)
    print("Puntos obtenidos:", puntos)
    guardar_puntaje(nombre, puntos)