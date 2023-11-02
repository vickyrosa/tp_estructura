from usuario.personal import Personal

class Limpieza(Personal):  #    HACER   metodo para iniciar trabajo y otro para terminarlo
    def __init__(self, tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad:bool = True):
        super().__init__(tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
        self.disponibilidad= disponibilidad
        
    def iniciartrabajo(self):
        if Limpieza.disponibilidad:
            self.disponibilidad = False
        else:
            return("No hay personal disponible")
    def finalizartrabajo(self):
        self.disponibilidad = True