class Habitacion():
    # Agregamos aca gastos? Asi la persona va al buffet y cuando 'paga' se le acredita a la habitacion
    def __init__(self, numero, tipo, precio_noche, bano_privado:bool, ventana_balcon:bool, disponible:bool):
        self.numero = numero
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.bano_privado = bano_privado
        self.ventana_balcon = ventana_balcon
        self.disponible = disponible
        
    def __str__(self):
        return f'''
    Habitacion número: {self.numero}
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
    
    def esta_disponible(self):
        return self.disponible
