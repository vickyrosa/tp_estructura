from usuario.cliente import Cliente
from usuario.administrativo import Administrativo
from usuario.administrador import Administrador
from usuario.mantenimiento import Mantenimiento
from usuario.limpieza import Limpieza
from hotel.habitacion import Habitacion
from hotel.hotel import Hotel
import datetime
from hotel.lista_reservas import Lista_Reservas
from hotel.habitacion import Habitacion
from hotel.reservas import Reserva
from collections import deque

# Las funciones download se encargan de leer los archivos txt donde esta la informacion de corridas previas del codigo, de tal forma
# que dicha informacion se guarda en distintas estructuras de datos (segun sea mas conveniente para cada caso) para poder modificarla,
# leerla o realizar la operacion necesaria. De esta forma tambien evitamos estar constantemente abriendo y cerrando los archivos txt
# obteniendo un codigo mas eficiente.

def download_hotel(lista_clientes):
    lista_habitaciones = download_habitaciones()
    lista_reservas_activas = download_reservas_activas(lista_clientes, lista_habitaciones)
    admin = download_administrador()
    ingresos_diarios = download_ingresos()
    hotel = Hotel(admin, lista_habitaciones, lista_reservas_activas, ingresos_diarios)
    return hotel

def download_ingresos(): #Devuelve la cantidad de ingresos diarios o 0, dependiendo de si hubo ingresos para la fecha actual.
    fecha_hoy = datetime.datetime.now().strftime('%d/%m/%Y')
    with open('txt/ingresos_diarios_aux.txt', 'r') as archivo_aux:
        lista_info_ingresos = archivo_aux.readlines()
    fecha, ingresos_diarios = lista_info_ingresos[0].strip().split(',')
    if fecha_hoy == fecha:
        return ingresos_diarios
    else:
        with open('txt/ingresos_diarios.txt', 'a') as archivo_ingresos:
            archivo_ingresos.write(f'Fecha: {fecha} - Ingresos Totales: {ingresos_diarios}\n\n')
        with open('txt/ingresos_diarios_aux.txt', 'w') as archivo_aux:
            archivo_aux.write(f'{fecha_hoy},0')
        return 0

def download_administrador():  #Devuelve la informacion del administrador contenida en el .txt. 
    with open('txt/administrador.txt', 'r') as archivo_administrador:
        info_administrador = archivo_administrador.readlines()
    tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo = info_administrador[0].strip().split(',')
    return Administrador(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)

def download_clientes():    #Devuelve una lista con toda la informacion de los clientes contenida en el .txt.
    lista_clientes = list()
    with open('txt/clientes.txt', 'r') as archivo_clientes:
        lista_info_clientes = archivo_clientes.readlines()
    for i in range(len(lista_info_clientes)):
        tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, historico_gastos = lista_info_clientes[i].strip().split(',')
        lista_clientes.append(Cliente(tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, int(historico_gastos)))
    return lista_clientes

def download_personal():    #Devuelve toda la informacion del personal separada por sectores.
    lista_administrativo = download_administrativo()
    lista_mantenimiento = download_mantenimiento()
    lista_limpieza = download_limpieza()
    
    return lista_administrativo, lista_mantenimiento, lista_limpieza

def download_administrativo():      #Devuelve una lista con toda la informacion del personal administrativo contenida en el .txt.
    lista_administrativo = list()
    with open('txt/administrativo.txt', 'r') as archivo_administrativo:
        lista_info_administrativo = archivo_administrativo.readlines()
    for i in range(len(lista_info_administrativo)):
        tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo = lista_info_administrativo[i].strip().split(',')
        lista_administrativo.append(Administrativo(tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo))
    return lista_administrativo

def download_mantenimiento():   #Devuelve una lista con toda la informacion del personal de mantenimiento contenida en el .txt.
    lista_mantenimiento = list()
    with open('txt/mantenimiento.txt', 'r') as archivo_mantenimiento:
        lista_info_mantenimiento = archivo_mantenimiento.readlines()
    for i in range(len(lista_info_mantenimiento)):
        tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad, fichar = lista_info_mantenimiento[i].strip().split(',')
        lista_mantenimiento.append(Mantenimiento(tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad, fichar))
    return lista_mantenimiento

def download_limpieza():    #Devuelve una lista con toda la informacion del personal de limpieza contenida en el .txt.
    lista_limpieza = list()
    with open('txt/limpieza.txt', 'r') as archivo_limpieza:
        lista_info_limpieza = archivo_limpieza.readlines()
    for i in range(len(lista_info_limpieza)):
        tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad, fichar = lista_info_limpieza[i].strip().split(',')
        lista_limpieza.append(Limpieza(tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad, fichar))
    return lista_limpieza

def download_habitaciones():    #Devuelve una lista con toda la informacion de la habitacion contenida en el .txt.
    lista_habitaciones = list()
    with open('txt/habitaciones.txt', 'r') as archivo_habitaciones:
        lista_info_habitaciones = archivo_habitaciones.readlines()
    for i in range(len(lista_info_habitaciones)):
        numero, capacidad_maxima, tipo, precio_noche, bano_privado, ventana_balcon = lista_info_habitaciones[i].strip().split(',')
        lista_habitaciones.append(Habitacion(numero, capacidad_maxima, tipo, precio_noche, bano_privado, ventana_balcon))
    return lista_habitaciones

def download_reservas_activas(lista_clientes, lista_habitaciones):
    lista_reservas = Lista_Reservas()
    pila_reservas = deque()
    with open('txt/reservas_activas.txt', 'r') as archivo_reservas:
        lista_info_reservas = archivo_reservas.readlines()
    for i in range(len(lista_info_reservas)):
        nroreserva, dni_cliente, nro_habitacion, fec_checkin, fec_checkout = lista_info_reservas[i].strip().split(',')
        for cli in lista_clientes:
            if cli.dni == dni_cliente:
                cliente = cli
                break
        for hab in lista_habitaciones:
            if hab.numero == nro_habitacion:
                habitacion = hab
                break
        # Verificamos si la reserva ya caduco o si sigue activa
        # Si caduco se agrega al txt de historico general de reservas, si es una reserva activa se agrega a la lista enlazada.
        if datetime.datetime.strptime(fec_checkout, '%d/%m/%Y') < datetime.datetime.today():
            pila_reservas.append(Reserva(nroreserva, cliente, habitacion, fec_checkin, fec_checkout))
        else:
            lista_reservas.agregar_reserva(Reserva(nroreserva, cliente, habitacion, fec_checkin, fec_checkout))
    historico_general_reservas(pila_reservas)
    return lista_reservas

# Extrae la informacion de la pila y la almacena en el txt   
def historico_general_reservas(pila_reservas):
    historico_gral_reservas = open('txt/historico_gral_reservas.txt', 'a')
    while pila_reservas:
        reserva = pila_reservas.pop()
        historico_gral_reservas.write(f'{reserva.nroreserva},{reserva.cliente.dni},{reserva.habitacion.numero},{reserva.fec_checkin},{reserva.fec_checkout}\n')
    historico_gral_reservas.close()

# Las funciones load se encargan de actualizar o sobreescribir (dependiendo el caso) los archivos txt, que en un principio de codigo
# leimos para obtener la informacion, para que todos los cambios realizados perduren en el tiempo.

def load_hotel(hotel):
    load_reservas_activas(hotel)
    load_habitaciones(hotel)
    load_administrador(hotel)

# Carga al archivo txt de reservas activas la informacion de las reservas almacenadas en la lista enlazada    
def load_reservas_activas(hotel):
    lista_reservas_activas = hotel.lista_reservas_activas
    reserva_movil = lista_reservas_activas.cabeza
    archivo_reservas = open('txt/reservas_activas.txt', 'w')
    while reserva_movil is not None:
        archivo_reservas.write(f'{reserva_movil.nroreserva},{reserva_movil.cliente.dni},{reserva_movil.habitacion.numero},{reserva_movil.fec_checkin},{reserva_movil.fec_checkout}\n')
        reserva_movil = reserva_movil.prox
    archivo_reservas.close()

# Carga al archivo txt de habitaciones todas las habitaciones de la lista
def load_habitaciones(hotel):
    lista_habitaciones = hotel.lista_habitaciones
    archivo_habitaciones = open('txt/habitaciones.txt', 'w')
    for habitacion in lista_habitaciones:
        archivo_habitaciones.write(f'{habitacion.numero},{habitacion.capacidad_max},{habitacion.tipo},{habitacion.precio_noche},{habitacion.bano_privado},{habitacion.ventana_balcon}\n')
    archivo_habitaciones.close()

# Carga al archivo txt de administrador los datos del mismo.
def load_administrador(hotel):
    admin = hotel.admin
    archivo_administrador = open('txt/administrador.txt', 'w')
    archivo_administrador.write(f'{admin.tipo_usuario},{admin.dni},{admin.nombre},{admin.contra},{admin.fec_nac},{admin.genero},{admin.tel},{admin.mail},{admin.domicilio},{admin.fec_alta},{admin.fec_baja},{admin.cuil},{admin.sueldo}')  

# Carga al archivo txt de clientes todos los clientes de la lista
def load_clientes(lista_clientes):
    archivo_clientes = open('txt/clientes.txt', 'w')
    for cliente in lista_clientes:
        archivo_clientes.write(f'{cliente.tipo_usuario},{cliente.dni},{cliente.nombre},{cliente.contra},{cliente.fec_nac},{cliente.genero},{cliente.tel},{cliente.mail},{cliente.domicilio},{cliente.fec_alta},{cliente.historico_gastos}\n')    
    archivo_clientes.close()

def load_personal(lista_administrativo, lista_mantenimiento, lista_limpieza):
    load_administrativo(lista_administrativo)
    load_mantenimiento(lista_mantenimiento)
    load_limpieza(lista_limpieza)

# Carga al archivo txt de empleados de mantenimiento todos los empleados de mantenimiento.
def load_administrativo(lista_administrativo):
    archivo_administrativo = open('txt/administrativo.txt', 'w')
    for administrativo in lista_administrativo:
        archivo_administrativo.write(f'{administrativo.tipo_usuario},{administrativo.dni},{administrativo.nombre},{administrativo.contra},{administrativo.fec_nac},{administrativo.genero},{administrativo.tel},{administrativo.mail},{administrativo.domicilio},{administrativo.fec_alta},{administrativo.fec_baja},{administrativo.cuil},{administrativo.sueldo}\n')
    archivo_administrativo.close()

# Carga al archivo txt de empleados de limpieza todos los empleados de limpieza.
def load_limpieza(lista_limpieza):
    archivo_limpieza = open('txt/limpieza.txt', 'w')
    for limpieza in lista_limpieza:
        archivo_limpieza.write(f'{limpieza.tipo_usuario},{limpieza.dni},{limpieza.nombre},{limpieza.contra},{limpieza.fec_nac},{limpieza.genero},{limpieza.tel},{limpieza.mail},{limpieza.domicilio},{limpieza.fec_alta},{limpieza.fec_baja},{limpieza.cuil},{limpieza.sueldo},{limpieza.disponibilidad},{limpieza.fichar}\n')
    archivo_limpieza.close()

# Carga al archivo txt de empleados de mantenimiento todos los empleados de mantenimiento.
def load_mantenimiento(lista_mantenimiento):
    archivo_mantenimiento = open('txt/mantenimiento.txt', 'w')
    for mantenimiento in lista_mantenimiento:
        archivo_mantenimiento.write(f'{mantenimiento.tipo_usuario},{mantenimiento.dni},{mantenimiento.nombre},{mantenimiento.contra},{mantenimiento.fec_nac},{mantenimiento.genero},{mantenimiento.tel},{mantenimiento.mail},{mantenimiento.domicilio},{mantenimiento.fec_alta},{mantenimiento.fec_baja},{mantenimiento.cuil},{mantenimiento.sueldo},{mantenimiento.disponibilidad},{mantenimiento.fichar}\n')
    archivo_mantenimiento.close()
