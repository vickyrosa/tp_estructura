class Buffet():
    def __init__(self):    
        self.menu = {'Desayuno': 2000,
                    'Almuerzo': 3000,
                    'Merienda': 2000,
                    'Cena': 3000,
                    'Bebida': 1000,
                    'Snack' :1000}
     
    # Para mostrar el menu cada vez cada llamamos a el metodo. 
    def mostrar_menu(self):
        for key in self.menu.keys():
            print(f'{key} -> ${self.menu[key]}')
    
    # Los pedidos se preparan segun ingresaron a la cola.
    def procesar_pedidos(self, cola_pedidos):
        while cola_pedidos:
            pedido = cola_pedidos.popleft()
            print(f"El pedido de '{pedido}' fue enviado a la cocina")
        print('La orden ya esta lista, retirar por mostrador')

        



