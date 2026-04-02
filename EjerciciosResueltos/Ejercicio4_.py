def ejercicio4():
    '''ESCAPE ROOM: LA BÓVEDA
    Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo 
    limitados. 
    Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás'''
    energia=100
    tiempo=12
    cerraduras_abiertas=0
    alarma=False
    codigo_parcial=""
    forzar_cerradura=0
    while True:
            Nombre=input("Ingrese su nombre: ").title().strip()
            if Nombre.replace(" ","").isalpha():
                print("Nombre del agente guardado.")
                break
            else:
                print("ERROR: Debe ingresar un nombre y no debe contener  números.")
                continue
    while energia>0 and tiempo>0 and cerraduras_abiertas<3:
        if alarma==True and tiempo<=3:
            
            break
        
        print("--MENÚ--\n"
        "[1] FORZAR CERRADURA\n" \
        "[2] HACKEAR PANEL\n" \
        "[3] DESCANSAR\n")
        
        while True:
            Op=input("Seleccione un opción del menú: ").strip()
            if Op.isdigit() and Op in ["1","2","3"]:
                print(f"Se selecciono la opción {Op}")
                break
            else:
                print("!ADVERTENCIA¡: Debe ingresar una de las opciones del menú ")
                continue
        match Op:
             case "1":
                forzar_cerradura+=1
                energia-=20
                tiempo  -=2
                if forzar_cerradura==3:
                    print("¡SE TRABÓ LA CERRADURA!")
                    alarma=True
                else:
                 if energia<40:
                    print("CUIDADO: Hay riesgo de alarma")
                    while True:
                        Numero=input("Elija un número del 1 al 3: ").strip()
                        if  Numero not in["1","2","3"]:
                         print("ERROR: Debe ingresar un número, del 1 al 3.")
                         continue
                        else:
                            print("PROCESANDO ELECCIÓN.......")
                            
                            if Numero=="3":
                               alarma=True
                               print("SE ACTIVÓ LA ALARMA")     
                            else:
                                print("Abriendo cerradura....")
                                cerraduras_abiertas+=1    
                            break
                 else:
                   print("Abriendo cerradura........")
                   cerraduras_abiertas+=1
             case "2":
                forzar_cerradura=0
                energia-=10
                tiempo-=3
                print("HACKEANDO PANEL......")
                for pasos in range(4):
                   while True:
                       letra=input(f"Pasos: {pasos}/4--Ingrese una letra al código: ").strip()
                       if letra.isalpha() and len(letra)==1:
                        codigo_parcial+=letra
                        break
                       else:
                           print("AGENTE SOLO PUEDES INGRESAR UNA LETRA POR PASO")
                   print(f"DESCIFRANDO CÓDIGO......: {codigo_parcial}")
                if len(codigo_parcial)>=8 and cerraduras_abiertas<3:
                    print("ABRIENDO CERRADURA....")
                    codigo_parcial=""
                    cerraduras_abiertas+=1
                else:
                    print(f"Faltan {8-len(codigo_parcial)} letras para que se abra una cerradura agente.")
             case "3":
                forzar_cerradura=0
                print("DESCANSANDO.....")
                if alarma==True:
                    tiempo-=1
                    energia+=5
                else:
                    energia+=15
                    tiempo-=1
                if energia>100:
                    energia=100
                    print("EL AGENTE ESTA RECUPERADO AL 100")
    
           
    if cerraduras_abiertas==3:
            print("EL AGENTE CUMPLIÓ SU MISIÓN")
    elif alarma==True and tiempo<=3:
            print("EL AGENTE FUÉ CAPTURADO...")
    elif energia<=0 or tiempo<=0:
            print("EL AGENTE FUÉ CAPTURADO...")
ejercicio4()