import datetime
from hotel.lista_reservas import Lista_Reservas
from hotel.habitacion import Habitacion
from hotel.hotel import Hotel
import funciones.funciones_auxiliares as fa
class Reserva:
    #OJO cambio aca que le paso el cliente (como objeto) entero que reserva en vez del nombre
    def __init__(self, nroreserva, cliente, habitacion, fec_checkin, fec_checkout, prox = None):
        self.nroreserva = nroreserva
        self.nombre= cliente.nombre
        self.habitacion=habitacion
        self.fec_checkin= fec_checkin
        self.fec_checkout= fec_checkout
        self.prox = prox
        
    def __str__(self):
        return str(self.data)
    
    def __eq__(self, otro):
        if self.nroreserva == otro.nroreserva:
            return True 
        else:
            return False
    def reservar(self, usuario):
        while True:
            tipo = input(''' Elija un tipo de habitacion:
                a. Simple
                b. Doble
                c. Suite
                d. Familiar
                        
                ''')
            match tipo:
                case 'a' | 'b' | 'c' | 'd':
                    break
                case _:
                    print('Porfavor elija una de las opciones (a | b | c | d)')
        while True:
            try:
                dia, mes, ano = map(int, input("Ingrese fecha de check in en formato dd/mm/yyyy: ").split('/'))
                fec_checkin = datetime.date(ano, mes, dia).strftime('%d/%m/%Y')
                break
            except:
                print('Porfavor ingrese una fecha valida en el formato pedido (Ej: 29/01/2023)')
                
        while True:
            try:
                dia, mes, ano = map(int, input("Ingrese fecha de check out en formato dd/mm/yyyy: ").split('/'))
                fec_checkout = datetime.date(ano, mes, dia).strftime('%d/%m/%Y')
                break
            except:
                print('Porfavor ingrese una fecha valida en el formato pedido (Ej: 29/01/2023)')
        # En caso de que el usuario decida salir directamente sin elegir, consideramos que es indiferente cual sea su habitacion,
        # por ende solo filtramos por tipo y fechas
        conbano = None
        conventana = None
        while True:
            accion = input(''' 
                a. Elegir con o sin baño
                b. Elegir con o sin ventana
                c. Salir (si no ha seleccionado ninguna opcion se le considerara como indiferente)
                        
            ''')
            match accion:
                case 'a':
                    bano = input('''Elija si quiere con baño privado o no:
                                a. Con baño privado
                                b. Sin baño privado
                                c. Indiferente
                                 
                                ''')
                    match bano:
                        case 'a': 
                            conbano = True
                        case 'b':
                            conbano = False
                        case 'c':
                            conbano = None
                        case _: 
                            print("Porfavor elija una de las opciones (a | b | c)")
                case 'b':
                    ventana = input('''Elija si quiere con ventana o no:
                                a. Con ventana
                                b. Sin ventana
                                c. Indiferente
                                    
                                ''')
                    match ventana:
                        case 'a':
                            conventana = True
                        case 'b': 
                            conventana = False
                        case 'c':
                            conventana = None
                        case _:
                            print("Porfavor elija una de las opciones (a | b | c)")
                case 'c':
                    break
                case _: 
                    print("Porfavor elija una de las opciones (a | b | c)")
        
        #Puse parametros hardcodeados, despues cambiar
        #Fijarme si existe la habitacion que esta buscando el cliente
        ### FIJARME SI LA FECHA CHECKIN Y FECHA CHECKOUT NO SE ENCUENTRAN EN NINGUN INTERVALO DE FECHAS (.GET DISPONIBILIDAD EN HABITACION)
        
        # Soy toto, ahi te agregue para acceder a la lsita de habitaciones (esta gurdada en la clase hotel)
        # OJO! Con las condiciones que nos da la persona para reservar tenemos que hacer una lista de posibles opciones de habitaciones
        # luego en las reservas SOLO vamos a verificar aquellas que coincidan con la habitacion que el cliente nuevo quiere.
        # Despues de eso vamos a tener que ver que NO haya solapamiento de fechas para ahi recien poder crear la reserva
        # En caso de que no se encuentre una habitacion disponible vamos a tener que decirle al usuario que no hay y ofrecerle dos opciones:
        # cerrar sesion o cambiar las condiciones de reserva (ya sea fechas, tipo cuarto o lo que quiera, osea volver a hcaer la reserva de 0)
        
        for hab in Hotel.lista_habitaciones:
                if hab.get_tipo() == tipo:
                    if conbano is not None:
                        if conventana is not None:
                            if conbano == hab.tiene_bano_privado() and conventana == hab.tiene_ventana_balcon():
                                if fa.disponibilidad(fec_checkin,fec_checkout,hab):
                                    Lista_Reservas.agregar_reserva(Reserva(Lista_Reservas.len_lista, usuario, hab, fec_checkin, fec_checkout))
                                    return True
                        else:
                           if fa.disponibilidad(fec_checkin,fec_checkout,hab):
                                Lista_Reservas.agregar_reserva(Reserva(Lista_Reservas.len_lista, usuario, hab, fec_checkin, fec_checkout))
                                return True
                    else:
                        if conventana is not None:
                            if fa.disponibilidad(fec_checkin,fec_checkout,hab):
                                Lista_Reservas.agregar_reserva(Reserva(Lista_Reservas.len_lista, usuario, hab, fec_checkin, fec_checkout))
                                return True
                        else:
                            if fa.disponibilidad(fec_checkin,fec_checkout,hab):
                                Lista_Reservas.agregar_reserva(Reserva(Lista_Reservas.len_lista, usuario, hab, fec_checkin, fec_checkout))
                                return True
        return False
        ##Returnea TRUE si encontro la reserva, FALSE si no hay ninguna habitacion disponible. 
       





    
    
