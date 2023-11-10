import funciones.funciones_auxiliares as fa
from hotel.reservas import Reserva
from hotel.buffet import Buffet

def menu_cliente(cliente, hotel):
    while True:
    # Creo menu para cliente
        opcion = input(''' Elija una opcion:
                        a. Reservar una habitacion
                        b. Cancelar reserva
                        c. Pedir del buffet
                        d. Ver mi categoria
                        e. Cambiar contraseña
                        f. Log out
                        
                        ''')
        match opcion:
            case 'a':
                #OJO! LOS METODOS SE TIENEN QUE LLAMAR SI O SI DE CLIENTE OSEA: cliente.ordenar_menu() y cliente.reservar()
                # Hacer try except para estos inputs
                cliente.reservar(hotel)
            case 'b':
                pass
            case 'c':
                Buffet.ordenar_menu(cliente)
            case 'd':
                cliente.ver_categoria()
            case 'e':
                cliente.cambiar_contra()
            case 'f':
                break
            case _:
                print('Por favor elija una de las opciones (a | b | c | d | e | f)')
    