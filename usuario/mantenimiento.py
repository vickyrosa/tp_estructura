from usuario.personal import Personal

class Mantenimiento(Personal):
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo, disponibilidad):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
        # Transformamos el txt a bool (porque de poner bool(disponibilidad), al ser un str, siempre sera True)
        self.disponibilidad = disponibilidad == 'True'

    def finalizar_tarea(self):
        if self.disponibilidad == False:
            self.disponibilidad = True
            print('Tarea finalizada con exito')
        else:
            return "No estaba realizando ninguna tarea actualmente"