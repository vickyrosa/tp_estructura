# ACLARACION: Usar txt, pero las cosas separadas por comas como si fuera un csv (onda el del parcial)
from hotel.habitacion import Habitacion
from usuario.cliente import Cliente
from hotel.buffet import Buffet
from hotel.hotel import Hotel
from hotel.reservas import Reserva
from hotel.lista_reservas import Lista_Reservas
import funciones.funciones_auxiliares as fa
import funciones.menu_cliente as menu_cliente
import datetime

if __name__ == '__main__':
    lista_clientes = fa.load_clientes()
    lista_administrativo, lista_mantenimiento, lista_limpieza = fa.load_personal()
    fa.load_hotel()
    
    while True:
        ingreso = input('''Elija una opcion:
                    a. Log In
                    b. Sign In
                    c. Cerrar programa
                    
                    ''')
        
        match ingreso:
            case 'a':
                usuario = fa.log_in(lista_clientes, lista_administrativo, lista_mantenimiento, lista_limpieza)
                match usuario.tipo_usuario:
                    case 'Cliente':
                        menu_cliente.menu_cliente(usuario)
                    case 'Administrativo':
                        print('Entro a admin')
                    case 'Mantenimiento':
                        print('Entro a Mantenimiento')
                    case 'Limpieza':
                        print('Entro a limpieza')
                    case None:
                        pass
            case 'b':
                while True:
                    tipo_usuario = input('''Elija una opcion:
                    a. Cliente
                    b. Personal del hotel
                    c. Volver atrás
                    
                    ''')
                    match tipo_usuario:
                        case 'a':
                            fa.sign_in_cliente(lista_clientes)
                            break
                        case 'b':
                            while True:
                                tipo_personal = input('''Elija una opcion:
                    a. Administrativo
                    b. Mantenimiento
                    c. Limpieza
                    d. Volver atrás
                    
                    ''')
                                match tipo_personal:
                                    case 'a':
                                        fa.sign_in_administrativo(lista_administrativo)
                                        # Este volver atras = False, es para que si el usuario en algun momento toco volver atras, no se guarde
                                        # el valor de esa variable y al crear el usuario, vuelva al menu principal.
                                        volver_atras = False
                                        break
                                    case 'b':
                                        fa.sign_in_mantenimiento(lista_mantenimiento)
                                        volver_atras = False
                                        break
                                    case 'c':
                                        fa.sign_in_limpieza(lista_limpieza)
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
                    if volver_atras:
                        pass
                    else:
                        break
            case 'c':
                break
            case _:
                print('Porfavor elija una de las opciones (a | b | c)')