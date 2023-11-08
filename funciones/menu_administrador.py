import funciones.funciones_auxiliares as fa
from hotel.reservas import Reserva

def menu_administrador(administrador, hotel):
    while True:
        opcion = input('''Elija una opcion:
                    a. Ver porcentaje ocupacion del dia
                    b. Ver porcentaje ocupacion del dia por tipo de habitacion
                    c. 
                    d. Cambiar contrasena
                    e. Log out
                    
                    ''')
        match opcion:
            case 'a':
                # NO ENTIENDO XQ SALTA ERROR, DICE QUE LE PASO DOS ARGUMENTO CDO CLARAMENTE LE TOY PASANDO UNO SOLO
                # Puse el print este para que se vea que administrador y hotel se pasan bien como objetos

                #creo que no se estan importando bien los archivos que te dicen el porcentaje.

                print(administrador)
                print(hotel)
                administrador.porcentaje_ocupacion(hotel)
            case 'b':
                administrador.porcentaje_ocupacion_portipo(hotel)
            case 'c':
                pass
            case 'd':
                administrador.cambiar_contra()
            case 'e':
                break
            case _:
                print('Por favor elija una de las opciones (a | b | c | d | e)')