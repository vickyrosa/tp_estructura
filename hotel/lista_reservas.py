class Lista_Reservas:   #Creamos una lista enlazada de las reservas (Gran volumen de datos)
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def agregar_reserva(self, reserva):
        if self.cabeza is None:
            self.cabeza = reserva 
        else:
            actual = self.cabeza
            while actual.prox:
                actual = actual.prox
            actual.prox = reserva 
        self.tamanio+=1

    def eliminar_reserva(self, nroreserva):            
        if self.cabeza is None:                                 
            return                                               
        if self.cabeza.nroreserva == nroreserva:
            self.cabeza = self.cabeza.prox
            self.tamanio-=1
            return
        actual = self.cabeza
        while actual.prox:
            if actual.prox.nroreserva == nroreserva:
                actual.prox = actual.prox.prox
                self.tamanio-=1
                return
            actual = actual.prox

    def mostrar_reservas(self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.nroreserva}, Habitación: {actual.habitacion}, Llegada: {actual.fec_alta}, Salida: {actual.fec_baja}")
            actual = actual.prox
    
    def len_lista(self):
        return self.tamanio
    
   



        
        
    
