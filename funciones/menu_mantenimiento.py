def menu_mantenimiento(mantenimiento):
    while True:
        opcion = input('''Elija una opcion:
                    a. Fichar Ingreso
                    b. Fichar Egreso
                    c. Finalizar Tarea
                    d. Cambiar contrasena
                    e. Log out
                        
                    ''').lower().strip()
        match opcion:
            case 'a':
                mantenimiento.fichar_ingreso()
            case 'b':
                mantenimiento.fichar_egreso()
            case 'c':
                mantenimiento.finalizar_tarea()
            case 'd':
                mantenimiento.cambiar_contra()
            case 'e':
                break
            case _:
                print('Porfavor elija una de las opciones (a | b | c | d | e)')