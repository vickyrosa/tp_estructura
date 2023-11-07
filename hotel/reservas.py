import datetime
from hotel.lista_reservas import Lista_Reservas
from hotel.habitacion import Habitacion
from hotel.hotel import Hotel
import funciones.checks as checks
import random
#import funciones.funciones_auxiliares as fa OJO! Esto va a haber que sacarlo! Porque en fa tmb importamos reservas
class Reserva:
    #OJO cambio aca que le paso el cliente (como objeto) entero que reserva en vez del nombre
    def __init__(self, nroreserva, cliente, habitacion, fec_checkin, fec_checkout, prox = None):
        self.nroreserva = nroreserva
        self.nombre= cliente
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
        
        #Puse parametros hardcodeados, despues cambiar
        #Fijarme si existe la habitacion que esta buscando el cliente
        ### FIJARME SI LA FECHA CHECKIN Y FECHA CHECKOUT NO SE ENCUENTRAN EN NINGUN INTERVALO DE FECHAS (.GET DISPONIBILIDAD EN HABITACION)
        
        # Soy toto, ahi te agregue para acceder a la lsita de habitaciones (esta gurdada en la clase hotel)
        # OJO! Con las condiciones que nos da la persona para reservar tenemos que hacer una lista de posibles opciones de habitaciones
        # luego en las reservas SOLO vamos a verificar aquellas que coincidan con la habitacion que el cliente nuevo quiere.
        # Despues de eso vamos a tener que ver que NO haya solapamiento de fechas para ahi recien poder crear la reserva
        # En caso de que no se encuentre una habitacion disponible vamos a tener que decirle al usuario que no hay y ofrecerle dos opciones:
        # cerrar sesion o cambiar las condiciones de reserva (ya sea fechas, tipo cuarto o lo que quiera, osea volver a hcaer la reserva de 0)
        
        for hab in hotel.lista_habitaciones:
            if hab.get_tipo() == tipo:
                if conbano is not None:
                    if conventana is not None:
                        if conbano == hab.tiene_bano_privado() and conventana == hab.tiene_ventana_balcon():
                            if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                                hotel.lista_reservas_activas.agregar_reserva(Reserva(random.randint(1,999999), usuario, hab, fec_checkin, fec_checkout))
                                return True
                    else:
                        if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                            hotel.lista_reservas_activas.agregar_reserva(Reserva(random.randint(1,999999), usuario, hab, fec_checkin, fec_checkout))
                            return True
                else:
                    if conventana is not None:
                        if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                            hotel.lista_reservas_activas.agregar_reserva(Reserva(random.randint(1,999999), usuario, hab, fec_checkin, fec_checkout))
                            return True
                    else:
                        if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                            hotel.lista_reservas_activas.agregar_reserva(Reserva(random.randint(1,999999), usuario, hab, fec_checkin, fec_checkout))
                            return True
        return False
        ##Returnea TRUE si encontro la reserva, FALSE si no hay ninguna habitacion disponible. 
    
    
    # CORRO ESTAS FUNCIONES ACA Y NO EN FA POR UN PROBLEMA DE MODULARIDAD CIRCULAR, NO NOS DEJA IMPORTAR RESERVAS EN FA Y EL MISMO TIEMPO
    # FA EN RESERVAS
    
    #Veo dos maneras de hacerlo: 1- Recorrer la lista enlazada preguntando en cada nodo por 
    # la habitacion y la fecha de reserva y ordenar de menor a mayor
    # La 2da forma es recorriendo el .txt que me parece menos practico porque tengo que abrir el archivo leerlo y recien ahi empezar a codear.
    def lista_reservas_actuales(habitacion, hotel):
        ##levantar una lista que tenga fechas checkin checkout por la habitacion que yo le pase
        #Obs: todo esto funciona bajo la suposicion de que fec_checkin < fec_checkout.
        # Puedo recorrer asi Lista_Reservas????
        #-----------------------------------------
        # Por si no anda aplicar sorted de una dejo esto de aca abajo
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
            pass
        else:
            for res in hotel.lista_reservas_activas:
                if res.habitacion == habitacion:
                    listareservas.append(datetime.datetime.strptime(res.fec_checkin, '%d/%m/%Y'))
                    listareservas.append(datetime.datetime.strptime(res.fec_checkout, '%d/%m/%Y'))
        ## Ahora toca ordenar de menor a mayor esas fechas de checkin checkout.
        listareservas = sorted(listareservas)
        return listareservas
    
    def disponibilidad(fec_checkin, fec_checkout, habitacion, hotel):
        lista_reservas_x_hab = Reserva.lista_reservas_actuales(habitacion, hotel)
        if len(lista_reservas_x_hab) == 0:
            return True
        if fec_checkout < lista_reservas_x_hab[0]:
            return True
        i = 2
        while i < lista_reservas_x_hab.len():
            if fec_checkin > lista_reservas_x_hab[i-1] and fec_checkout < lista_reservas_x_hab[i]:
                return True
            i += 2
        if fec_checkin > lista_reservas_x_hab[i-1]:
            return True       
        return False
       





    
    
