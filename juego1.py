import os
import msvcrt
import random

pos_x = 2
pos_y = 2

alto = 5
ancho = 5

llave_x = 0
llave_y = 0

def gen_key():
    global llave_x, llave_y

    llave_x = random.randint(1,ancho-1)
    llave_y = random.randint(4,alto-1)

    return llave_x, llave_y

def draw():
    os.system("cls")

    for i in range(0,alto):
        for j in range(0,ancho):
            if j != pos_x or i != pos_y:
                if j == llave_x and i == llave_y:
                    print("!", end="")

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

            elif key == "s" and pos_y < 4:
                pos_y += 1
                draw()
                
            elif key == "a" and pos_x > 0:
                pos_x -= 1
                draw()
                
            elif key == "d" and pos_x < 4:
                pos_x += 1
                draw()

            elif key == "q":
                break
                


