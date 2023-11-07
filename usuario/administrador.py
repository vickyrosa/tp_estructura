from usuario.personal import Personal
from hotel.hotel import Hotel
from hotel.lista_reservas import Lista_Reservas
import datetime

class Administrador(Personal):
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
        
    def porcentaje_ocupacion(hotel):
        cont_ocupados = 0
        reserva_movil = hotel.lista_reservas_activas.head
        # Este paso parece de mas, pero es para que todas las fechas sean calculadas con la misma hora y que no haya excpeciones con eso
        fecha_hoy = datetime.datetime.strptime(str(datetime.date.today()), '%d/%m/%Y')
        while reserva_movil is not None:
            if datetime.datetime.strptime(reserva_movil.fec_checkin, '%d/%m/%Y') <= fecha_hoy <= datetime.datetime.strptime(reserva_movil.fec_checkout, '%d/%m/%Y'):
                cont_ocupados += 1
            reserva_movil = reserva_movil.prox
        print(f'Estan ocupados {(cont_ocupados/len(hotel.lista_habitaciones))*100}% de cuartos del hotel')
    
    def porcentaje_ocupacion_portipo(hotel):
        dict_tipos = {'Ocupado':{'Simple':0, 'Doble':0, 'Suite':0, 'Familiar':0}, 'Total':{'Simple':0, 'Doble':0, 'Suite':0, 'Familiar':0}}
        reserva_movil = hotel.lista_reservas_activas.head
        fecha_hoy = datetime.datetime.strptime(str(datetime.date.today()), '%d/%m/%Y')
        while reserva_movil is not None:
            dict_tipos['Total'][reserva_movil.habitacion.tipo] += 1
            if datetime.datetime.strptime(reserva_movil.fec_checkin, '%d/%m/%Y') <= fecha_hoy <= datetime.datetime.strptime(reserva_movil.fec_checkout, '%d/%m/%Y'):
                dict_tipos['Ocupado'][reserva_movil.habitacion.tipo] += 1
            reserva_movil = reserva_movil.prox
        for key in dict_tipos['Total'].keys:
            print(f"Tipo habitacion: {key} - Porcentaje de ocupación: {(dict_tipos['Ocupado'][key]/dict_tipos['Total'][key])*100}%")
    
    def despedir_personal(personal):
        personal.fec_baja = datetime.date.today().strftime('%d/%m/%Y')
        return f'{personal.nombre} ha sido despedido correctamente'
        
            
            