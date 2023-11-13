def menu_cliente(cliente, hotel):
    while True:
        opcion = input('''Elija una opcion:
                    a. Reservar una habitacion
                    b. Cancelar reserva
                    c. Ver mis reservas
                    d. Pedir del buffet
                    e. Ver mi categoria
                    f. Cambiar contraseña
                    g. Log out
                        
                    ''')
        match opcion:
            case 'a':
                cliente.reservar(hotel)
            case 'b':
                cliente.cancelar_reserva(hotel)
            case 'c':
                print('Ver reservas!')
                #cliente.ver_mis_reservas(hotel)
            case 'd':
                cliente.ordenar_del_buffet(hotel)
            case 'e':
                cliente.ver_categoria()
            case 'f':
                cliente.cambiar_contra()
            case 'g':
                break
            case _:
                print('Por favor elija una de las opciones (a | b | c | d | e | f)')
    