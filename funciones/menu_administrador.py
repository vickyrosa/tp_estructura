def menu_administrador(administrador, hotel, lista_administrativo, lista_clientes):
    while True:
        opcion = input('''Elija una opcion:
                    a. Ver porcentaje ocupacion del dia
                    b. Ver porcentaje ocupacion del dia por tipo de habitacion
                    c. Ver cantidad de clientes por tipo
                    d. Ver ingresos
                    e. Dar de alta un administrativo
                    f. Dar de baja un administrativo
                    g. Cambiar contrasena
                    h. Log out
                    
                    ''').strip().lower()
        match opcion:
            case 'a':
                administrador.porcentaje_ocupacion(hotel)
            case 'b':
                administrador.porcentaje_ocupacion_portipo(hotel)
            case "c":
                administrador.cant_clientes_por_tipo(lista_clientes)
            case 'd':
                administrador.buscar_recaudacion(hotel)
            case 'e':
                administrador.sign_in_administrativo(lista_administrativo)
            case 'f':
                administrador.despedir_administrativo(lista_administrativo)
            case 'g':
                administrador.cambiar_contra()
            case 'h':
                break
            case _:
                print('Por favor elija una de las opciones ( a | b | c | d | e | f | g | h )')