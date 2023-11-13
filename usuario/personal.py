from usuario.usuario import Usuario

class Personal(Usuario):
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo):   
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta)
        self.fec_baja=fec_baja
        self.cuil = cuil
        self.sueldo = sueldo

        
    