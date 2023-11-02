from usuario.cliente import Cliente
from usuario.administrativo import Administrativo
from usuario.administrador import Administrador
from usuario.mantenimiento import Mantenimiento
from usuario.limpieza import Limpieza
from hotel.habitacion import Habitacion
from hotel.hotel import Hotel
import funciones.checks as checks
import datetime
from hotel.lista_reservas import Lista_Reservas
from hotel.habitacion import Habitacion
from hotel.reservas import Reserva

# IMPORTANTE! Es probable que sea mejor crear varios archivos.py segun el tipo de funciones que son asi esta mas organizado y
# funciones auxiliares no queda gigante por ejemplo separar en: fciones_login, fciones_signin, fciones_load, fciones_auxiliares, etc.

def load_hotel():
    lista_habitaciones = list()
    with open('txt/habitaciones.txt', 'r') as archivo_habitaciones:
        lista_info_habitaciones = archivo_habitaciones.readlines()
        for i in range(len(lista_info_habitaciones)):
            numero, tipo, precio_noche, bano_privado, ventana_balcon, disponible = lista_info_habitaciones[i].strip().split(',')
            lista_habitaciones.append(Habitacion(numero, tipo, precio_noche, bano_privado, ventana_balcon, disponible))
    admin = Administrador('Administrador','1','Jefe','jefe123','40','M','123456','jefe@hotel.com','a1','01/01/1990',None,'123','10000')
    hotel = Hotel(admin, lista_habitaciones)

def load_clientes():    #Devuelve una lista con toda la informacion de los clientes contenida en el .txt.
    lista_clientes = list()
    with open('txt/clientes.txt', 'r') as archivo_clientes:
        lista_info_clientes = archivo_clientes.readlines()
        for i in range(len(lista_info_clientes)):
            tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, historico_gastos = lista_info_clientes[i].strip().split(',')
            lista_clientes.append(Cliente(tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, historico_gastos))
    return lista_clientes

def load_personal():    #Devuelve toda la informacion del personal separada por sectores.
    lista_administrativo = load_administrativo()
    lista_mantenimiento = load_mantenimiento()
    lista_limpieza = load_limpieza()
    
    return lista_administrativo, lista_mantenimiento, lista_limpieza

def load_administrativo():      #Devuelve una lista con toda la informacion del personal administrativo contenida en el .txt.
    lista_administrativo = list()
    with open('txt/administrativo.txt', 'r') as archivo_administrativo:
        lista_info_administrativo = archivo_administrativo.readlines()
        for i in range(len(lista_info_administrativo)):
            tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo = lista_info_administrativo[i].strip().split(',')
            lista_administrativo.append(Administrativo(tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo))
    return lista_administrativo

def load_mantenimiento():   #Devuelve una lista con toda la informacion del personal de mantenimiento contenida en el .txt.
    lista_mantenimiento = list()
    with open('txt/mantenimiento.txt', 'r') as archivo_mantenimiento:
        lista_info_mantenimiento = archivo_mantenimiento.readlines()
        for i in range(len(lista_info_mantenimiento)):
            tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad = lista_info_mantenimiento[i].strip().split(',')
            lista_mantenimiento.append(Mantenimiento(tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad))
    return lista_mantenimiento

def load_limpieza():    #Devuelve una lista con toda la informacion del personal de limpieza contenida en el .txt.
    lista_limpieza = list()
    with open('txt/limpieza.txt', 'r') as archivo_limpieza:
        lista_info_limpieza = archivo_limpieza.readlines()
        for i in range(len(lista_info_limpieza)):
            tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad = lista_info_limpieza[i].strip().split(',')
            lista_limpieza.append(Limpieza(tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad))
    return lista_limpieza

#Las siguientes funciones se utilizan cuando se requiera que el usuario ingrese informacion.

def pedir_dni():
    return input('Ingrese su DNI: ')
        
def pedir_nombre():
    return input('Ingrese su nombre: ')

def pedir_contra():
    return input('Ingrese su contraseña: ')

def pedir_edad():
    return input('Ingrese su edad: ')

def pedir_sexo():
    return input('Ingrese su sexo: ')

def pedir_telefono():
    return input('Ingrese su numero de telefono: ')

def pedir_mail():
    return input('Ingrese su mail: ')

def pedir_domicilio():
    return input('Ingrese su domicilio: ')

def pedir_cuil():
    return input('Ingrese su numero de CUIL: ')

def pedir_sueldo():
    return input('Ingrese sueldo: ')

# Le asignamos a variables la informacion del usuario mediante los metodos creados anteriormente.
def pedir_datos_basicos_sing_in(lista):
    while True:
        dni = pedir_dni()
        
        # Con este check verificamos que el dni que ingresa el cliente no exista en la base de datos
        if checks.check_dni(lista, dni) == True:
            break
        print('El DNI ingresado ya existe en la base de datos, porfavor ingrese uno nuevo.')
    nombre = pedir_nombre()
    edad = pedir_edad()
    sexo = pedir_sexo()
    tel = pedir_telefono()
    mail = pedir_mail()
    domicilio = pedir_domicilio()
    contra = pedir_contra()
    fec_alta = datetime.datetime.now().strftime('%d/%m/%y')
    return dni, nombre, contra, edad, sexo, tel, mail, domicilio, fec_alta

# Con las variables del metodo anterior anadimos a nuestra "base de datos" al usuario creado.
def sign_in_cliente(lista_clientes):
    dni, nombre, contra, edad, sexo, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in(lista_clientes)
    tipo_usuario = 'Cliente'
    
    # Una vez que cargo todos los datos, lo agrego a la base de datos
    with open('txt/clientes.txt', 'a') as archivo_clientes:
        archivo_clientes.write(f'{tipo_usuario},{dni},{nombre},{contra},{edad},{sexo},{tel},{mail},{domicilio},{fec_alta},{0}\n')
    print(f'El usuario del cliente {nombre} con DNI: {dni} fue creado satisfactoriamente.')
    
    # Agregamos esto porque cuando pusimos:
    # -> print(f'El usuario del cliente {nombre} con DNI: {dni} fue creado satisfactoriamente.', end = '\n') <-
    # no funcionaba bien. Y queriamos que al volver al menu se vea un espacio, por una cuestion de prolijidad y estetica para el usuario.
    
    print('')

# Dejo hecha la base queda hacerle el final nomas

def sign_in_administrativo(lista_administrativo):
    dni, nombre, contra, edad, sexo, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in(lista_administrativo)
    tipo_usuario = 'Administrativo'
    cuil = pedir_cuil()
    sueldo = pedir_sueldo()
    with open('txt/administrativo.txt', 'a') as archivo_administrativo:
        archivo_administrativo.write(f'{tipo_usuario},{dni},{nombre},{contra},{edad},{sexo},{tel},{mail},{domicilio},{fec_alta},{None},{cuil},{sueldo}\n')
    print(f'El usuario del empleado administrativo {nombre} con DNI: {dni} fue creado satisfactoriamente.')
    
def sign_in_mantenimiento(lista_mantenimiento):
    dni, nombre, contra, edad, sexo, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in(lista_mantenimiento)
    tipo_usuario = 'Mantenimiento'
    cuil = pedir_cuil()
    sueldo = pedir_sueldo()
    with open('txt/mantenimiento.txt', 'a') as archivo_mantenimiento:
        archivo_mantenimiento.write(f'{tipo_usuario},{dni},{nombre},{contra},{edad},{sexo},{tel},{mail},{domicilio},{fec_alta},{None},{cuil},{sueldo},{True}\n')
    print(f'El usuario del empleado de mantenimiento {nombre} con DNI: {dni} fue creado satisfactoriamente.')
    
def sign_in_limpieza(lista_limpieza):
    dni, nombre, contra, edad, sexo, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in(lista_limpieza)
    tipo_usuario = 'Limpieza'
    cuil = pedir_cuil()
    sueldo = pedir_sueldo()
    with open('txt/limpieza.txt', 'a') as archivo_limpieza:
        archivo_limpieza.write(f'{tipo_usuario},{dni},{nombre},{contra},{edad},{sexo},{tel},{mail},{domicilio},{fec_alta},{None},{cuil},{sueldo},{True}\n')
    print(f'El usuario del empleado de limpieza {nombre} con DNI: {dni} fue creado satisfactoriamente.')

def buscar_usuario(lista, dni, contra):
    for persona in lista:
        if persona.dni == dni and persona.contra == contra:
            return persona
    return None

def log_in(lista_clientes, lista_administrativo, lista_mantenimiento, lista_limpieza):
    dni = pedir_dni()
    contra = pedir_contra()
    usuario = buscar_usuario(lista_clientes, dni, contra)
    if usuario == None:
       usuario = buscar_usuario(lista_administrativo, dni, contra)
       if usuario == None:
           usuario = buscar_usuario(lista_mantenimiento, dni, contra)
           if usuario == None:
               usuario = buscar_usuario(lista_limpieza, dni, contra)
               if usuario == None:
                   print('El dni o contraseña ingresados no son correctos.')
    return usuario
def lista_reservas_actuales(habitacion):
##levantar una lista que tenga fechas checkin checkout por la habitacion que yo le pase
    listareservas = []
    return listareservas













def disponibilidad(fec_checkin, fec_checkout, habitacion):
    lista_reservas_x_hab = lista_reservas_actuales(habitacion)
    if fec_checkin < lista_reservas_x_hab[0] and fec_checkout < lista_reservas_x_hab[0]:
        return True
    i = 2
    while i < lista_reservas_x_hab.len():
        if fec_checkin > lista_reservas_x_hab[i-1] and fec_checkout < lista_reservas_x_hab[i]:
            return True
        i += 2
    return False
