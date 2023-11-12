def menu_administrador(administrador, hotel, lista_administrativo):
    while True:
        opcion = input('''Elija una opcion:
                    a. Ver porcentaje ocupacion del dia
                    b. Ver porcentaje ocupacion del dia por tipo de habitacion
                    c. Ver ingresos
                    d. Dar de alta un administrativo
                    e. Dar de baja un administrativo
                    f. Cambiar contrasena
                    g. Log out
                    
                    ''')
        match opcion:
            case 'a':
                administrador.porcentaje_ocupacion(hotel)
            case 'b':
                administrador.porcentaje_ocupacion_portipo(hotel)
            case "c":
                administrador.buscar_recaudacion()
            case 'd':
                administrador.sign_in_administrativo(lista_administrativo)
            case 'e':
                administrador.despedir_administrativo(lista_administrativo)
            case 'f':
                administrador.cambiar_contra()
            case 'g':
                break
            case _:
                print('Por favor elija una de las opciones ( a | b | c | d | e | f | g )')