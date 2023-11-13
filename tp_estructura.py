import funciones.funciones_auxiliares as fa
import funciones.funciones_log_in_y_sign_in as flisi
import funciones.menu_cliente as menu_cliente
import funciones.menu_administrativo as menu_administrativo
import funciones.menu_limpieza as menu_limpieza
import funciones.menu_mantenimiento as menu_mantenimiento
import funciones.menu_administrador as menu_administrador

if __name__ == '__main__':
    lista_clientes = fa.download_clientes()
    lista_administrativo, lista_mantenimiento, lista_limpieza = fa.download_personal()
    hotel = fa.download_hotel(lista_clientes)
    
    while True:
        ingreso = input('''Elija una opcion:
                    a. Log In
                    b. Sign In
                    c. Cerrar programa
                    
                    ''').lower().strip()
        
        match ingreso:
            case 'a':
                usuario = flisi.log_in(lista_clientes, lista_administrativo, lista_mantenimiento, lista_limpieza, hotel)
                if usuario != None:
                    match usuario.tipo_usuario:
                        case 'Cliente':
                            menu_cliente.menu_cliente(usuario, hotel)
                        case 'Administrativo':
                            menu_administrativo.menu_administrativo(usuario, hotel, lista_clientes, lista_mantenimiento, lista_limpieza)
                        case 'Mantenimiento':
                            menu_mantenimiento.menu_mantenimiento(usuario)
                        case 'Limpieza':
                            menu_limpieza.menu_limpieza(usuario)
                        case 'Administrador':
                            menu_administrador.menu_administrador(usuario, hotel, lista_administrativo, lista_clientes)
                pass
            
            case 'b':
                # Solo el cliente puede realizar un sign in 'por su cuenta'. Los empleados requieren que un personal superior les haga el sign in.
                flisi.sign_in_cliente(lista_clientes)
            
            case 'c':
                fa.load_hotel(hotel)
                fa.load_clientes(lista_clientes)
                fa.load_personal(lista_administrativo, lista_mantenimiento, lista_limpieza)
                print('La carga de archivos al sistema fue exitosa.')
                break
            case _:
                print('Por favor elija una de las opciones (a | b | c)')