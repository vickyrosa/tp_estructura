def menu_administrativo(administrativo, hotel, lista_clientes, lista_mantenimiento, lista_limpieza):
    while True:
        opcion = input('''Elija una opcion:
                    a. Dar de alta personal
                    b. Dar de baja personal
                    c. Asignar tarea
                    d. Cancelar tarea
                    e. Buscar reservas de un cliente
                    f. Cambiar contrasena
                    g. Log out
                        
                    ''').lower().strip()
        match opcion:
            case 'a':
                while True:
                    tipo_usuario = input('''Que usuario creara:
                    a. Mantenimiento
                    b. Limpieza
                    c. Volver atras                                    
                                        
                    ''').lower().strip()
                    match tipo_usuario:
                        case 'a':
                            administrativo.sign_in_mantenimiento(lista_mantenimiento)
                        case 'b':
                            administrativo.sign_in_limpieza(lista_limpieza)
                        case 'c':
                            break
                        case _:
                            print('Porfavor elija una de las opciones (a | b | c)')
                
            case 'b':
                administrativo.despedir_personal(lista_mantenimiento, lista_limpieza)
            case 'c':
                administrativo.encargar_tareas(lista_mantenimiento, lista_limpieza)
            case 'd':
                administrativo.cancelar_tarea(lista_mantenimiento, lista_limpieza)
            case 'e':
                administrativo.mostrar_reservas_cliente(hotel, lista_clientes)
            case 'f':
                administrativo.cambiar_contra()
            case 'g':
                break
            case _:
                print('Porfavor elija una de las opciones (a | b | c | d | e | f | g )')