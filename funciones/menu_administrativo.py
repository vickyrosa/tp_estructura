def menu_administrativo():
    opcion = input(''' Elija una opcion:
                    a. Dar de baja personal
                    b. Asignar tarea
                    c. BOTON PRUEBA
                    
                    ''')
    match opcion:
        case 'a':
            pass
        case 'b':
            pass
        case 'c':
            print('Entro a Administrativo')
        case _:
            print('Porfavor elija una de las opciones (a | b | c)')