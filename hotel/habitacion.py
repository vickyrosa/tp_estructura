class Habitacion():
    def __init__(self, numero, capacidad_max, tipo, precio_noche, bano_privado:bool, ventana_balcon:bool):
        self.numero = numero
        self.capacidad_max = int(capacidad_max)
        self.tipo = tipo
        self.precio_noche = int(precio_noche)
        # Con estas lineas de codigo transformamos el str de los txt a bool
        self.bano_privado = bano_privado == 'True'
        self.ventana_balcon = ventana_balcon == 'True'
        
    def __str__(self):
        return f'''
    Habitacion número: {self.numero}
    Capacidad máxima de personas: {self.capacidad_max}
    Tipo: {self.tipo}
    Precio por noche: {self.precio_noche}
    Tiene baño privado: {self.bano_privado}
    Tiene ventana balcon: {self.ventana_balcon}'''
    
    def aumentar_precio(self, nuevo_precio):
        self.precio_noche = nuevo_precio
        return self.precio_noche
    
    def get_precio(self):
        return self.precio_noche
    
    def get_numero(self):
        return self.numero
    
    def get_tipo(self):
        return self.tipo
    
    def tiene_bano_privado(self):
        return self.bano_privado
    
    def tiene_ventana_balcon(self):
        return self.ventana_balcon

