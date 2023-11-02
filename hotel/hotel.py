class Hotel():
    def __init__(self, admin, lista_habitaciones, nombre = 'Hotel POO'):
        self.admin = admin
        # Va a ser una lista con las habitaciones
        self.lista_habitaciones = lista_habitaciones
        
    def __str__(self):
        return f'{self.nombre}'
    hpla
    def porcentaje_ocupacion(self, por_tipo = False):
        # Voy a cambiar esto, porque lo hice al principio sin tener en cuenta cosas como el txt
        # Si el usuario no especifica nada simplemente nos va a dar el porcentaje de ocupacion
        # Si el usuario ingresa True va a darnos el porcentaje de ocupacion por tipo
        # Ver si convene agregar set para ver las habitaciones disponibles
        # OJO! Capaz es mejor hacer dos funciones diferentes y que el usuario desde el menu pueda elegir
        cont_disponibles = 0
        dict_tipos = {'Disponible':{'Simple':0, 'Doble':0, 'Suite':0, 'Familiar':0}, 'Total':{'Simple':0, 'Doble':0, 'Suite':0, 'Familiar':0}}
        if por_tipo == False:
            for habitacion in self.lista_habitaciones:
                if habitacion.esta_disponible():
                    cont_disponible += 1
            print(f'Estan ocupados {(1-(cont_disponibles/len(self.lista_habitaciones)))*100}% de cuartos del hotel')
            return {(1-(cont_disponibles/len(self.lista_habitaciones)))*100}
        else:
            for habitacion in self.lista_habitaciones:
                dict_tipos['Total'][habitacion.tipo] += 1
                if habitacion.esta_disponible():
                    dict_tipos['Disponible'][habitacion.tipo] += 1
            for key in dict_tipos['Total'].keys:
                print(f'''Tipo habitacion: {key}
                      Porcentaje de ocupación: {(1-dict_tipos['Disponible'][key]/dict_tipos['Total'][key])*100}%''')

  
