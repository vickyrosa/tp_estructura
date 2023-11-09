def menu_administrativo(administrativo, hotel, lista_clientes):
    while True:
        opcion = input(''' Elija una opcion:
                        a. Dar de baja personal
                        b. Asignar tarea
                        c. Buscar resrvas de un cliente
                        d. Log out
                        
                        ''')
        match opcion:
            case 'a':
                administrativo.despedir_personal()
            case 'b':
                pass
            case 'c':
                administrativo.mostrar_reservas_cliente(hotel, lista_clientes)
            case 'd':
                break
            case _:
                print('Porfavor elija una de las opciones (a | b | c)')