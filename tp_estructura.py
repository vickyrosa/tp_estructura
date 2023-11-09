# ACLARACION: Usar txt, pero las cosas separadas por comas como si fuera un csv (onda el del parcial)
import funciones.funciones_auxiliares as fa
import funciones.funciones_log_in_y_sign_in as flisi
import funciones.menu_cliente as menu_cliente
import funciones.menu_administrativo as menu_administrativo
import funciones.menu_limpieza as menu_limpieza
import funciones.menu_mantenimiento as menu_mantenimiento
import funciones.menu_administrador as menu_administrador
import datetime

if __name__ == '__main__':
    lista_clientes = fa.download_clientes()
    lista_administrativo, lista_mantenimiento, lista_limpieza = fa.download_personal()
    hotel = fa.download_hotel(lista_clientes)
    
    while True:
        ingreso = input('''Elija una opcion:
                    a. Log In
                    b. Sign In
                    c. Cerrar programa
                    
                    ''').lower()
        
        match ingreso:
            case 'a':
                usuario = flisi.log_in(lista_clientes, lista_administrativo, lista_mantenimiento, lista_limpieza, hotel)
                if usuario != None:
                    match usuario.tipo_usuario:
                        case 'Cliente':
                            menu_cliente.menu_cliente(usuario, hotel)
                        case 'Administrativo':
                            menu_administrativo.menu_administrativo(usuario, hotel, lista_clientes)
                        case 'Mantenimiento':
                            print('Entro a Mantenimiento')
                        case 'Limpieza':
                            print('Entro a limpieza')
                        case 'Administrador':
                            menu_administrador.menu_administrador(usuario, hotel, lista_administrativo)
                pass
            
            case 'b':
                while True:
                    tipo_usuario = input('''Elija una opcion:
                    a. Cliente
                    b. Personal del hotel
                    c. Volver atrás
                    
                    ''').lower()
                    match tipo_usuario:
                        case 'a':
                            flisi.sign_in_cliente(lista_clientes)
                            break
                        case 'b':
                            while True:
                                tipo_personal = input('''Elija una opcion:
                    a. Administrativo
                    b. Mantenimiento
                    c. Limpieza
                    d. Volver atrás
                    
                    ''').lower()
                                match tipo_personal:
                                    case 'a':
                                        flisi.sign_in_administrativo(lista_administrativo)
                                        # Este volver atras = False, es para que si el usuario en algun momento toco volver atras, no se guarde
                                        # el valor de esa variable y al crear el usuario, vuelva al menu principal.
                                        volver_atras = False
                                        break
                                    case 'b':
                                        flisi.sign_in_mantenimiento(lista_mantenimiento)
                                        volver_atras = False
                                        break
                                    case 'c':
                                        flisi.sign_in_limpieza(lista_limpieza)
                                        volver_atras = False
                                        break
                                    case 'd':
                                        # Ponemos este bool aca para que si quiere volver atras no haga break y vuelva al login, sino que le aparezcan las opciones del menu anterior
                                        volver_atras = True
                                        break
                                    case _:
                                        print('Porfavor elija una de las opciones (a | b | c | d)')
                        case 'c':
                            break
                        case _:
                            print('Porfavor elija una de las opciones (a | b | c)')
                            volver_atras = True
                    if volver_atras:
                        pass
                    else:
                        break
            case 'c':
                fa.load_hotel(hotel)
                fa.load_clientes(lista_clientes)
                fa.load_personal(lista_administrativo, lista_mantenimiento, lista_limpieza)
                print('La carga de archivos al sistema fue exitosa.')
                break
            case _:
                print('Porfavor elija una de las opciones (a | b | c)')