def menu_limpieza(limpieza):
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
                limpieza.fichar_ingreso()
            case 'b':
                limpieza.fichar_egreso()
            case 'c':
                limpieza.finalizar_tarea()
            case 'd':
                limpieza.cambiar_contra()
            case 'e':
                break
            case _:
                print('Porfavor elija una de las opciones (a | b | c | d | e)')