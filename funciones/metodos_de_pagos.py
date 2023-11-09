import datetime

def ingresar_tarjeta():
    while True:
        try:
            digitos = input('Ingrese los digitos de su tarjeta sin espacios: ').strip()
            if len(digitos) != 16:
                raise ValueError("Ingrese correctamente los digitos de su tarjeta")
            else:
                mes, ano = map(int,input("Ingrese mes y fecha de vencimiento en formato MM/AA: ").split("/"))
                fec_venc = datetime.date(mes, ano)
                if fec_venc > datetime.now():
                    raise ValueError("La tarjeta esta vencida")
                if fec_venc.isalpha():
                    raise ValueError("Ingrese mes y fecha de vecimiento en formato MM/AA")
            return digitos, # Me devuelve los digitos
        except ValueError as e:
            print(e)

