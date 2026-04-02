def ejercicio1():
    activa=True
    #Caja del Kiosco
    print("--CAJA--")
    while activa:
        total_desc=0
        total_no_desc=0
        while True:
            Nombre=input("Ingrese su Nombre: ").title().strip()
            if Nombre=="":
                print("¡EL NOMBRE NO PUEDE ESTAR VACÍO!. Intente nuevamente.")
                continue
            elif not Nombre.replace(" ","").isalpha():
                print("!EL NOMBRE DEBE CONTENER SOLO LETRAS¡")
                continue
            break
        while True:
            Productos=input("Ingrese la cantidad de Productos a Comprar: ").strip()
            if Productos=="":
                print("!Ingrese una cantidad¡")
                continue
            elif not Productos.replace(" ","").isdigit():
                print("!DEBE INGRESAR SOLO NÚMEROS ENTEROS Y DEBEN SER POSITIVOS¡")
                continue
            if Productos=="0":
                print("INGRESE CANTIDADES MAYORES A CERO")
                continue
            for i in range(int(Productos)):
                while True:
                    Precio=input(f"Producto {i+1} - Precio:").strip()
                    if Precio=="":
                        print("NO PUEDE ESTAR VACÍO")
                        continue
                    elif Precio=="0":
                        print("EL PRECIO DEBESER MAYOR QUE CERO")
                        continue
                    if not Precio.replace(" ","").isdigit():
                        print("ERROR, INGRESE PRECIO VÁLIDO ('ENTERO Y POSITIVO')") #Podria agregar para corroborar decimales
                        continue
                    Precio=int(Precio)
                    total_no_desc+=Precio
                    break
                while True:
                    Descuento=input("¿Tiene Descuento? (S/N): ").strip().lower()
                    if Descuento=="":
                        print("NO PUEDE ESTAR VACÍO")
                        continue
                    if Descuento not in["s","n"]:
                        print("DEBE INGRESAR: 'S' o 'N'")
                        continue
                    else:
                        if Descuento=="s":
                            Precio_Final=Precio*0.90
                        else:
                            Precio_Final=Precio 
                    break
                total_desc+=Precio_Final
            break
        Ahorro=total_no_desc-total_desc
        Promedio=float(total_desc/int(Productos))
        print()
        print(f"Cliente:{Nombre}")
        print(f"Cantidad De Porductos: {Productos}")
        print()
        print(f"Total sin descuentos: ${total_no_desc}")
        print(f"Total con descuentos: ${total_desc:.2f}")
        print(f"Ahorro Total: ${Ahorro:.2f}")
        print(f"Promedio Por Producto: ${Promedio:.2f}")
        activa=False