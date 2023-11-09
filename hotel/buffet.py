from usuario.usuario import Usuario
from usuario.cliente import Cliente


class Buffet():
    def __init__(self, menu):    
        # Crea el menu vacio
        self.menu = menu
    def agregar_comida(self, item, precio_item):
        
        # Se fija que si no hay comidas en el menu, crea uno. Si hay comidas lo agrega junto con su precio.
        # Checkea que este bien el formato del dato (NO SE SI ES NECESARIO)
        if type(precio_item) == int and type(item) == str:
            if len(self.menu) == 0:
                self.menu = {item: precio_item}
            else:
                if item in self.menu.keys:
                    
                    # Si el item a agregar ya esta en el menu devuelve error (ACA VA A TENER QUE HABER UNA OPCION QUE TE DEJE VOLVER AL MENU)
                    return "El item que quiere agregar ya se encuentra en el menu"
                else:
                    self.menu[item] = precio_item
        else: 
            return "Introduzca un formato correcto"  ## ACA HAY QUE VOLVER AL MENU (QUE NO EXISTE POR AHORA)
    def remover_comida(self, item):
        
        # Borra una comida determinada que le pase. Si el menu esta vacio o no esta el item devuelve error (idem caso anterior).
        # Si encuentra el item lo borra. 
        if type(item) == str:
            if len(self.menu) == 0:
                return "El menu se encuentra vacio"
            else:
                if item in self.menu.keys:
                    self.menu.pop(item)
                else:
                    return "El item que quiere borrar no existe"
        else: 
            return "Introduzca un formato correcto"  ## ACA HAY QUE VOLVER AL MENU (QUE NO EXISTE POR AHORA)
    def modificar_precio_comida(self,item,nuevo_precio_item):
        
        # Le doy una comida y modifico el precio (TENGO QUE HACER UNA OPCION PARA DARLE UN PRECIO Y CAMBIAR EL ITEM? no tiene sentido me parece)
        if type(nuevo_precio_item) == int and type(item) == str:
            if len(self.menu) == 0: #No hay comidas entonces no puedo cambiar nada.
                return "No puede modificar el precio ya que no hay ninguna comida en el menu"
            else:
                if item in self.menu.keys:
                    self.menu.update({item:nuevo_precio_item})
                else:   #No encontro el item que le pase.
                    return "No puede modificar el precio ya que no se encuentra la comida en el menu"
        else: 
            return "Introduzca un formato correcto"  ## ACA HAY QUE VOLVER AL MENU (QUE NO EXISTE POR AHORA)
    def __str__(self):
        # Printeo el diccionario entero
        return self.menu
    def  ver_precio_comida(self, item):
        ## Para cuando se instancia cliente.ordenar() acceder al precio del item.
        return self.menu.get(item)
    
    #### HAGO EL MENU PERO NO VA ACA

    def ordenar_menu(self, cliente):
        print('Menu del buffet\n========')
        Buffet.__str__()
        total = 0
        while True:
            print("Menu del buffet:")
            Buffet.__str__()
            ans = input("Selecione lo que quiera ordenar (Escriba 'salir' si ya no desea ordenar ): ")
            ans = ans.lower().strip()
            if ans == 'salir':
                break
            elif ans in self.menu:
                total += self.menu[ans]
                print(f"Ordenaste {ans}. Su comida llegara pronto")
                cliente.historico_gastos += total
            else:
                print("Ese plato no esta en el menu. Por favor, elija un plato del menu.")
        print(f'Precio total: {total}')
                    


