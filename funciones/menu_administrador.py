import funciones.funciones_auxiliares as fa
from hotel.reservas import Reserva

def menu_administrador(administrador, hotel):
    opcion = input('''Elija una opcion:
                   a. Ver porcentaje ocupacion del dia
                   b. Ver porcentaje ocupacion del dia por tipo de habitacion
                   c. 
                   d. Cambiar contrasena
                   e.
                   
                   ''')
    match opcion:
        case 'a':
            # NO ENTIENDO XQ SALTA ERROR, DICE QUE LE PASO DOS ARGUMENTO CDO CLARAMENTE LE TOY PASANDO UNO SOLO
            print(administrador)
            administrador.porcentaje_ocupacion(hotel)
        case 'b':
            administrador.porcentaje_ocupacion_portipo(hotel)
        case 'c':
            pass
        case 'd':
            administrador.cambiar_contra()
        case 'e':
            pass
        case _:
            pass