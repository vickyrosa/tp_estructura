import funciones.funciones_auxiliares as fa
from hotel.reservas import Reserva

def menu_cliente(cliente):
    # Creo menu para cliente
    opcion = input(''' Elija una opcion:
                    a. Reservar una habitacion
                    b. Ir al buffet
                    c. BOTON PRUEBA
                    
                    ''')
    match opcion:
        case 'a':
            # Hacer try except para estos inputs
            Reserva.reservar(cliente)
        case 'b':
            pass
        case 'c':
            print('Entro a cliente')
    