import datetime

def metodo_de_pago():
    while True:
        opcion = input('''Seleccione un metodo de pago:
                    a. Efectivo
                    b. Tarjeta
                    
                    ''').strip().lower()
        match opcion:
            case 'a':
                efectivo()
                break
            case 'b':
                if ingresar_tarjeta():
                    print('Pago realizado con exito.')
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

