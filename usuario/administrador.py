from usuario.personal import Personal
from usuario.usuario import Usuario
import datetime
import funciones.funciones_log_in_y_sign_in as flisi
from usuario.administrativo import Administrativo

class Administrador(Personal):
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
    
    # Devuelve el porcentaje de ocupacion del hotel. Pedimos la fecha de hoy en el formato correspondiente, 
    # recorremos la lista de reservas activas y nos fijamos que la fecha se encuentre entre la fecha de checkin y checkout.
    # Si se encuentra entre esos parametros la habitacion esta ocupada y sera tomada en cuenta al realizar la cuenta.
    def porcentaje_ocupacion(self, hotel):
        cont_ocupados = 0
        reserva_movil = hotel.lista_reservas_activas.cabeza
        fecha_hoy = datetime.datetime.today().strftime('%d/%m/%Y')
        # Aunque parezca un paso excesivo, es necesario para que todas las fechas sean calculadas con la misma hora y que no haya excepciones con eso
        fecha_hoy = datetime.datetime.strptime(fecha_hoy, '%d/%m/%Y')
        while reserva_movil is not None:
            if datetime.datetime.strptime(reserva_movil.fec_checkin, '%d/%m/%Y') <= fecha_hoy <= datetime.datetime.strptime(reserva_movil.fec_checkout, '%d/%m/%Y'):
                cont_ocupados += 1
            reserva_movil = reserva_movil.prox
        print(f'Estan ocupados {round((cont_ocupados/len(hotel.lista_habitaciones))*100, 2)}% de cuartos del hotel')
    
    # Al momento de contar la habitacion ocupada tambien se fija en su tipo.
    def porcentaje_ocupacion_portipo(self, hotel):
        # Los numeros de la cantidad total de habitaciones por tipo los dejamos fijos debido al feedback recibido de que el hotel
        # no se expande.
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
    
    # Solo un administrador puede despedir a un administrativo. Le pide el DNI del administrativo y lo busca en la lista de 
    # empleaedos administrativos. Si lo encuentra le cambia el atributo de fecha de baja por hoy y lo agrega a el txt de ex-personal.
    # Luego lo borra de la lista de empleados administrativos y del set con usuarios.
    def despedir_administrativo(self, lista_administrativo):
        while True:
            dni = input('Ingrese DNI del administrativo a dar de baja: ').strip()
            if flisi.check_dni(dni):
                break
        i = 0
        for administrativo in lista_administrativo:
            if administrativo.dni == dni:
                administrativo.fec_baja = datetime.date.today().strftime('%d/%m/%Y')
                with open('txt/ex_personal.txt', 'a') as ex_personal:
                    ex_personal.write(f'{administrativo.tipo_usuario},{administrativo.dni},{administrativo.nombre},{administrativo.contra},{administrativo.fec_nac},{administrativo.genero},{administrativo.tel},{administrativo.mail},{administrativo.domicilio},{administrativo.fec_alta},{administrativo.fec_baja},{administrativo.cuil},{administrativo.sueldo}\n')
                del(lista_administrativo[i])
                Usuario.set_dni.discard(administrativo.dni)
                Usuario.set_cuil.discard(administrativo.cuil)
                print(f'{administrativo.nombre} ha sido despedido correctamente')
                return
            i += 1
        print(f'No se ha encontrado un administrativo con el dni: {dni}')
    
    # El administrador va a ser el unico que pueda hacer sign in a un administrativo. Con los datos del usuario administrativo 
    # lo agrega a la lista de amdministrativos.
    def sign_in_administrativo(self, lista_administrativo):
        dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = flisi.pedir_datos_basicos_sing_in()
        tipo_usuario = 'Administrativo'
        cuil = flisi.pedir_cuil()
        sueldo = flisi.pedir_sueldo()
        lista_administrativo.append(Administrativo(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo))
    
    # Un administrador puede pedir las recaudaciones de un dia especifico. Con el dia ya seleccionado buscamos en el txt de los ingresos 
    # diarios lo recaudado ese dia y lo mostramos en la consola con el print.
    def buscar_recaudacion(self, hotel):
        while True:
            try:
                dia, mes, ano = map(int, input("Ingrese fecha de la cual quiere conocer la recaudación diaria en formato DD/MM/YYYY: ").split('/'))
                fecha = datetime.datetime.strftime(datetime.date(ano, mes, dia), '%d/%m/%Y')
                break
            except:
                print('Por favor ingrese una fecha valida en el formato pedido (Ej: 29/01/2023)') 
        with open('txt/ingresos_diarios.txt', 'r') as archivo_ingresos:
            for linea in archivo_ingresos:
                    if linea.startswith(f"Fecha: {fecha}"):
                        print(f'\n{linea}')
                        return
        if fecha == datetime.datetime.strftime(datetime.date.today(), '%d/%m/%Y'):
            print(f'\nFecha: {fecha} - Ingresos Totales: {hotel.ingresos_diarios}\n')
            return
        print('\nNo se encontraron datos de la fecha pedida\n')
    
    # Un administrador puede conocer la cantidad de clientes en cada nivel en el momento buscado
    def cant_clientes_por_tipo(self, lista_clientes):
        lista_cantidad = [0,0,0]
        tipos_cliente = ['Nivel Bajo', 'Nivel Medio', 'Nivel Alto']
        for cliente in lista_clientes:
            if cliente.historico_gastos in range(0,50000):
                lista_cantidad[0] += 1
            elif cliente.historico_gastos in range(50000,250000):
                lista_cantidad[1] += 1
            else:
                lista_cantidad[2] += 1
        for i in range(len(lista_cantidad)):
            print(f'De {tipos_cliente[i]} hay {lista_cantidad[i]} clientes')