def ejercicio3():
    print('''Ejercicio 3 (Alta) — “Agenda de Turnos con 
    Nombres (sin listas)”''')
    activa=True
    Lunes1=""
    Lunes2=""
    Lunes3=""
    Lunes4=""
    Martes1=""
    Martes2=""
    Martes3=""
    while activa:
        print("[1] RESERVAR TURNO\n" \
        "[2] CANCELAR TURNO\n" \
        "[3] VER AGENDA DEL DÍA \n" \
        "[4] VER RESUMEN GENERAL\n" \
        "[5] CERRAR SISTEMA\n")
        while True:
            Op=input("Ingrese un número de las opciones: ").strip()
            if Op=="" or not Op.isdigit():
                print("ERROR: Debe ingresar un número, entero y positivo")
                continue
            elif Op not in ["1","2","3","4","5"]:
                print("ERROR: Debe ingresar un número de las opciones.")
                continue
            else:
                break
        match Op:
            case "1":
                print("Sección: Reservar Turno")
                
                while True:
                    Dia=input("Selecciones el día:\n" \
                    "[1] Lunes\n" \
                    "[2] Martes: ")
                    if Dia in ["1","2"]:
                        break
                    else:
                        print("ERROR: Debe ingresar una de las opciones.")
                        continue
                        
                
                while True:
                    Nombre=input("Ingrese su Nombre: ").strip().title()
                    if Nombre!="" and Nombre.replace(" ","").isalpha():
                           
                        break
                    print("ERROR: Debe ingresar un nombre, el cúal solo debe tener letras")
                match Dia:
                    case "1":
                        print("Turno para el día Lunes:")
                        if Nombre == Lunes1 or Nombre == Lunes2 or Nombre == Lunes3 or Nombre == Lunes4:
                            print("ERROR: Ya tiene un turno asignado para este día.")
                        elif Lunes1=="":
                            print("Turno Reservado")
                            Lunes1=Nombre
                        elif Lunes2=="":
                            print("Turno Reservado")
                            Lunes2=Nombre
                        elif Lunes3=="":
                            print("Turno Reservado")
                            Lunes3=Nombre
                        elif Lunes4=="":
                            print("Turno Reservado")
                            Lunes4=Nombre
                        else:
                            print("No hay ningún turno disponible para el Día Lunes, pruebe con el día Martes.")
                    case "2":
                        print("Turno para el día Martes: ")
                        if Nombre==Martes1 or  Nombre==Martes2 or  Nombre==Martes3:
                            print("ERROR: Ya tieneun turno asignado para este día.")                        
                        elif Martes1=="":
                            print("Turno Reservado")
                            Martes1=Nombre
                        elif Martes2=="":
                            print("Turno Reservado")
                            Martes2=Nombre
                        elif Martes3=="":
                            print("Turno Reservado")
                            Martes3=Nombre
                        else:
                            print("Sin turnos disponibles para el Martes, intente con el día Lunes")
            case "2":
                print("Sección: Cancelar Turno")
                while True:
                    Dia_can=input("Seleccione el día en el cual tenía su turno:\n" \
                    "[1] Lunes\n" \
                    "[2] Martes: ")
                    if Dia_can in ["1","2"]:
                        break     
                    else:
                        print("ERROR: Debe ingresar una de las opciones.")
                        continue
                        
                while True:
                            Nombre=input("Ingrese su Nombre: ").strip().title()
                            if Nombre!="" and Nombre.replace(" ","").isalpha():
                               
                                break
                            print("ERROR: Debe ingresar un nombre, el cúal solo debe tener letras")
                           
                match Dia_can:
                    case "1":
                        print("Trunos del Día lunes")
                        
                        if Nombre==Lunes1:
                            print("*"*10,"CANCELANDO TURNO","*"*10)
                            Lunes1=""
                            print("TURNO CANCELADO")
                        elif Nombre==Lunes2:
                            print("*"*10,"CANCELANDO TURNO","*"*10)
                            Lunes2=""
                            print("TURNO CANCELADO")
                        elif Nombre==Lunes3:
                            print("*"*10,"CANCELANDO TURNO","*"*10)
                            Lunes3=""
                            print("TURNO CANCELADO")
                        elif Nombre==Lunes4:
                            print("*"*10,"CANCELANDO TURNO","*"*10)
                            Lunes4=""
                            print("TURNO CANCELADO")
                        else:
                            print("Su nombre no tiene ningún turno asignado para cancelar")
                    case "2":
                        if Nombre==Martes1:
                            print("*"*10,"CANCELANDO TURNO","*"*10)
                            Martes1=""
                            print("TURNO CANCELADO")
                        elif Nombre==Martes2:
                            print("*"*10,"CANCELANDO TURNO","*"*10)
                            Martes2=""
                            print("TURNO CANCELADO")
                        elif Nombre==Martes3:
                            print("*"*10,"CANCELANDO TURNO","*"*10)
                            Martes3=""
                            print("TURNO CANCELADO")
                        else:
                            print("Su nombre no tiene ningún turno asignado para cancelar")
            case "3":
                print("\nAGENDA DEL DÍA LUNES")
                print(f"TURNO 1: {Lunes1 if Lunes1!="" else 'Libre' }")
                print(f"TURNO 2: {Lunes2 if Lunes2!="" else 'Libre' }")
                print(f"TURNO 3: {Lunes3 if Lunes3!="" else 'Libre' }")
                print(f"TURNO 4: {Lunes4 if Lunes4!="" else 'Libre' }\n")
                print("AGENDA DEL DÍA MARTES\n")
                print(f"TURNO 1: {Martes1 if Martes1!="" else 'Libre' }")
                print(f"TURNO 2: {Martes2 if Martes2!="" else 'Libre' }")
                print(f"TURNO 3: {Martes3 if Martes3!="" else 'Libre' }\n")
            case "4":
                lunes_turnos_oc=0
                martes_turnos_oc=0
                print("RESUMEN GENERAL: ")
                print("\n Lunes: ")
                if Lunes1!="":
                    lunes_turnos_oc+=1
                if Lunes2!="":
                    lunes_turnos_oc+=1
                if Lunes3!="":
                    lunes_turnos_oc+=1
                if Lunes4!="":
                    lunes_turnos_oc+=1
                Turnos_Lunes=4-lunes_turnos_oc
                print(f" El día lunes cuenta con: {Turnos_Lunes} turnos disponibles")
                print("\n Martes: ")
                if Martes1!="":
                    martes_turnos_oc+=1
                if Martes2!="":
                    martes_turnos_oc+=1
                if Martes3!="":
                    martes_turnos_oc+=1
                Turnos_Martes=3-martes_turnos_oc
                print(f" El día martes cuenta con: {Turnos_Martes} turnos disponibles")
                if lunes_turnos_oc>martes_turnos_oc:
                    print("\nEl día lunes tiene más turnos ocupados que el día martes")
                elif martes_turnos_oc>lunes_turnos_oc:
                    print("\nEl día martes tiene más turnos ocpuados que el día lunes")
                else:
                    print("\nAmbos días tienen la misma cantidad de días ocupados ")
            case "5":
                print("CERRNADO SISTEMA")
                activa=False
ejercicio3()