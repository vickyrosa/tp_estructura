from usuario.personal import Personal
import datetime

class Limpieza(Personal):  #    HACER   metodo para iniciar trabajo y otro para terminarlo
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
        self.disponibilidad = disponibilidad == 'True'
        
    def finalizar_tarea(self):
        if self.disponibilidad == False:
            self.disponibilidad = True
            print('Tarea finalizada con exito')
        else:
            return "No estaba realizando ninguna tarea actualmente"
        
    def fichar_ingreso(self):
        fichas_ingreso = open('tp_estructura/txt/fichas_ingreso.txt', 'a')
        fichas_ingreso.write(f'{self.dni},{datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n')
        fichas_ingreso.close()
        print('Se registro su hora de llegada a las ',datetime.datetime.now().strftime("%d/%m/%y %H:%M"))  

    def fichar_egreso(self):
        fichas_egreso = open('tp_estructura/txt/fichas_egreso.txt', 'a')
        fichas_egreso.write(f'{self.dni},{datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n')
        fichas_egreso.close()
        print('Se registro su hora de salida a las ',datetime.datetime.now().strftime("%d/%m/%y %H:%M"))