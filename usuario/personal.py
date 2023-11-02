from usuario.usuario import Usuario
import datetime

class Personal(Usuario):
    def __init__(self, tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo):   
        super().__init__(tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta)
        self.fec_baja=fec_baja
        self.cuil = cuil
        self.sueldo = sueldo

    def fichar_ingreso(self):
        fichas_ingreso = open('tp_estructura/txt/fichas_ingreso.txt', 'a')
        fichas_ingreso.write(f'{self.dni},{datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n')
        fichas_ingreso.close()

    def fichar_egreso(self):
        fichas_egreso = open('tp_estructura/txt/fichas_egreso.txt', 'a')
        fichas_egreso.write(f'{self.dni},{datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n')
        fichas_egreso.close()
    