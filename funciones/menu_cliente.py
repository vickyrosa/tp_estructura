import funciones.funciones_auxiliares as fa
from hotel.reservas import Reserva

def menu_cliente(cliente):
    # Creo menu para cliente
    opcion = input(''' Elija una opcion:
                    a. Reservar una habitacion
                    b. Cancelar reserva
                    c. Pedir del buffet
                    d. Cambiar contraseña
                    e. BOTON PRUEBA
                    
                    ''')
    match opcion:
        case 'a':
            # Hacer try except para estos inputs
            Reserva.reservar(cliente)
        case 'b':
            pass
        case 'c':
            pass
        case 'd':
            cliente.cambiar_contra()
        case 'e':
            print('Entro a cliente')
        case _:
            print('Porfavor elija una de las opciones (a | b | c)')
    