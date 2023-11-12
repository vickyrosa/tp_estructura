class Hotel():
    def __init__(self, admin, lista_habitaciones, lista_reservas_activas, ingresos_diarios, nombre = 'Hotel POO'):
        self.admin = admin
        # Va a ser una lista con las habitaciones
        self.lista_habitaciones = lista_habitaciones
        self.lista_reservas_activas = lista_reservas_activas
        self.nombre = nombre
        
    def __str__(self):
        return f'{self.nombre}'


  
