class Lista_Reservas:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
        
    # Metodo que agrega una reserva a la lsita enlazada
    def agregar_reserva(self, reserva):
        if self.cabeza is None:
            self.cabeza = reserva 
        else:
            actual = self.cabeza
            while actual.prox:
                actual = actual.prox
            actual.prox = reserva 
        self.tamanio+=1

    # Metodo que elimina una reserva de la lista enlazada tomando como dato su numero de reserva
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

    # Devuelve el largo de la lista enlazada
    def len_lista(self):
        return self.tamanio
    
   



        
        
    
