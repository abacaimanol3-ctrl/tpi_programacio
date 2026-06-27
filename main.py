import os

while True:
    from juegos_completos import juego1
        
    os.system("cls")
    try:
        print("Juegos disponibles: \n"
                    "1_Juego: MathQuest")

        opcion = opcion = int(input("\n"
                            "Seleccione un juego: "))

        if opcion == 1:
            juego1.Init() 
        
        else:
            print("Opcion invalida")
        
    except ValueError:
        print("Opcion invalida")


