from usuario.personal import Personal
import datetime

class Mantenimiento(Personal):
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad, fichar):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
        # Transformamos el txt a bool (porque de poner bool(disponibilidad), al ser un str, siempre sera True)
        self.disponibilidad = disponibilidad == 'True'
        self.fichar = fichar == 'True'

    # Perminte al empleado marcar la realización de una tarea
    def finalizar_tarea(self):
        if self.disponibilidad == False:
            self.disponibilidad = True
            print('Tarea finalizada con exito')
        else:
            print("No estaba realizando ninguna tarea actualmente")

    # Permite fichar la hora y el dia del ingreso del empleado
    def fichar_ingreso(self):
        if self.fichar == True:
            fichas_ingreso = open('txt/fichas_ingreso.txt', 'a')
            fichas_ingreso.write(f'{self.dni},{datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n')
            fichas_ingreso.close()
            self.fichar = False
            print('Se registro su hora de llegada a las ',datetime.datetime.now().strftime("%d/%m/%y %H:%M"))
        else:
            print('Su ingreso fue fichado previamente.')

    # Permite fichar la hora y el dia del egreso del empleado
    def fichar_egreso(self):
        if self.fichar == False:
            fichas_egreso = open('txt/fichas_egreso.txt', 'a')
            fichas_egreso.write(f'{self.dni},{datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n')
            fichas_egreso.close()
            self.fichar = True
            print('Se registro su hora de salida a las ',datetime.datetime.now().strftime("%d/%m/%y %H:%M"))
        else:
            print('Su egreso fue fichado previamente.')