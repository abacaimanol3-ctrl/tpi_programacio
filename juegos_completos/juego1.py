import os
import msvcrt
import random

pos_x = 2
pos_y = 2

turnos = 6
turnos_l = 0
puntos = 0
quest = 0

runs = 0

buf_color = "\033[33m"
floor = "\033[32m"
void = "\033[0m"

alto = 5
ancho = 5

meta_x = random.randint(11, 38)
meta_y = random.randint(11, 22)

preguntas =[["Que tipo de numero sera el resultado?: n * 2 \n 1_par \n 2_impar \n", "1"], 
            ["Que tipo de numero sera el resultado?: 3 / 2 \n 1_entero \n 2_decimal \n", "2"],
            ["Que tipo de numero sera el resultado?: n<0 \n 1_numero positivo \n 2_numero negativo \n", "2"],
            ["Esto es verdadero?: -2 < 2 \n 1_verdadero \n 2_falso \n", "1"],
            ["Que tipo de numero sera el resultado?: -2 * 2 \n 1_positivo \n 2_negativo \n", "2"],
            ["Esto es verdadero?: (-4 < n < -2) n = -3 \n 1_verdadero \n 2_falso ", "1"]]


llave_p_x = 0
llave_p_y = 0

fails = 1

buf_x = 0
buf_y = 0

llave_n_x = 0
llave_n_y = 0

def reset():
    global pos_x, pos_y, turnos, turnos_l, puntos, quest, alto, ancho
    global meta_x, meta_y, llave_p_x, llave_p_y, fails, buf_x, buf_y, llave_n_x, llave_n_y

    pos_x = 2
    pos_y = 2
    turnos = 6
    turnos_l = 0
    puntos = 0
    quest = 0
    alto = 5
    ancho = 5
    fails = 1
    meta_x = random.randint(11, 22)
    meta_y = random.randint(11, 22)
    
    gen_key("", "", False, False)
    gen_buf()

def gen_buf():
    global buf_x, buf_y

    buf = 0

    buf = random.randint(0,100)

    if buf >= 70:
        buf_x = random.randint(pos_x-3, pos_x+3)
        buf_y = random.randint(pos_y-3, pos_y+3)
    
    else:
        buf_x = -1
        buf_y = -1

    if buf_x == pos_x and buf_y == pos_y:
        gen_buf()
        return buf_x, buf_y

    return buf_x, buf_y

def questions(q, k):
    global turnos, alto, ancho, fails, puntos, quest

    print(preguntas[q][0])
    r = input("Ingrese su respuesta: ")
    
    if r == preguntas[q][1]:
        turnos += 7
        puntos += 1
        extendMap(k)
    
    else:
        fails -= 0.1
        turnos *= fails
        turnos = int(turnos)

        gen_key("", "", False, False)
        draw()

    quest += 1

    gen_buf()

def extendMap(tipo):
    global alto, ancho

    if tipo == "p":
        alto += 5
    elif tipo == "n":
        ancho += 5

    gen_key("", "", False, False)
    gen_buf()

    draw()
    return alto, ancho


def puzzle(llave):
    global turnos, alto, ancho

    pregunta = random.randint(0,5)

    questions(pregunta, llave)


def gen_key(referencia1, referencia2, key_1, key_2):
    global llave_p_x, llave_p_y, llave_n_x, llave_n_y

    if referencia1 == "" and referencia2 == "":
        llave_p_x = random.randint(1,ancho-3)
        llave_p_y = random.randint(alto-3,alto-1)

        llave_n_x = random.randint(ancho-3, ancho-1)
        llave_n_y = random.randint(1, alto-3)
    
    else:
        if key_1 == True:
            llave_p_x = random.randint(referencia1-6, referencia1+6)
            llave_p_y = random.randint(referencia2-6, referencia2+6)

        if key_2 == True:
            llave_n_x = random.randint(referencia1-6, referencia1+6)
            llave_n_y = random.randint(referencia2-6, referencia2+6)

        if (llave_n_x == pos_x and llave_n_y == pos_y) or (llave_p_x == pos_x and llave_p_y == pos_y):
            gen_key(referencia1, referencia2, key_1, key_2)
            
            return llave_p_x, llave_p_y

    if (llave_n_x == pos_x and llave_n_y == pos_y) or (llave_p_x == pos_x and llave_p_y == pos_y):
        gen_key("", "", False, False)

    return llave_p_x, llave_p_y


def draw():
    global turnos, turnos_l

    os.system("cls")
    turnos -= 1

    print("Te quedan: ", turnos, "turnos")

    for i in range(0,alto):
        for j in range(0,ancho):
            if j != pos_x or i != pos_y:
                if j == llave_p_x and i == llave_p_y:
                    print("+", end="")

                elif j == llave_n_x and i == llave_n_y:
                    print("-", end="")

                elif j == meta_x and i == meta_y:
                    print("W", end="")

                elif j == buf_x and i == buf_y:
                    print(f"{buf_color}B{void}", end="")

                else:
                    print(f"{floor}.{void}", end="")


            else:
                print("@", end="")
                
        print()

def Init():
    global pos_x, pos_y, turnos, alto, ancho, turnos_l, runs

    reset()

    gen_key("", "", False, False)
    draw()

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8").lower()

            if key == "w" and pos_y > 0:
                pos_y -= 1
                turnos_l += 1
                draw()

            elif key == "s" and pos_y < alto-1:
                pos_y += 1
                turnos_l += 1
                draw()
                
            elif key == "a" and pos_x > 0:
                pos_x -= 1
                turnos_l += 1
                draw()
                
            elif key == "d" and pos_x < ancho-1:
                pos_x += 1
                turnos_l += 1
                draw()

            elif key == "q":
                while True:
                    print("Estas seguro de querer salir? \n 1_si \n 2_no")
                    opcion = input("Ingresa una opcion: ")

                    if opcion == "1":
                        break
                    elif opcion == "2":
                        reset()
                        Init()

                        break

                    else:
                        print("Opcion no identificada")

                break
        if pos_x == llave_p_x and pos_y == llave_p_y:
            puzzle("p")

        elif pos_x == llave_n_x and pos_y == llave_n_y:
            puzzle("n")

        elif pos_x == buf_x and pos_y == buf_y:
            print("que tipo de ventaja quieres?: \n 1_traer las llaves cerca \n 2_mas turnos")
            op = input("Ingresa tu respuesta aqui: ")

            if op == "1":
                gen_key(pos_x, pos_y, True, True)
                gen_buf()
                draw()
            
            elif op == "2":
                turnos += 10
                gen_buf()
                draw()

        elif pos_x == meta_x and pos_y == meta_y:
            print("En hora buena. Has ganado")
            nombre = input("Introduce tu nombre aqui: ")
            estadistica = "Score_" + nombre + ".txt"

            with open(estadistica, "w", encoding="utf-8") as archivo:
                runs += 1

                archivo.write(f"Jugador: {nombre} \n")
                archivo.write(f"Partidas jugadas: {runs} \n")
                archivo.write(f"Turnos restantes: {turnos}\n")
                archivo.write(f"Movimientos: {turnos_l}\n")
                archivo.write(f"Preguntas acertadas: {puntos}\n")
                archivo.write(f"Preguntas realizadas: {quest}")
                


            break

        if ancho >= 41:
            ancho = 40
            gen_key(-100, 0, False, True)
        
        if alto >= 26:
            alto = 25
            gen_key(-100, 0, True, False)

        if turnos <= 0:
            runs += 1
            print("Juego acabado")
            break



