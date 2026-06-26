import os
import msvcrt
import random

pos_x = 2
pos_y = 2

turnos = 10

alto = 5
ancho = 5

preguntas =["Que tipo de numero sera el resultado?: n * 2 \n 1_par \n 2_impar \n", 
            "Que tipo de numero sera el resultado?: 3 / 2 \n 1_entero \n 2_decimal \n",
            "Que tipo de numero sera el resultado?: n<0 \n 1_numero positivo \n 2_numero negativo \n",
            "esto es verdadero?: -2 < 2 \n 1_verdadero \n 2_falso \n",
            "que tipo de numero sera el resultado?: -2 * 2 \n 1_positivo \n 2_negativo \n"]


llave_p_x = 0
llave_p_y = 0

llave_n_x = 0
llave_n_y = 0

def extendMap(tipo):
    global alto, ancho
    if tipo == "p":
        alto += 5
    elif tipo == "n":
        ancho += 5

    draw()
    return alto, ancho


def puzzle(llave):
    global turnos, alto, ancho

    gen_key()

    pregunta = random.randint(0,5)
    if pregunta == 1:
        print(preguntas[0])
        respuesta = input("Ingrese la respuesta: ")

        if respuesta == "1":
            turnos += 10
            extendMap(llave)

        elif respuesta == "2":
            turnos -= 3

        else:
            print("Respuesta no reconosida")

    if pregunta == 2:
        print(preguntas[1])
        respuesta = input("Ingrese la respuesta: ")

        if respuesta == "2":
            turnos += 10
            extendMap(llave)
            

        elif respuesta == "1":
            turnos -= 3

        else:
            print("Respuesta no reconosida")
            
    if pregunta == 3:
        print(preguntas[2])
        respuesta = input("Ingrese la respuesta: ")

        if respuesta == "2":
            turnos += 10
            extendMap(llave)

        elif respuesta == "1":
            turnos -= 3

        else:
            print("Respuesta no reconosida")

    if pregunta == 4:
        print(preguntas[3])
        respuesta = input("Ingrese la respuesta: ")

        if respuesta == "1":
            turnos += 10
            extendMap(llave)

        elif respuesta == "2":
            turnos -= 3

        else:
            print("Respuesta no reconosida")

    if pregunta == 5:
        print(preguntas[4])
        respuesta = input("Ingrese la respuesta: ")

        if respuesta == "2":
            turnos += 10
            extendMap(llave)

        elif respuesta == "1":
            turnos -= 3

        else:
            print("Respuesta no reconosida")   


def gen_key():
    global llave_p_x, llave_p_y, llave_n_x, llave_n_y

    llave_p_x = random.randint(1,ancho-3)
    llave_p_y = random.randint(alto-3,alto-1)

    llave_n_x = random.randint(ancho-3, ancho-1)
    llave_n_y = random.randint(1, alto-3)

    return llave_p_x, llave_p_y


def draw():
    os.system("cls")

    for i in range(0,alto):
        for j in range(0,ancho):
            if j != pos_x or i != pos_y:
                if j == llave_p_x and i == llave_p_y:
                    print("+", end="")

                elif j == llave_n_x and i == llave_n_y:
                    print("-", end="")
                else:
                    print(".", end="")


            else:
                print("@", end="")
                
        print()


def Init():
    global pos_x, pos_y

    gen_key()
    draw()

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8").lower()

            if key == "w" and pos_y > 0:
                pos_y -= 1
                draw()

            elif key == "s" and pos_y < alto-1:
                pos_y += 1
                draw()
                
            elif key == "a" and pos_x > 0:
                pos_x -= 1
                draw()
                
            elif key == "d" and pos_x < ancho-1:
                pos_x += 1
                draw()

            elif key == "q":
                break
        
        if pos_x == llave_p_x and pos_y == llave_p_y:
            puzzle("p")

        elif pos_x == llave_n_x and pos_y == llave_n_y:
            puzzle("n")



