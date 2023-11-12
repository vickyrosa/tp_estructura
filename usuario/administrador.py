from usuario.personal import Personal
from hotel.hotel import Hotel
from hotel.lista_reservas import Lista_Reservas
import datetime
import funciones.funciones_auxiliares as fa
import funciones.funciones_log_in_y_sign_in as flisi
from usuario.administrativo import Administrativo

class Administrador(Personal):
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
        
    def porcentaje_ocupacion(self, hotel):
        cont_ocupados = 0
        reserva_movil = hotel.lista_reservas_activas.cabeza
        fecha_hoy = datetime.datetime.today().strftime('%d/%m/%Y')
        # Este paso parece de mas, pero es para que todas las fechas sean calculadas con la misma hora y que no haya excpeciones con eso
        fecha_hoy = datetime.datetime.strptime(fecha_hoy, '%d/%m/%Y')
        while reserva_movil is not None:
            if datetime.datetime.strptime(reserva_movil.fec_checkin, '%d/%m/%Y') <= fecha_hoy <= datetime.datetime.strptime(reserva_movil.fec_checkout, '%d/%m/%Y'):
                cont_ocupados += 1
            reserva_movil = reserva_movil.prox
        print(f'Estan ocupados {round((cont_ocupados/len(hotel.lista_habitaciones))*100, 2)}% de cuartos del hotel')
    
    def porcentaje_ocupacion_portipo(self, hotel):
        dict_tipos = {'Ocupado':{'Simple':0, 'Doble':0, 'Suite':0, 'Familiar':0}, 'Total':{'Simple':9, 'Doble':9, 'Suite':9, 'Familiar':9}}
        reserva_movil = hotel.lista_reservas_activas.cabeza
        fecha_hoy = datetime.datetime.today().strftime('%d/%m/%Y')
        fecha_hoy = datetime.datetime.strptime(fecha_hoy, '%d/%m/%Y')
        while reserva_movil is not None:
            if datetime.datetime.strptime(reserva_movil.fec_checkin, '%d/%m/%Y') <= fecha_hoy <= datetime.datetime.strptime(reserva_movil.fec_checkout, '%d/%m/%Y'):
                dict_tipos['Ocupado'][reserva_movil.habitacion.tipo] += 1
            reserva_movil = reserva_movil.prox
        for key in dict_tipos['Total'].keys():
            print(f"Tipo habitacion: {key} - Porcentaje de ocupación: {round((dict_tipos['Ocupado'][key]/dict_tipos['Total'][key])*100, 2)}%")
    
    def despedir_administrativo(self, lista_administrativo):
        dni = input('Ingrese DNI del administrativo a dar de baja: ').strip()
        i = 0
        for administrativo in lista_administrativo:
            if administrativo.dni == dni:
                administrativo.fec_baja = datetime.date.today().strftime('%d/%m/%Y')
                with open('txt/ex_personal.txt', 'a') as ex_personal:
                    ex_personal.write(f'{administrativo.tipo_usuario},{administrativo.dni},{administrativo.nombre},{administrativo.contra},{administrativo.fec_nac},{administrativo.genero},{administrativo.tel},{administrativo.mail},{administrativo.domicilio},{administrativo.fec_alta},{administrativo.fec_baja},{administrativo.cuil},{administrativo.sueldo}\n')
                del(lista_administrativo[i])
                print(f'{administrativo.nombre} ha sido despedido correctamente')
                break
            i += 1
        print(f'No se ha encontrado un administrativo con el dni: {dni}')
    
    def sign_in_administrativo(self, lista_administrativo):
        dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = flisi.pedir_datos_basicos_sing_in()
        tipo_usuario = 'Administrativo'
        cuil = flisi.pedir_cuil()
        sueldo = flisi.pedir_sueldo()
        lista_administrativo.append(Administrativo(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo))
    
    def buscar_recaudacion(self, fecha):
        while True:
            try:
                dia, mes, ano = map(int, input("Ingrese fecha de la cual quiere conocer la recaudación diaria en formato DD/MM/YYYY: ").split('/'))
                fecha = datetime.date(ano, mes, dia)
                break
            except:
                print('Por favor ingrese una fecha valida en el formato pedido (Ej: 29/01/2023)')
        ingreso_total = 0 
        with open('txt/recaudacion.txt', 'r') as archivo_recaudacion:
            for linea in archivo_recaudacion:
                    if linea.startswith(f"Fecha: {fecha}"):
                        ingreso_total = int(linea.split('Recaudacion del dia: ')[1])
                        break
            return ingreso_total
            
      
    
       
            