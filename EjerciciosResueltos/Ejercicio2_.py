def ejercicio2():
    '''EJERCICIO 2: Acceso al Campus y Menú Seguro'''
    contador=3
    Usuario_correcto="alumno"
    Clave_correcta="python123"
    cerrar=True
    while contador>0:
        Usuario=input("Igresar nombre de Usuario: ")
        Contraseña=input("Ingrese su contraseña: ")
        if Contraseña!=Clave_correcta or Usuario!=Usuario_correcto:
            print("Contraseña o Usuario !INCORRECTO¡")
            contador-=1
            continue
        while True:
            print("\n[1] VER ESTADO DE INSCRIPCIÓN\n" \
            "[2] CAMBIAR CLAVE\n" \
            "[3] MOSTRAR MENSAJE MOTIVACIONAL\n" \
            "[4] SALIR\n")
            Eleccion=input("Ingrese el número de la opción que desee: ").strip()
            if not Eleccion.isdigit():
                print("ERROR: DEBE INGRESAR UN NÚMERO")
                continue
            if Eleccion=="" or Eleccion not in["1","2","3","4"]:
                print("¡ERROR! DEBE INGRESAR UNA DE LAS OPCIONES")
                continue
            match Eleccion:
                case "1":
                    print("'Inscripto'")
                case "2":
                    print("-CAMBIO DE CLAVE-")
                    cambio=True
                    while cambio:
                        Clave_Nueva=input("Ingrese su Nueva clave: ")
                        if input("Confirme la clave: ")!=Clave_Nueva:
                            print("Las claves deben coincidir")
                            continue
                        elif len(Clave_Nueva)<6:
                            print("LA CALVE DEBE SER DE 6 CARACTERES O MÁS")
                            continue
                        else:
                            print("Los cambios se realizaron correctamente")
                            cambio=False
                            #esta parte se podria mejorar permitiendo el uso de la nueva contraseña, guardandola
                case "3":
                    print("Para vos, Frase motivacional del día:\n")
                    print("'TENES QUE SER COMO JHON SNOW Y SEGUIR PARA ADELANTE'")
                case "4":
                    print("CERRANDO","-"*30)
                    break
        if cerrar:
            break
        
    else:
        print("CUENTA BLOQUEDA")
ejercicio2()