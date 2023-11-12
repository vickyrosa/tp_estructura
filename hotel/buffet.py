# IMPORT METODO DE PAGO

class Buffet():
    def __init__(self):    
        self.menu = {'Desayuno': 2000,
                    'Almuerzo': 3000,
                    'Merienda': 2000,
                    'Cena': 3000,
                    'Bebida': 1000,
                    'Snack' :1000}
        
    def __str__(self):
        return self.menu

    def mostrar_menu(self):
        for key in self.menu.keys():
            print(f'{key} -> ${self.menu[key]}')
    
    def procesar_pedidos(self, cola_pedidos):
        while cola_pedidos:
            pedido = cola_pedidos.popleft()
            print(f"El pedido de '{pedido}' fue enviado a la cocina")
        print('La orden ya esta lista, retirar por mostrador')

        



