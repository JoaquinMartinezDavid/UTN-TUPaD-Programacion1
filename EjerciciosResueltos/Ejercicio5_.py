def ejercicio5():
    '''EJERCICIO 5: "ESCAPE ROOM: LA ARENA DEL GLADIADOR'''
    Vida_ene=int(100)
    Daño_Base_en=int(12)
    
    Turno_ene=True
    while True:
        Nombre_Gla=input("Ingres el nombre del Gladiadior: ").title().strip()
        if Nombre_Gla!="" and Nombre_Gla.replace(" ","").isalpha():
            print("SURGE UN NUEVO GLADIADOR")
            Vida_Gla=int(100)
            Pociones_Vida=int(3)
            Daño_Base=int(15)
            Turno_Gla=True
            break
        else:
            print("ERROR: Debe ingresar un nombre,debe contener solo letras")
    while Vida_Gla>0 and Vida_ene>0:
        while Turno_Gla and Vida_Gla>0:
            Turno_ene=True
            print("Gladiador:\n" \
            f"Vida: {Vida_Gla}\n"
            f"Pociones de vida:{Pociones_Vida}\n")

            print("Enemigo:\n" \
            f"Vida del enemigo: {Vida_ene}\n")
            
            while True:
                print("-MENÚ--\n" \
                "[1] ATAQUE PESADO\n" \
                "[2] RÁFAGA VELOZ\n" \
                "[3] CURAR\n")
                Op=input("Ingrese la opción que desee: ").strip()
                if Op.isdigit() and Op in ["1","2","3"]:
                    print("ELECCIÓN CONFIRMADA GLADIADOR")
                    break
                else:
                    print("ERROR: Debe ingresar una de las opciones del menú.")
            match Op:
                case "1":
                    if Vida_ene<20:
                        print("GOLPEEE CÍTICOOO DEL GALDIADOOR")
                        Golpe_crítico=float(Daño_Base*(1.5))
                        print(f"!ATACASTE AL ENEMIGO POR {Golpe_crítico} PUNTOS DE DAÑO¡")
                        Vida_ene-=Golpe_crítico
                    else:
                        print(f"!ATACASTE AL ENEMIGO POR {Daño_Base} PUNTOS DE DAÑO¡")
                        Vida_ene-=Daño_Base
                    Turno_Gla=False
                case "2":
                    print("!RÁFAGA VELOZ¡")
                    for i in range(3):
                        Vida_ene-=5
                        print("> Golpe conectado por 5 de daño")
                    Turno_Gla=False
                case "3":
                    print("!CURAAR¡")
                    if Pociones_Vida>0 and Pociones_Vida<=3:
                        Vida_Gla+=30
                        Pociones_Vida-=1
                        print(f"VIDA RESTAURADA: {Vida_Gla}")
                        print(f"GLADIADOR TE QUEDAN: {Pociones_Vida} pociones.")
                        if Vida_Gla>100:
                            Vida_Gla=int(100)
                    else:
                        print("¡NO QUEDAN MAS POCIONES!")
                    Turno_Gla=False
        if Vida_ene>0:
            print("EL ENEMIGO VA A ATACAR....\n")
            while Turno_ene:
                Turno_Gla=True
                Vida_Gla-=12
                print(f"!EL ENEMIGO TE ATACÓ POR {Daño_Base_en} PUNTOS DE DAÑO¡")
                Turno_ene=False
    if Vida_Gla>0:
        print(f"¡VICTORIA!: {Nombre_Gla} ha ganado la batalla.")
    else:
        print(f"!DERROTA¡: Has caido en combate")
ejercicio5()