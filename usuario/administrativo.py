from usuario.personal import Personal
import funciones.funciones_auxiliares as fa
from hotel.reservas import Reserva 
import funciones.funciones_log_in_y_sign_in as flisi
from usuario.limpieza import Limpieza
from usuario.mantenimiento import Mantenimiento
import datetime


class Administrativo(Personal):
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
    
    def sign_in_mantenimiento(self, lista_mantenimiento):
        dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = flisi.pedir_datos_basicos_sing_in()
        tipo_usuario = 'Mantenimiento'
        cuil = flisi.pedir_cuil()
        sueldo = flisi.pedir_sueldo()
        lista_mantenimiento.append(Mantenimiento(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo))
        print(f'El usuario del personal de mantenimiento con DNI: {dni} fue creado correctamente.')
        
    def sign_in_limpieza(self, lista_limpieza):
        dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = flisi.pedir_datos_basicos_sing_in()
        tipo_usuario = 'Limpieza'
        cuil = flisi.pedir_cuil()
        sueldo = flisi.pedir_sueldo()
        lista_limpieza.append(Limpieza(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo))
        print(f'El usuario del personal de limpieza con DNI: {dni} fue creado correctamente.')
        
    def encargar_tareas(self, lista_mantenimiento, lista_limpieza):
        while True:
            area = input(''' Elija una opcion:
                            a. Ordenar mantenimiento
                            b. Ordenar limpieza
                            c. Salir

                            ''').strip().lower()
                        
            match area:
                case 'a':
                    self.encargar_mantenimiento(lista_mantenimiento)
                case 'b':
                    self.encargar_limpieza(lista_limpieza)
                case 'c':
                    break
                case _:
                    print('Porfavor elija una de las opciones (a | b | c)')

    def encargar_limpieza(self, lista_limpieza):
        while True:
            dni_empleado = input('Ingrese DNI del empleado: ').strip()
            if flisi.check_dni(dni_empleado):
                break
        for empleado in lista_limpieza:
            if empleado.dni == dni_empleado:
                if empleado.disponibilidad == True:
                    empleado.disponibilidad = False
                    print("La tarea fue asignada correctamente")
                    return
                else:
                    print('El empleado esta ocupado')
                    return
        print("No se encontro al empleado")
    
    def encargar_mantenimiento(self, lista_mantenimiento):
        while True:
            dni_empleado = input('Ingrese DNI del empleado: ').strip()
            if flisi.check_dni(dni_empleado):
                break
        for empleado in lista_mantenimiento:
            if empleado.dni == dni_empleado:
                if empleado.disponibilidad == True:
                    empleado.disponibilidad = False
                    print("La tarea fue asignada correctamente")
                    return
                else:
                    print('El empleado esta ocupado')
                    return
        print("No se encontro al empleado")
    
    def cancelar_tarea(self, lista_mantenimiento, lista_limpieza):
        while True:
            dni_empleado = input('Ingrese DNI del empleado: ').strip()
            if flisi.check_dni(dni_empleado):
                break
        for empleado in lista_limpieza:
            if empleado.dni == dni_empleado:
                if empleado.disponibilidad == False:
                    empleado.disponibilidad = True
                    print("La tarea ha sido cancelada correctamente")
                    return
                else:
                    print('El empleado no esta realizando ninguna tarea')
                    return
        for empleado in lista_mantenimiento:
           if empleado.dni == dni_empleado:
                if empleado.disponibilidad == False:
                    empleado.disponibilidad = True
                    print("La tarea ha sido cancelada correctamente")
                    return
                else:
                    print('El empleado no esta realizando ninguna tarea')
                    return
        print("No se encontro al empleado o su tarea ya ha sido finalizada")
    
    def mostrar_reservas_cliente(self, hotel, lista_clientes):
        while True:
            cliente = None
            dni_cliente = input('Ingrese DNI del cliente a buscar: ').strip()
            if flisi.check_dni(dni_cliente):
                for cli in lista_clientes:
                    if dni_cliente == cli.dni:
                        cliente = cli
                        break
                # Verificamos que el cliente exista, si no lo hace, vuelve a pedirle un DNI
                if cliente is not None:
                    break
                else:
                    print('El cliente no existe en la base de datos, porfavor ingrese otro DNI.')
                
        lista_reservas = hotel.lista_reservas_activas
        lista_hab = hotel.lista_habitaciones
        
        reservas_encontradas = []
    
        actual = lista_reservas.cabeza
        while actual:
            if actual.cliente.dni == dni_cliente:
                reservas_encontradas.append(actual)
            actual = actual.prox

        historico_gral_reservas = open('txt/historico_gral_reservas.txt', 'r')
        lista_info_reserva = historico_gral_reservas.readlines()
        for i in range(len(lista_info_reserva)):
            nro_reserva, dni, nro_habitacion, fec_checkin, fec_checkout = lista_info_reserva[i].strip().split(',')
            if dni == cliente.dni:
                for hab in lista_hab:
                    if hab.numero == nro_habitacion:
                        habitacion = hab
                        break
                reserva = Reserva(nro_reserva, cliente, habitacion, fec_checkin, fec_checkout)
                reservas_encontradas.append(reserva)

        if reservas_encontradas:
            print("Reservas del cliente:")
            for reserva in reservas_encontradas:
                print(f'Número de reserva: {reserva.nroreserva} Habitación: {reserva.habitacion} Fecha de check-in: {reserva.fec_checkin}\tFecha de check-out: {reserva.fec_checkout}\n')    
        else:
            print("No se encontraron reservas para este cliente.")
            
    def despedir_personal(self, lista_mantenimiento, lista_limpieza):
        area_personal = None
        while True:
            dni_empleado = input('Ingrese DNI del empleado: ').strip()
            if flisi.check_dni(dni_empleado):
                break
        echado = False
        for mantenimiento in lista_mantenimiento:
            if mantenimiento.dni == dni_empleado:
                mantenimiento.fec_baja = datetime.date.today().strftime('%d/%m/%Y')
                echado = True
                area_personal = 'Mantenimiento'
                break
        if echado == False:
            for limpieza in lista_limpieza:
                if limpieza.dni == dni_empleado:
                    limpieza.fec_baja = datetime.date.today().strftime('%d/%m/%Y')
                echado = True
                area_personal = 'Limpieza'
                break
        if echado == True:
            return f'{mantenimiento.nombre}, personal de {area_personal} ha sido despedido correctamente'
        else:
            print(f'No se ha encontrado un empleado con el dni: {dni_empleado}')
            