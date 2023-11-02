from usuario.personal import Personal

class Mantenimiento(Personal):
    def __init__(self, tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad:bool = True):
        super().__init__(tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
        self.disponibilidad= disponibilidad