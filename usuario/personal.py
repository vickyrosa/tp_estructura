from usuario.usuario import Usuario

class Personal(Usuario):
    
    set_cuil = set()
    
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, fec_baja, cuil, sueldo):   
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta)
        self.fec_baja=fec_baja
        self.cuil = cuil
        self.set_cuil.add(cuil)
        self.sueldo = sueldo

        
    