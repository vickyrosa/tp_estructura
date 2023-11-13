import datetime

def metodo_de_pago(hotel, ingreso):
    while True:
        opcion = input('''Seleccione un metodo de pago:
                    a. Efectivo
                    b. Tarjeta
                    
                    ''').strip().lower()
        match opcion:
            case 'a':
                efectivo()
                load_ingresos(hotel, ingreso)
                break
            case 'b':
                if ingresar_tarjeta():
                    print('Pago realizado con exito.')
                    load_ingresos(hotel, ingreso)
                    break
                else:
                    pass
            case _:
                print('Por favor elija una de las opciones ( a | b )')

def efectivo():
    print('Pago realizado con exito.')

def ingresar_tarjeta():
    while True:
        try:
            digitos = input('Ingrese los digitos de su tarjeta sin espacios: ').strip()
            if len(digitos) != 16:
                raise ValueError("La tarjeta debe tener 16 digitos")
            if not digitos.isdigit():
                raise ValueError('La tarjeta solo puede contener numeros')
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            mes, ano = map(int,input("Ingrese mes y fecha de vencimiento en formato MM/AA: ").split("/"))
            fec_venc = datetime.datetime.strptime(f'{10}/{mes}/{ano}', '%d/%m/%y')
            break
        except:
            print('Por favor ingrese una fecha valida y en el formato pedido (Ej: 10/23)')
    mes_y_ano_ahora = datetime.datetime.strptime(f'{10}/{datetime.date.today().month}/{datetime.date.today().strftime("%y")}', '%d/%m/%y')
    if fec_venc < mes_y_ano_ahora:
        print('La tarjeta esta vencida, por favor seleccione otro metodo de pago o ingrese otra tarjeta')
        return False
    return True
        
def load_ingresos(hotel, ingreso):
    ingreso = int(ingreso)
    fecha_hoy = datetime.datetime.now().strftime('%d/%m/%Y')
    with open('txt/ingresos_diarios_aux.txt', 'r') as archivo_aux:
        fecha = archivo_aux.read(10)
    if fecha_hoy == fecha:
        hotel.ingresos_diarios += ingreso
        with open('txt/ingresos_diarios_aux.txt', 'w') as archivo_aux:
            archivo_aux.write(f"{fecha_hoy},{hotel.ingresos_diarios}")
    else:
        with open('txt/ingresos_diarios.txt', 'a') as archivo_ingresos:
            archivo_ingresos.write(f"Fecha: {fecha} - Ingresos Totales: {hotel.ingresos_diarios}\n\n")
        hotel.ingresos_diarios = ingreso
        with open('txt/ingresos_diarios_aux.txt', 'w') as archivo_aux:
            archivo_aux.write(f"{fecha_hoy},{hotel.ingresos_diarios}")