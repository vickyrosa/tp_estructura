from usuario.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, historico_gastos):
        super().__init__(tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta)
        self.historico_gastos = historico_gastos