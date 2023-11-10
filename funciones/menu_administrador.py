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
