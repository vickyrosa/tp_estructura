from usuario.personal import Personal

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