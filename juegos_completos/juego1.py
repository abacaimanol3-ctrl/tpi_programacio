import os
import msvcrt
import random

pos_x = 2
pos_y = 2

turnos = 6
turnos_l = 0
puntos = 0
quest = 0

buf_color = "\033[33m"
floor = "\033[32m"
void = "\033[0m"

alto = 5
ancho = 5

meta_x = random.randint(11, 22)
meta_y = random.randint(11, 22)

preguntas =[["Que tipo de numero sera el resultado?: n * 2 \n 1_par \n 2_impar \n", "1"], 
            ["Que tipo de numero sera el resultado?: 3 / 2 \n 1_entero \n 2_decimal \n", "2"],
            ["Que tipo de numero sera el resultado?: n<0 \n 1_numero positivo \n 2_numero negativo \n", "2"],
            ["esto es verdadero?: -2 < 2 \n 1_verdadero \n 2_falso \n", "1"],
            ["que tipo de numero sera el resultado?: -2 * 2 \n 1_positivo \n 2_negativo \n", "2"]]


llave_p_x = 0
llave_p_y = 0

fails = 1

buf_x = 0
buf_y = 0

llave_n_x = 0
llave_n_y = 0

def gen_buf():
    global buf_x, buf_y

    buf = 0

    buf = random.randint(0,100)

    if buf >= 80:
        buf_x = random.randint(pos_x-3, pos_x+3)
        buf_y = random.randint(pos_y-3, pos_y+3)

    if buf_x == pos_x and buf_y == pos_y:
        gen_buf()

    return buf_x, buf_y

gen_buf()

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


    pregunta = random.randint(0,4)

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
    global pos_x, pos_y, turnos, alto, ancho, turnos_l

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
            estadistica = "Score_" + nombre
            with open(estadistica + ".txt", "a", encoding="utf-8") as archivo:
                jugador = f"Jugador: {nombre} \n"
                turnos_r = f"Turnos restantes: {turnos}\n"
                movimientos = f"Movimientos: {turnos_l}\n"
                preg_ac = f"Preguntas acertadas: {puntos}\n"
                preg_r = f"Preguntas realizadas: {quest}"

                archivo.write(jugador)
                archivo.write(turnos_r)
                archivo.write(movimientos)
                archivo.write(preg_ac)
                archivo.write(preg_r)
            break

        if ancho >= 21:
            ancho = 25
            gen_key(-100, 0, False, True)
        
        if alto >= 21:
            alto = 25
            gen_key(-100, 0, True, False)

        if turnos <= 0:
            print("Juego acabado")
            break



