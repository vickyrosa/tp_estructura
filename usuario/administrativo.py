from usuario.personal import Personal
import funciones.funciones_auxiliares as fa
from hotel.reservas import Reserva 
import funciones.funciones_log_in_y_sign_in as flisi
from usuario.limpieza import Limpieza
from usuario.mantenimiento import Mantenimiento


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
        
    def encargar_tareas(self):
        while True:
            area = input(''' Elija una opcion:
                            a. Ordenar limpieza
                            b. Ordenar mantenimiento
                            c. Salir

                            ''')
            dni_empleado = input("Ingrese el DNI del empleado a realizar tarea")
            match area:
                case 'a':
                    self.encargar_limpieza(dni_empleado)
                case 'b':
                    self.encargar_mantenimiento(dni_empleado)
                case 'c':
                    break

    def encargar_limpieza(self, dni_personal):
        lista_limpieza = fa.download_limpieza()
        for empleado in lista_limpieza:
            if empleado.dni == dni_personal and empleado.disponibilidad == True:
                empleado.disponibilidad = False
                return "La tarea fue asignada correctamente"
        return "No se encontro al empleado"
    
    def encargar_mantenimiento(self, dni_personal):
        lista_mantenimiento = fa.download_mantenimiento()
        for empleado in lista_mantenimiento:
            if empleado.dni == dni_personal and empleado.disponibilidad == True:
                empleado.disponibilidad = False
                return "La tarea fue asignada correctamente"
        return "No se encontro al empleado"
    
    def cancelar_tarea(self, dni_personal):
        lista_limpieza = fa.download_limpieza()
        lista_mantenimiento = fa.download_mantenimiento()
        for empleado in lista_limpieza:
            if empleado.dni == dni_personal and empleado.disponibilidad == False:
                empleado.disponibilidad = True
                return  "La tarea ha sido cancelada correctamente"
        for empleado in lista_mantenimiento:
           if empleado.dni == dni_personal and empleado.disponibilidad == False:
               empleado.disponibilidad = True
               return  "La tarea ha sido cancelada correctamente"
        return "No se encontro al empleado"
    
    def mostrar_reservas_cliente(self, hotel, lista_clientes):
        dni_cliente = input("Ingrese DNI del cliente a buscar: ")
        lista_reservas = hotel.lista_reservas_activas
        lista_hab = hotel.lista_habitaciones
        for cli in lista_clientes:
            if dni_cliente == cli.dni:
                cliente = cli
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
            if int(dni) == cliente.dni:
                for hab in lista_hab:
                    if hab.numero == nro_habitacion:
                        habitacion = hab
                reserva = Reserva(nro_reserva, cliente, habitacion, fec_checkin, fec_checkout)
                reservas_encontradas.append(reserva)

        if reservas_encontradas:
            print("Reservas del cliente:")
            for reserva in reservas_encontradas:
                print(f'Número de reserva: {reserva.nroreserva} Habitación: {reserva.habitacion} Fecha de check-in: {reserva.fec_checkin}\tFecha de check-out: {reserva.fec_checkout}\n')    
        else:
            print("No se encontraron reservas para este cliente.")