def menu_cliente(cliente, hotel):
    while True:
        opcion = input('''Elija una opcion:
                    a. Reservar una habitacion
                    b. Cancelar reserva
                    c. Pedir del buffet
                    d. Ver mi categoria
                    e. Cambiar contraseña
                    f. Log out
                        
                    ''')
        match opcion:
            case 'a':
                cliente.reservar(hotel)
            case 'b':
                print('NO ESTA HECHO!!!')
            case 'c':
                cliente.ordenar_del_buffet()
            case 'd':
                cliente.ver_categoria()
            case 'e':
                cliente.cambiar_contra()
            case 'f':
                break
            case _:
                print('Por favor elija una de las opciones (a | b | c | d | e | f)')
    