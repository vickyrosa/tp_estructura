import funciones.funciones_auxiliares as fa
from hotel.reservas import Reserva

def menu_administrador(admin, hotel):
    opcion = input('''Elija una opcion:
                   a. Ver porcentaje ocupacion del dia
                   b. Ver porcentaje ocupacion del dia por tipo de habitacion
                   c. 
                   d. 
                   
                   ''')
    match opcion:
        case 'a':
            admin.porcentaje_ocupacion(hotel)
        case 'b':
            admin.porcentaje_ocupacion_portipo(hotel)
        case 'c':
            pass
        case 'd':
            pass