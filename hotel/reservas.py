import datetime
from hotel.lista_reservas import Lista_Reservas
from hotel.habitacion import Habitacion
from hotel.hotel import Hotel
#import funciones.menu_cliente as menu_cliente
import random
#import funciones.funciones_auxiliares as fa OJO! Esto va a haber que sacarlo! Porque en fa tmb importamos reservas
class Reserva:
    #OJO cambio aca que le paso el cliente (como objeto) entero que reserva en vez del nombre
    def __init__(self, nroreserva, cliente, habitacion, fec_checkin, fec_checkout, prox = None):
        self.nroreserva = nroreserva
        self.cliente = cliente
        self.habitacion =habitacion
        self.fec_checkin = fec_checkin
        self.fec_checkout = fec_checkout
        self.prox = prox
        
    def __str__(self):
        return str(self.nroreserva)
    
    def __eq__(self, otro):
        if self.nroreserva == otro.nroreserva:
            return True 
        else:
            return False
        
    def reservar(usuario, hotel):
        while True:
            tipo = input(''' Elija un tipo de habitacion:
                a. Simple
                b. Doble
                c. Suite
                d. Familiar
                        
                ''')
            match tipo:
                case 'a':
                    tipo = 'Simple'
                    break
                case 'b':
                    tipo = 'Doble'
                    break
                case 'c':
                    tipo = 'Suite'
                    break
                case 'd':
                    tipo = 'Familiar'
                    break
                case _:
                    print('Porfavor elija una de las opciones (a | b | c | d)')
        while True:
            # Utilizamos dos While diferentes para cada fecha, asi el usuario en caso de ingresar una de las dos en un formato incorrecto
            # no precisa volver a ingresar la anterior
            while True:
                try:
                    dia, mes, ano = map(int, input("Ingrese fecha de check-in en formato DD/MM/YYYY: ").split('/'))
                    fec_checkin = datetime.date(ano, mes, dia)
                    break
                except:
                    print('Porfavor ingrese una fecha valida en el formato pedido (Ej: 29/01/2023)')
                    
            while True:
                try:
                    dia, mes, ano = map(int, input("Ingrese fecha de check-out en formato DD/MM/YYYY: ").split('/'))
                    fec_checkout = datetime.date(ano, mes, dia)
                    break
                except:
                    print('Porfavor ingrese una fecha valida en el formato pedido (Ej: 29/01/2023)')
            if fec_checkin < fec_checkout:
                if datetime.date.today() < fec_checkin:
                    # Una vez que verificamos que las fechas son correctas cronologicamente, las pasamos a str en el formato que queremos
                    fec_checkin = fec_checkin.strftime('%d/%m/%Y')
                    fec_checkout = fec_checkout.strftime('%d/%m/%Y')
                    break
                else:
                    print('Porfavor ingrese una fecha de check-in posterior al dia de hoy')
            else:
                print('Porfavor ingrese una fecha de check-in anterior a fecha de check-out')
                    
        # En caso de que el usuario decida salir directamente sin elegir, consideramos que es indiferente cual sea su habitacion,
        # por ende solo filtramos por tipo y fechas
        conbano = None
        conventana = None
        while True:
            accion = input(''' 
                a. Elegir con o sin baño
                b. Elegir con o sin ventana
                c. Continuar (si no ha seleccionado ninguna opcion se le considerara como indiferente)
                        
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

        for hab in hotel.lista_habitaciones:
            numero_reserva = random.randint(1,999999)
            if hab.get_tipo() == tipo:
                if conbano is not None:
                    if conventana is not None:
                        if conbano == bool(hab.tiene_bano_privado()) and conventana == bool(hab.tiene_ventana_balcon()):
                            if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                                hotel.lista_reservas_activas.agregar_reserva(Reserva(numero_reserva, usuario, hab, fec_checkin, fec_checkout))
                                Reserva.confirmacion_reserva(numero_reserva, usuario, hab, fec_checkin, fec_checkout)
                                return True
                    else:
                        if conbano == bool(hab.tiene_bano_privado()):
                            if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                                hotel.lista_reservas_activas.agregar_reserva(Reserva(numero_reserva, usuario, hab, fec_checkin, fec_checkout))
                                Reserva.confirmacion_reserva(numero_reserva, usuario, hab, fec_checkin, fec_checkout)
                                return True
                else:
                    if conventana is not None:
                        if conventana == bool(hab.tiene_ventana_balcon()):
                            if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                                hotel.lista_reservas_activas.agregar_reserva(Reserva(numero_reserva, usuario, hab, fec_checkin, fec_checkout))
                                Reserva.confirmacion_reserva(numero_reserva, usuario, hab, fec_checkin, fec_checkout)
                                return True
                    else:
                        if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                            hotel.lista_reservas_activas.agregar_reserva(Reserva(numero_reserva, usuario, hab, fec_checkin, fec_checkout))
                            Reserva.confirmacion_reserva(numero_reserva, usuario, hab, fec_checkin, fec_checkout)
                            return True
        print('No se encontro una habitacion disponible en las fechas con sus preferencias, porfavor realize una nueva reserva cambiando los parametros y/o fechas')
    
    def confirmacion_reserva(numero_reserva, usuario, hab, fec_checkin, fec_checkout):
        print(f'''La reserva fue efectuada correctamente.
NUMERO DE RESERVA: {numero_reserva}

HABITACION:
{hab}

CLIENTE:
{usuario}
CHECK IN: {fec_checkin}
CHECK OUT: {fec_checkout}
''')
    
    def lista_reservas_actuales(habitacion, hotel):
        ##levantar una lista que tenga fechas checkin checkout por la habitacion que yo le pase
        #Obs: todo esto funciona bajo la suposicion de que fec_checkin < fec_checkout.
        #-----------------------------------------
        #listareservasnum = []
        #fecinaux = 0
        #fecoutaux = 0
        # for res in Lista_Reservas:
        #     if res.habitacion == habitacion:
        #         fecinaux = int(res.fec_checkin.strftime("%Y%m%d%H%M%S"))
        #         fecoutaux = int(res.fec_checkout.strftime("%Y%m%d%H%M%S"))
        #         listareservasnum.append[fecinaux]
        #         listareservasnum.append[fecoutaux]
        # ## Ahora toca ordenar de menor a mayor esas fechas de checkin checkout.
        # ## Como tengo las fechas en formato int lo hago con sorted.
        # listareservasnum = sorted(listareservasnum)
        # # Ahora recorro la lista y paso las fechas de formato int a formato fecha.
        # listareservasfec = []
        # for fecha in listareservasnum:
        #     fecha = str(fecha)
        #     fecha = datetime.strptime(fecha, "%Y%m%d%H%M%S")
        #     listareservasfec.append(fecha)
        #-----------------------------------------
        listareservas = []
        if hotel.lista_reservas_activas.len_lista() == 0:
            print("No hay reservas actuales")
            pass
        else:
            lista_reservas_activas = hotel.lista_reservas_activas
            reserva_movil = lista_reservas_activas.cabeza
            while reserva_movil is not None:
                if reserva_movil.habitacion == habitacion:
                    listareservas.append(datetime.datetime.strptime(reserva_movil.fec_checkin, '%d/%m/%Y'))
                    listareservas.append(datetime.datetime.strptime(reserva_movil.fec_checkout, '%d/%m/%Y'))
                reserva_movil = reserva_movil.prox    
        ## Ahora toca ordenar de menor a mayor esas fechas de checkin checkout
        listareservas = sorted(listareservas)
        return listareservas
    
    def disponibilidad(fec_checkin, fec_checkout, habitacion, hotel):
        fecha_checkin =  datetime.datetime.strptime(fec_checkin, '%d/%m/%Y')
        fecha_checkout =  datetime.datetime.strptime(fec_checkout, '%d/%m/%Y')
        lista_reservas_x_hab = Reserva.lista_reservas_actuales(habitacion, hotel)
        if len(lista_reservas_x_hab) == 0:
            return True
        if fecha_checkout < lista_reservas_x_hab[0]:
            return True
        i = 2
        while i < len(lista_reservas_x_hab):
            if fecha_checkin > lista_reservas_x_hab[i-1] and fecha_checkout < lista_reservas_x_hab[i]:
                return True
            i += 2
        if fecha_checkin > lista_reservas_x_hab[i-1]:
            return True
        return False
        # opcion = input('''No se encontraron habitaciones disponibles en esas fechas, elija una opcion:
        #             a. Reservar otra habitacion
        #             b. Volver atrás   
        #             ''')
        # match opcion:
        #     case 'a':
        #         Reserva.reservar()
        #     case 'b':
        #         menu_cliente.menu_cliente()
        # pass
       





    
    
