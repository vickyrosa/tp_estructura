#Las siguientes funciones se utilizan cuando se requiera que el usuario ingrese informacion.
import datetime
from usuario.usuario import Usuario
from usuario.cliente import Cliente
from usuario.mantenimiento import Mantenimiento
from usuario.limpieza import Limpieza
from usuario.administrativo import Administrativo


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
            print("Género no válido. Por favor, ingrese 'F' para femenino, 'M' para masculino u 'O' para otro.")

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
    
# def sign_in_administrativo(lista_administrativo):
#     dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in()
#     tipo_usuario = 'Administrativo'
#     cuil = pedir_cuil()
#     sueldo = pedir_sueldo()
#     lista_administrativo.append(Administrativo(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo))
    
# def sign_in_mantenimiento(lista_mantenimiento):
#     dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in()
#     tipo_usuario = 'Mantenimiento'
#     cuil = pedir_cuil()
#     sueldo = pedir_sueldo()
#     lista_mantenimiento.append(Mantenimiento(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo))
    
# def sign_in_limpieza(lista_limpieza):
#     dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta = pedir_datos_basicos_sing_in()
#     tipo_usuario = 'Limpieza'
#     cuil = pedir_cuil()
#     sueldo = pedir_sueldo()
#     lista_limpieza.append(Limpieza(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, None, cuil, sueldo))

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