import datetime
import funciones.metodos_de_pagos as mp

class Reserva:
    def __init__(self, nroreserva, cliente, habitacion, fec_checkin, fec_checkout, prox = None):
        self.nroreserva = int(nroreserva)
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
    
    # Este metodo le muestra al cliente que reservo todos los datos de su reserva en detalle
    def confirmacion_reserva(numero_reserva, usuario, hab, fec_checkin, fec_checkout, dias_totales, hotel):
        print(f'''La reserva fue efectuada correctamente.
NUMERO DE RESERVA: {numero_reserva}

HABITACION:{hab}

CLIENTE: {usuario}
CHECK IN: {fec_checkin}
CHECK OUT: {fec_checkout}
TOTAL DIAS: {dias_totales}

COSTO TOTAL: ${hab.precio_noche*dias_totales} (${hab.precio_noche} por noche)
''')
        mp.metodo_de_pago(hotel, hab.precio_noche*dias_totales)
    
    def lista_reservas_actuales(habitacion, hotel):
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
        # Ordenamos de menor a mayor esas fechas de checkin checkout
        listareservas = sorted(listareservas)
        return listareservas
    
    def disponibilidad(fec_checkin, fec_checkout, habitacion, hotel):
        fecha_checkin =  datetime.datetime.strptime(fec_checkin, '%d/%m/%Y')
        fecha_checkout =  datetime.datetime.strptime(fec_checkout, '%d/%m/%Y')
        lista_reservas_x_hab = Reserva.lista_reservas_actuales(habitacion, hotel)
        if len(lista_reservas_x_hab) == 0:
            return True
        # Se fija si la fecha de check-out de la reserva es anterior o igual a la primera fecha de checkin (pues consideramos que el
        # check-out se realiza temprano y el check in seguido a el).
        if fecha_checkout <= lista_reservas_x_hab[0]:
            return True
        i = 2
        # Se fija si la fecha de check-in de la reserva actual es posterior o igual a la fecha de check-out de la reserva anterior y la fecha
        # de check-out de la reserva actual es anterior o igual a la fecha de check-in de la siguiente reserva, entonces la habitación está disponible.
        # Esto es posible porque la lista de resevas x habitacion está ordenada.
        while i < len(lista_reservas_x_hab):
            if fecha_checkin >= lista_reservas_x_hab[i-1] and fecha_checkout <= lista_reservas_x_hab[i]:
                return True
            i += 2
        # Si la fecha de check-in es posterior o igual a la fecha de check-out de la última reserva en la lista, entonces está disponible.
        if fecha_checkin >= lista_reservas_x_hab[i-1]:
            return True
        return False
    
