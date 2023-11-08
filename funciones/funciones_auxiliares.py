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
from usuario.usuario import Usuario
from collections import deque

# IMPORTANTE! Es probable que sea mejor crear varios archivos.py segun el tipo de funciones que son asi esta mas organizado y
# funciones auxiliares no queda gigante por ejemplo separar en: fciones_login, fciones_signin, fciones_load, fciones_auxiliares, etc.

def download_hotel(lista_clientes):
    lista_habitaciones = download_habitaciones()
    lista_reservas_activas = download_reservas_activas(lista_clientes, lista_habitaciones)
    admin = download_administrador()
    hotel = Hotel(admin, lista_habitaciones, lista_reservas_activas)
    return hotel

def download_administrador():
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
        lista_clientes.append(Cliente(tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, historico_gastos))
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
        tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad = lista_info_mantenimiento[i].strip().split(',')
        lista_mantenimiento.append(Mantenimiento(tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad))
    return lista_mantenimiento

def download_limpieza():    #Devuelve una lista con toda la informacion del personal de limpieza contenida en el .txt.
    lista_limpieza = list()
    with open('txt/limpieza.txt', 'r') as archivo_limpieza:
        lista_info_limpieza = archivo_limpieza.readlines()
    for i in range(len(lista_info_limpieza)):
        tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad = lista_info_limpieza[i].strip().split(',')
        lista_limpieza.append(Limpieza(tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad))
    return lista_limpieza

def download_habitaciones():
    lista_habitaciones = list()
    with open('txt/habitaciones.txt', 'r') as archivo_habitaciones:
        lista_info_habitaciones = archivo_habitaciones.readlines()
    for i in range(len(lista_info_habitaciones)):
        numero, tipo, precio_noche, bano_privado, ventana_balcon, disponible = lista_info_habitaciones[i].strip().split(',')
        lista_habitaciones.append(Habitacion(numero, tipo, precio_noche, bano_privado, ventana_balcon, disponible))
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
        if datetime.datetime.strptime(fec_checkout, '%d/%m/%Y') < datetime.datetime.today():
            pila_reservas.append(Reserva(nroreserva, cliente, habitacion, fec_checkin, fec_checkout))
        else:
            lista_reservas.agregar_reserva(Reserva(nroreserva, cliente, habitacion, fec_checkin, fec_checkout))
    historico_general_reservas(pila_reservas)
    return lista_reservas
    
def historico_general_reservas(pila_reservas):
    historico_gral_reservas = open('txt/historico_gral_reservas.txt', 'a')
    while pila_reservas:
        reserva = pila_reservas.pop()
        historico_gral_reservas.write(f'{reserva.nroreserva},{reserva.cliente.dni},{reserva.habitacion.numero},{reserva.fec_checkin},{reserva.fec_checkout}\n')
    historico_gral_reservas.close()
#Las siguientes funciones se utilizan cuando se requiera que el usuario ingrese informacion.

#Cambie la funcion de pedir dni para no usar check sino set, asi metemos esa estructura
#el set esta guardado en la clase Usuario 

#el check que hay para dni mas abajo no lo borre porque se puede usar para otra cosa

def pedir_dni ():
    while True:
        try:
            dni = input('Ingrese su DNI: ').strip()
            if not dni.isnumeric():
                raise ValueError("DNI debe tener caracteres numéricos.")
            if len(dni) != 8:
                raise ValueError("El DNI debe contener 8 digitos")
            return dni  # Me devuelve el DNI validado
        except ValueError as e:
            print(e)

def pedir_nombre():
    while True:
        nombre = input('Ingrese su nombre y apellido (Ej: Felipe Martin Oyerzabal): ').strip()
        try:
            for letra in nombre:
                if letra.isdigit():
                    raise ValueError("El nombre no puede tener caracteres numericos.")
            return nombre
        except ValueError as e:
            print(e)

def pedir_contra():
    return input('Ingrese su contraseña: ').strip()

def pedir_fec_nac():
    while True:
        fec_nac_str = input("Ingrese fecha de nacimiento en formato DD/MM/YYYY: ").strip()
        try:
            fec_nac = datetime.datetime.strptime(fec_nac_str, '%d/%m/%Y')
            hoy = datetime.datetime.today().strftime('%d/%m/%Y')
            hoy = datetime.datetime.strptime(hoy, '%d/%m/%Y')
            # Calcula edad
            edad = hoy.year - fec_nac.year - ((hoy.month, hoy.day) < (fec_nac.month, fec_nac.day))
            if edad >= 18:
                fec_nac = fec_nac.strftime('%d/%m/%Y')
                return fec_nac
            else:
                print("Debe tener más de 18 años para ingresar.")  
        except ValueError:
            print("""Formato de fecha invalido. 
                  Por favor ingrese su fecha de nacimiento en el formato DD/MM/YYYY.""")

def pedir_genero():
    while True:
        genero = input("Ingrese su género (F para femenino, M para masculino, O para otro): ").upper().strip()
        if genero in ["F", "M", "O"]:
            return genero
        else:
            print("Género no válido. Por favor, ingrese 'F' para femenino, 'M' para masculino o 'O' para otro.")

def pedir_telefono():
    return input('Ingrese su numero de telefono: ').strip()

def pedir_mail():
    return input('Ingrese su mail: ').lower().strip()

def pedir_domicilio():
    return input('Ingrese su domicilio: ').strip()

def pedir_cuil():
    while True:
        cuil = input('Ingrese su numero de CUIL: ').strip()
        try:
            if not cuil.isnumeric():
                    raise ValueError("El CUIL debe tener caracteres numéricos.")
            if len(cuil) < 11:
                    raise ValueError("El CUIL debe contener al menos 11 digitos")
            if cuil in Usuario.set_cuil:
                raise ValueError("El CUIL ingresado ya existe. Por favor ingrese otro CUIL.")
            return cuil
        except ValueError as e:
            print(e)


def pedir_sueldo():
    return input('Ingrese sueldo: ').strip()

# Le asignamos a variables la informacion del usuario mediante los metodos creados anteriormente.


def pedir_datos_basicos_sing_in():
    while True:
        dni = pedir_dni()
        if dni in Usuario.set_dni:
            print("El DNI ingresado ya existe. Por favor ingrese otro DNI.")
        else:
            Usuario.set_dni.add(dni)  # Agrega DNI ingresado al set
            break      
    nombre = pedir_nombre()
    fec_nac = pedir_fec_nac()
    genero = pedir_genero()
    tel = pedir_telefono()     
    mail = pedir_mail()
    domicilio = pedir_domicilio()
    contra = pedir_contra()
    fec_alta = datetime.datetime.today().strftime('%d/%m/%Y')
    return dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta

# Con las variables del metodo anterior anadimos a nuestra "base de datos" al usuario creado.

def sign_in_cliente(lista_clientes):
    dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in()
    tipo_usuario = 'Cliente'
    lista_clientes.append(Cliente(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta,0))
    
    # Nomina cliente legible para personal del hotel
    nomina_cliente = open('txt/nomina_clientes.txt', 'a')
    nomina_cliente.write(f'{nombre}  {dni}  {tel}  {mail}\n')
    nomina_cliente.close()
    
def sign_in_administrativo(lista_administrativo):
    dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in()
    tipo_usuario = 'Administrativo'
    cuil = pedir_cuil()
    sueldo = pedir_sueldo()
    lista_administrativo.append(Administrativo(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo))
    
def sign_in_mantenimiento(lista_mantenimiento):
    dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in()
    tipo_usuario = 'Mantenimiento'
    cuil = pedir_cuil()
    sueldo = pedir_sueldo()
    lista_mantenimiento.append(Mantenimiento(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo))
    
def sign_in_limpieza(lista_limpieza):
    dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in()
    tipo_usuario = 'Limpieza'
    cuil = pedir_cuil()
    sueldo = pedir_sueldo()
    lista_limpieza.append(Limpieza(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo))

def buscar_usuario(lista, dni, contra):
    for persona in lista:
        if persona.dni == dni and persona.contra == contra:
            return persona
    return None

def log_in(lista_clientes, lista_administrativo, lista_mantenimiento, lista_limpieza, hotel):
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
                   if dni == hotel.admin.dni and contra == hotel.admin.contra:
                        usuario = hotel.admin
                   else:
                        print('El dni o contraseña ingresados no son correctos.')
    return usuario

def load_hotel(hotel):
    load_reservas_activas(hotel)
    load_habitaciones(hotel)
    load_administrador(hotel)
    
def load_reservas_activas(hotel):
    lista_reservas_activas = hotel.lista_reservas_activas
    reserva_movil = lista_reservas_activas.cabeza
    archivo_reservas = open('txt/reservas_activas.txt', 'w')
    while reserva_movil is not None:
        archivo_reservas.write(f'{reserva_movil.nroreserva},{reserva_movil.cliente.dni},{reserva_movil.habitacion.numero},{reserva_movil.fec_checkin},{reserva_movil.fec_checkout}\n')
        reserva_movil = reserva_movil.prox
    archivo_reservas.close()

def load_habitaciones(hotel):
    lista_habitaciones = hotel.lista_habitaciones
    archivo_habitaciones = open('txt/habitaciones.txt', 'w')
    for habitacion in lista_habitaciones:
        archivo_habitaciones.write(f'{habitacion.numero},{habitacion.tipo},{habitacion.precio_noche},{habitacion.bano_privado},{habitacion.ventana_balcon},{habitacion.disponible}\n')
    archivo_habitaciones.close()

def load_administrador(hotel):
    admin = hotel.admin
    archivo_administrador = open('txt/administrador.txt', 'w')
    archivo_administrador.write(f'{admin.tipo_usuario},{admin.dni},{admin.nombre},{admin.contra},{admin.fec_nac},{admin.genero},{admin.tel},{admin.mail},{admin.domicilio},{admin.fec_alta},{admin.fec_baja},{admin.cuil},{admin.sueldo}')
    

def load_clientes(lista_clientes):
    # Una vez que cerramos el programa, cargo todos los datos, lo agrego a la base de datos
    archivo_clientes = open('txt/clientes.txt', 'w')
    for cliente in lista_clientes:
        archivo_clientes.write(f'{cliente.tipo_usuario},{cliente.dni},{cliente.nombre},{cliente.contra},{cliente.fec_nac},{cliente.genero},{cliente.tel},{cliente.mail},{cliente.domicilio},{cliente.fec_alta},{cliente.historico_gastos}\n')    
    archivo_clientes.close()

def load_personal(lista_administrativo, lista_mantenimiento, lista_limpieza):
    load_administrativo(lista_administrativo)
    load_limpieza(lista_mantenimiento)
    load_mantenimiento(lista_limpieza)
    
def load_administrativo(lista_administrativo):
    archivo_administrativo = open('txt/administrativo.txt', 'w')
    for administrativo in lista_administrativo:
        archivo_administrativo.write(f'{administrativo.tipo_usuario},{administrativo.dni},{administrativo.nombre},{administrativo.contra},{administrativo.fec_nac},{administrativo.genero},{administrativo.tel},{administrativo.mail},{administrativo.domicilio},{administrativo.fec_alta},{administrativo.fec_baja},{administrativo.cuil},{administrativo.sueldo}\n')
    archivo_administrativo.close()

def load_limpieza(lista_limpieza):
    archivo_limpieza = open('txt/limpieza.txt', 'w')
    for limpieza in lista_limpieza:
        archivo_limpieza.write(f'{limpieza.tipo_usuario},{limpieza.dni},{limpieza.nombre},{limpieza.contra},{limpieza.fec_nac},{limpieza.genero},{limpieza.tel},{limpieza.mail},{limpieza.domicilio},{limpieza.fec_alta},{limpieza.fec_baja},{limpieza.cuil},{limpieza.sueldo},{limpieza.disponibilidad}\n')
    archivo_limpieza.close()

def load_mantenimiento(lista_mantenimiento):
    archivo_mantenimiento = open('txt/mantenimiento.txt', 'w')
    for mantenimiento in lista_mantenimiento:
        archivo_mantenimiento.write(f'{mantenimiento.tipo_usuario},{mantenimiento.dni},{mantenimiento.nombre},{mantenimiento.contra},{mantenimiento.fec_nac},{mantenimiento.genero},{mantenimiento.tel},{mantenimiento.mail},{mantenimiento.domicilio},{mantenimiento.fec_alta},{mantenimiento.fec_baja},{mantenimiento.cuil},{mantenimiento.sueldo},{mantenimiento.disponibilidad}\n')
    archivo_mantenimiento.close()