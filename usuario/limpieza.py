from usuario.personal import Personal

class Limpieza(Personal):  #    HACER   metodo para iniciar trabajo y otro para terminarlo
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad:bool = True):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
        self.disponibilidad= disponibilidad
        
    def iniciar_trabajo(self):
        if Limpieza.disponibilidad:
            self.disponibilidad = False
        else:
            return("No hay personal disponible")
    def finalizar_trabajo(self):
        self.disponibilidad = True