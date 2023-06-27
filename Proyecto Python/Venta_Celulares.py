Proyecto venta de celulares

Aca mostramos el drive del video

https://drive.google.com/file/d/11z2OyAKI5nrTi7t_Bg2-Wr5WeQ7icMN6/view?usp=drive_link

Copiamos el codigo 

# Llamamos al procedimiento de menu principal, desde nuestro proceso principal.
# 	menuPrincipal();

def menuPrincipal():
    opcion = 0

    # La variable "opcion" determina la marca de celular seleccionada
    # Utilizamos un bucle "while" para asegurarnos de que se ingresen opciones validas

    while opcion < 1 or opcion > 3:
        # Mostramos el menú principal con las opciones de marca.
        print("╔═════════════════════════════════════════╗")
        print("║                                                                                          ║")
        print("║                     ***OMEGA CELULARES***                         ║")
        print("║                                                                                          ║")
        print("║        1. SAMSUNG                             2. MOTOROLA      ║")
        print("║                                                                                          ║")
        print("║                                     3. SALIR                                       ║")
        print("║                                                                                          ║")
        print("╚═════════════════════════════════════════╝")
        print("")
        opcion = int(input("Digite una opción: "))
        print("")

        # Utilizamos una estructura "if-elif-else" para seleccionar una marca o salir del programa si es necesario.

        if opcion == 1:
            menuSamsung(opcion)
        elif opcion == 2:
            menuMotorola(opcion)
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción incorrecta, digite nuevamente:")

    return


# La función "menuSamsung" muestra y gestiona el menú para la marca Samsung.

def menuSamsung(opcion):
    opcion1 = 0
    opcion2 = 0

    # Utilizamos un bucle "while" para asegurarnos de que se ingresen opciones válidas.

    while opcion1 < 1 or opcion1 > 3:
        # Mostramos el menú de Samsung con las opciones de modelo.
        print("╔═════════════════════════════════════════╗")
        print("")
        print("                            ***MENU SAMSUNG***")
        print("")
        print("                          1. Samsung Galaxy A23")
        print("                          2. Samsung Galaxy A54 5G")
        print("                                         3. Salir")
        print("")
        print("╚═════════════════════════════════════════╝")
        print("")
        opcion1 = int(input("Digite una opción: "))
        print("")

        if opcion1 == 1:
            # Mostramos el menú y gestionamos las opciones para el modelo Samsung seleccionado.
            print("╔═════════════════════════════════════════╗")
            print("")
            print("                         Samsung Galaxy A23")
            print("                            Precio: $132.799")
            print("                                1. Comprar")
            print("                          2. Ver características")
            print("")
            print("╚═════════════════════════════════════════╝")
            print("")

            while opcion2 < 1 or opcion2 > 2:
                opcion2 = int(input("Digite una opción: "))
                print("")

                if opcion2 == 1:
                    metodoPago(opcion1, opcion)
                elif opcion2 == 2:
                    caracteristicas(opcion1, opcion)
                else:
                    print("Opción incorrecta, digite nuevamente")
            opcion2 = 0

        elif opcion1 == 2:
            print("╔═════════════════════════════════════════╗")
            print("")
            print("                        Samsung Galaxy A54 5G")
            print("                             Precio: $209.999")
            print("                                 1. Comprar")
            print("                          2. Ver características")
            print("")
            print("╚═════════════════════════════════════════╝")
            print("")

            while opcion2 < 1 or opcion2 > 2:
                opcion2 = int(input("Digite una opción: "))
                print("")

                if opcion2 == 1:
                    metodoPago(opcion1, opcion)
                elif opcion2 == 2:
                    caracteristicas(opcion1, opcion)
                else:
                    print("Opción incorrecta, digite nuevamente")
            opcion2 = 0

        else:
            print("Opción incorrecta, digite nuevamente")
            print("")

    return


# La función "menuMotorola" muestra y gestiona el menú para la marca Motorola.

def menuMotorola(opcion):
    opcion1 = 0
    opcion2 = 0

    # Utilizamos un bucle "while" para asegurarnos de que se ingresen opciones válidas

    while opcion1 < 1 or opcion1 > 3:
        # Mostramos el menú de Motorola con las opciones de modelo
        print("╔═════════════════════════════════════════╗")
        print("")
        print("                       ***MENU MOTOROLA***")
        print("")
        print("                  1. Motorola Edge 30 Fusion 5G")
        print("                         2. Motorola Moto G52")
        print("                                   3. Salir")
        print("")
        print("╚═════════════════════════════════════════╝")
        print("")
        opcion1 = int(input("Digite una opción: "))
        print("")

        if opcion1 == 1:
            # Mostramos el menú y gestionamos las opciones para el modelo Motorola seleccionado.
            print("╔═════════════════════════════════════════╗")
            print("")
            print("                     Motorola Edge 30 Fusion 5G")
            print("                             Precio: $249.999")
            print("                                1. Comprar")
            print("                          2. Ver características")
            print("")
            print("╚═════════════════════════════════════════╝")
            print("")

            while opcion2 < 1 or opcion2 > 2:
                opcion2 = int(input("Digite una opción: "))
                print("")

                if opcion2 == 1:
                    metodoPago(opcion1, opcion)
                elif opcion2 == 2:
                    caracteristicas(opcion1, opcion)
                else:
                    print("Opción incorrecta, digite nuevamente")
            opcion2 = 0

        elif opcion1 == 2:
            print("╔═════════════════════════════════════════╗")
            print("")
            print("                         Motorola Moto G52")
            print("                             Precio: $99.999")
            print("                              1. Comprar")
            print("                        2. Ver características")
            print("")
            print("╚═════════════════════════════════════════╝")
            print("")

            while opcion2 < 1 or opcion2 > 2:
                opcion2 = int(input("Digite una opción: "))
                print("")

                if opcion2 == 1:
                    metodoPago(opcion1, opcion)
                elif opcion2 == 2:
                    caracteristicas(opcion1, opcion)
                else:
                    print("Opción incorrecta, digite nuevamente")
            opcion2 = 0

        else:
            print("Opción incorrecta, digite nuevamente")
            print("")

    return


# Función para realizar el método de pago
# Luego de cada opcion de pago se finaliza el programa  y se cierra, con un
#  mensaje final .  "Gracias por la compra"

def metodoPago(opcion1, opcion):
    opcion3 = 0

    while opcion3 < 1 or opcion3 > 3:
        print("╔═════════════════════════════════════════╗")
        print("")
        print("                           ***MÉTODO DE PAGO***")
        print("")
        print("   Seleccione una opcion: ")
        print("")
        print("              1. Mercado Pago (15% de descuento)")
        print("              2. Tarjeta de débito (10% de descuento)")
        print("              3. Tarjeta de crédito (6/12 cuotas sin interés)")
        print("              4. Volver al menú anterior")
        print("")
        print("╚═════════════════════════════════════════╝")
        print("")

        opcion3 = int(input("Digite una opción: "))
        print("")

        if opcion3 == 1:
            precio = 0

            if opcion == 1:
                if opcion1 == 1:
                    precio = 132799
                elif opcion1 == 2:
                    precio = 209999
            elif opcion == 2:
                if opcion1 == 1:
                    precio = 249999
                elif opcion1 == 2:
                    precio = 99999

            descuento = precio * 0.15
            precio_final = precio - descuento

            print("El precio con descuento del 15% es: $", "{:.2f}".format(precio_final))
            print("")
            print("¡Gracias por su compra!")

        elif opcion3 == 2:
            precio = 0

            if opcion == 1:
                if opcion1 == 1:
                    precio = 132799
                elif opcion1 == 2:
                    precio = 209999
            elif opcion == 2:
                if opcion1 == 1:
                    precio = 249999
                elif opcion1 == 2:
                    precio = 99999

            descuento = precio * 0.10
            precio_final = precio - descuento

            print("El precio con descuento del 10% es: $", "{:.2f}".format(precio_final))
            print("")
            print("¡Gracias por su compra!")

        elif opcion3 == 3:
            precio = 0

            if opcion == 1:
                if opcion1 == 1:
                    precio = 132799
                elif opcion1 == 2:
                    precio = 209999
            elif opcion == 2:
                if opcion1 == 1:
                    precio = 249999
                elif opcion1 == 2:
                    precio = 99999

            print("╔═════════════════════════════════════════╗")
            print("")
            print("                       1. 6 cuotas sin interés")
            print("                       2. 12 cuotas sin interés")
            print("")
            cuotas = int(input("Digite una opción: "))
            print("")
            print("╚═════════════════════════════════════════╝")
            print("")

            if cuotas == 1:
                monto_cuota = precio / 6
                print("El monto de cada cuota es: $", "{:.2f}".format(monto_cuota))
                print("")
                print("¡Gracias por su compra!")
            elif cuotas == 2:
                monto_cuota = precio / 12
                print("El monto de cada cuota es: $", "{:.2f}".format(monto_cuota))
                print("")
                print("¡Gracias por su compra!")
            else:
                print("Opción incorrecta, volviendo al menú principal")
                print("")

        elif opcion3 == 4:
            if opcion == 1:
                menuSamsung(opcion)
            elif opcion == 2:
                menuMotorola(opcion)

        else:
            print("Opción incorrecta, volviendo al menú principal")
            print("")
            print("¡Gracias por su compra!")

        return


# Subproceso correspondiente a las características de nuestros celulares

def caracteristicas(opcion1, opcion):
    opcion3 = 0
    matriz = [
        [  # Caracteristicas Samsung
            "Pantalla: 6.6 1080x2400 PX PLS TFT, Procesador: Qualcomm SM6225 8 núcleos 2.4 Ghz, "
            "RAM: 4GB, Almacenamiento: 128GB, "
            "Cámara: 50 MP + 5 MP + 2 MP + 2 MP, Batería: 5000 mAh, OS: Android 12, Perfil: 8.4mm, "
            "Peso: 195g"
        ],
        [
            "Pantalla: 6.4 1080x2400 PX Super Amoled, Procesador: Exynos 1380 8 núcleos 2.4GHz, "
            "RAM: 8GB, Almacenamiento: 128GB, Camara: 50 MP + 12 MP + 5 MP, Batería: 5000 mAh, "
            "OS: Android 13, Perfil: 8.2mm, Peso: 202g"
        ],
        [  # Caracteristicas Motorola
            "Pantalla: 6.5 1080x2400 PX P-OLED, Procesador: Qualcomm Snapdragon 888+, "
            "RAM: 12GB, Almacenamiento: 256GB,"
            "Camara: 50 MP + 13 MP + 2 MP, Bateria: 4400 mAh, OS: Android 12, Perfil: 7.0mm, Peso: 175g"
        ],
        [
            "Pantalla: 6.5 1080x2400 PX P-OLED, Procesador: Qualcomm Snapdragon 680 8 núcleos 2.4 Ghz, "
            "RAM: 6GB, Almacenamiento: 128GB,"
            "Camara: 50 MP + 8 MP + 2 MP, Batería: 5000 mAh, OS: Android 12, Perfil: 7.9mm, Peso: 169g"
        ]
    ]

    # Condicional múltiple anidado para mostrar las características del modelo seleccionado

    if opcion == 1:
        caracteristicas_samsung = matriz[opcion1 - 1][0].split(", ")
        for caracteristica in caracteristicas_samsung:
            print(caracteristica)

    elif opcion == 2:
        caracteristicas_motorola = matriz[opcion1 - 1][0].split(", ")
        for caracteristica in caracteristicas_motorola:
            print(caracteristica)

    print("")
    print("╔═════════════════════════════════════════╗")
    print("")
    print("                                  1. Comprar")
    print("                       2. Volver al menú anterior")
    print("                       3. Volver al menú principal")
    print("")
    print("╚═════════════════════════════════════════╝")
    print("")

    # Estructura "while" para que se digiten las opciones correctas
    # o se vuelva a los menues anteriores

    while opcion3 < 1 or opcion3 > 3:
        opcion3 = int(input("Digite una opción: "))
        print("")

        if opcion == 1:
            if opcion3 == 1:
                metodoPago(opcion1, opcion)
            elif opcion3 == 2:
                menuSamsung(opcion)
            elif opcion3 == 3:
                menuPrincipal()
            else:
                print("Opción incorrecta, digite nuevamente")

        elif opcion == 2:
            if opcion3 == 1:
                metodoPago(opcion1, opcion)
            elif opcion3 == 2:
                menuMotorola(opcion)
            elif opcion3 == 3:
                menuPrincipal()
            else:
                print("Opción incorrecta, digite nuevamente")

    return


menuPrincipal()
