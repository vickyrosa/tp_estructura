from usuario.usuario import Usuario

class Cliente(Usuario):

    def __init__(self, tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta, historico_gastos):
        super().__init__(tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta)
        self.historico_gastos = historico_gastos
    def categoria(self):
        #Historico gastos es una lista de ints?
        total = 0
        for gasto in self.historico_gastos:
            total += gasto
        match total:
            case [0,1000]:
                return "Su categoria es Baja"
            case [1000,10000]:
                return "Su categoria es Media"
            case _:
                return "Su categoria es Alta"
        