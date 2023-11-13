from usuario.personal import Personal
import funciones.funciones_auxiliares as fa
from hotel.reservas import Reserva 
import funciones.funciones_log_in_y_sign_in as flisi
from usuario.limpieza import Limpieza
from usuario.mantenimiento import Mantenimiento
from usuario.usuario import Usuario
import datetime


class Administrativo(Personal):
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
    
    # Un administrador puede ser el único que puede hacer sign in a un empleado de mantenimiento o de limpieza. 
    # Luego ingresa el empleado a su lista correspondiente
    def sign_in_mantenimiento(self, lista_mantenimiento):
        dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = flisi.pedir_datos_basicos_sing_in()
        tipo_usuario = 'Mantenimiento'
        cuil = flisi.pedir_cuil()
        sueldo = flisi.pedir_sueldo()
        lista_mantenimiento.append(Mantenimiento(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo, 'True'))
        print(f'El usuario del personal de mantenimiento con DNI: {dni} fue creado correctamente.')
        
    def sign_in_limpieza(self, lista_limpieza):
        dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = flisi.pedir_datos_basicos_sing_in()
        tipo_usuario = 'Limpieza'
        cuil = flisi.pedir_cuil()
        sueldo = flisi.pedir_sueldo()
        lista_limpieza.append(Limpieza(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo, 'True'))
        print(f'El usuario del personal de limpieza con DNI: {dni} fue creado correctamente.')
        
    # Un administrativo puede encargarle tareas a empleados de mantenimiento o de limpieza
    # Lo hace a través de un submenú
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
    
    # Itera la lista de empleados de limpieza, verifica si el empleado está disponible para asignarle una tarea 
    # si lo está cambia su disponibilidad a ocupado
    def encargar_limpieza(self, lista_limpieza):
        while True:
            # Verifica que el dni este correctamente ingresado
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
    
    # Itera la lista de empleados de mantenimiento, verifica si el empleado está disponible para asignarle una tarea 
    # si lo está cambia su disponibilidad a ocupado
    def encargar_mantenimiento(self, lista_mantenimiento):
        while True:
            #verifica que el dni este correctamente ingresado
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
    
    # Permite cancelar una tarea encomendada analizando la disponibilidad del empleado.
    # Para realizalo se debe ingresar el DNI del empleado para identificarlo
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
    
    # Muestra las reservas del cliente
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
        # Las reservas del cliente se guardan en una lista, para buscarlas hay que recorrer la lista enlazada en la que se almacenan
        # las reservas activas y posteriormente el txt que almacena las reservas vencidas.
    
        # Al hacerlo en este orden en la lista que se le mustra al usuario va a ver primero las reservas activas y posteriormente
        # las que ya vencieron.
        nodo = lista_reservas.cabeza
        while nodo:
            if nodo.cliente.dni == dni_cliente:
                reservas_encontradas.append(nodo)
            nodo = nodo.prox

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
            print(f"Reservas de {cliente.nombre}:")
            for reserva in reservas_encontradas:
                print(f'Número de reserva: {reserva.nroreserva} Habitación: {reserva.habitacion.numero} Fecha de check-in: {reserva.fec_checkin}\tFecha de check-out: {reserva.fec_checkout}\n')    
        else:
            print("No se encontraron reservas para este cliente.")

    #Itera sobre las listas de empleados de mantenimiento y limpieza para buscar al empleado con el DNI proporcionado. 
    # Si encuentra al empleado, actualiza la fecha de baja, lo registra en un archivo de empleados despedidos, elimina al empleado de la lista y actualiza los DNI y CUIL.    
    def despedir_personal(self, lista_mantenimiento, lista_limpieza):
        while True:
            dni_empleado = input('Ingrese DNI del empleado: ').strip()
            if flisi.check_dni(dni_empleado):
                break
        i = 0
        for mantenimiento in lista_mantenimiento:
            if mantenimiento.dni == dni_empleado:
                mantenimiento.fec_baja = datetime.date.today().strftime('%d/%m/%Y')
                with open('txt/ex_personal.txt', 'a') as ex_personal:
                    ex_personal.write(f'{mantenimiento.tipo_usuario},{mantenimiento.dni},{mantenimiento.nombre},{mantenimiento.contra},{mantenimiento.fec_nac},{mantenimiento.genero},{mantenimiento.tel},{mantenimiento.mail},{mantenimiento.domicilio},{mantenimiento.fec_alta},{mantenimiento.fec_baja},{mantenimiento.cuil},{mantenimiento.sueldo}\n')
                del(lista_mantenimiento[i])
                Usuario.set_dni.discard(mantenimiento.dni)
                Usuario.set_cuil.discard(mantenimiento.cuil)
                print(f'{mantenimiento.nombre}, personal de Mantenimiento ha sido despedido correctamente')
                return
            i += 1
        i = 0
        for limpieza in lista_limpieza:
            if limpieza.dni == dni_empleado:
                limpieza.fec_baja = datetime.date.today().strftime('%d/%m/%Y')
                with open('txt/ex_personal.txt', 'a') as ex_personal:
                    ex_personal.write(f'{limpieza.tipo_usuario},{limpieza.dni},{limpieza.nombre},{limpieza.contra},{limpieza.fec_nac},{limpieza.genero},{limpieza.tel},{limpieza.mail},{limpieza.domicilio},{limpieza.fec_alta},{limpieza.fec_baja},{limpieza.cuil},{limpieza.sueldo}\n')
                del(lista_limpieza[i])
                Usuario.set_dni.discard(limpieza.dni)
                Usuario.set_cuil.discard(limpieza.cuil)
                print(f'{limpieza.nombre}, personal de Limpieza ha sido despedido correctamente')
                return
            i += 1
        print(f'No se ha encontrado un empleado con el dni: {dni_empleado}')
            