from usuario.personal import Personal
from hotel.hotel import Hotel
from hotel.lista_reservas import Lista_Reservas
import datetime

class Administrador(Personal):
    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta, fec_baja, cuil, sueldo)
        
    def porcentaje_ocupacion(self):
        # Voy a cambiar esto, porque lo hice al principio sin tener en cuenta cosas como el txt
        # Lo termino manana, pero basicamente es recorrer la lista de reservas accediendo asi Hotel.lista_reservas_activas
        cont_disponibles = 0
        dict_tipos = {'Disponible':{'Simple':0, 'Doble':0, 'Suite':0, 'Familiar':0}, 'Total':{'Simple':0, 'Doble':0, 'Suite':0, 'Familiar':0}}
        for habitacion in self.lista_habitaciones:
            if habitacion.esta_disponible():
                cont_disponible += 1
        print(f'Estan ocupados {(1-(cont_disponibles/len(self.lista_habitaciones)))*100}% de cuartos del hotel')
        return {(1-(cont_disponibles/len(self.lista_habitaciones)))*100}
    
    def porcentaje_ocupacion_portipo(self):
        dict_tipos = {'Disponible':{'Simple':0, 'Doble':0, 'Suite':0, 'Familiar':0}, 'Total':{'Simple':0, 'Doble':0, 'Suite':0, 'Familiar':0}}
        for habitacion in self.lista_habitaciones:
            dict_tipos['Total'][habitacion.tipo] += 1
            if habitacion.esta_disponible():
                dict_tipos['Disponible'][habitacion.tipo] += 1
        for key in dict_tipos['Total'].keys:
            print(f'''Tipo habitacion: {key}
                    Porcentaje de ocupación: {(1-dict_tipos['Disponible'][key]/dict_tipos['Total'][key])*100}%''')
    def despedir_personal(self, personal):
        personal.fec_baja = datetime.now()
        return f"Ha sido despedido correctamente {personal.nombre} {personal.apellido}" 
        
            
            