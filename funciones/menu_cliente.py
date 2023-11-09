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
                        d. Cambiar contraseña
                        e. Log out
                        
                        ''')
        match opcion:
            case 'a':
                # Hacer try except para estos inputs
                Reserva.reservar(cliente, hotel)
            case 'b':
                Buffet.ordenar_menu(cliente)
            case 'c':
                pass
            case 'd':
                cliente.cambiar_contra()
            case 'e':
                break
            case _:
                print('Por favor elija una de las opciones (a | b | c | d | e)')
    