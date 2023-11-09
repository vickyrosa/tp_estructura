from usuario.personal import Personal

class Mantenimiento(Personal):
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad:bool = True):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
        self.disponibilidad= disponibilidad
    def finalizar_trabajo(self):
        if self.disponibilidad == False:
            self.disponibilidad = True
        else:
            return "No estaba realizando ninguna tarea actualmente"
        