def menu_administrador(administrador, hotel, lista_administrativo):
    while True:
        opcion = input('''Elija una opcion:
                    a. Ver porcentaje ocupacion del dia
                    b. Ver porcentaje ocupacion del dia por tipo de habitacion
                    c. Dar de alta un administrativo
                    d. Dar de baja un administrativo
                    e. Cambiar contrasena
                    f. Log out
                    
                    ''')
        match opcion:
            case 'a':
                # NO ENTIENDO XQ SALTA ERROR, DICE QUE LE PASO DOS ARGUMENTO CDO CLARAMENTE LE TOY PASANDO UNO SOLO
                # Puse el print este para que se vea que administrador y hotel se pasan bien como objetos

                #creo que no se estan importando bien los archivos que te dicen el porcentaje.
                administrador.porcentaje_ocupacion(hotel)
            case 'b':
                administrador.porcentaje_ocupacion_portipo(hotel)
            case 'c':
                administrador.sign_in_administrativo(lista_administrativo)
            case 'd':
                administrador.despedir_administrativo(lista_administrativo)
            case 'e':
                administrador.cambiar_contra()
            case 'f':
                break
            case _:
                print('Por favor elija una de las opciones ( a | b | c | d | e | f )')
