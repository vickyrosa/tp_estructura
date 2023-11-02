class Lista_Reservas:   #Creamos una lista enlazada de las reservas (Gran volumen de datos)
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def agregar_reserva(self, reserva):#nroreserva):
        #nueva_reserva = Reserva(nroreserva)
        if self.cabeza is None:
            self.cabeza = reserva #nueva_reserva
        else:
            actual = self.cabeza
            while actual.prox:
                actual = actual.prox
            actual.prox = reserva #nueva_reserva
        self.tamanio+=1

    def buscar_reserva(self, reserva):#nroreserva):
        actual = self.cabeza
        while actual:
            if actual.reserva == reserva:
            #if actual.nroreserva == nroreserva:
                return actual.data
            actual = actual.prox
        return None

    def eliminar_reserva(self, reserva):#nroreserva):
        if self.cabeza is None:
            return
        if self.cabeza.reserva == reserva:
        #if self.cabeza.nroreserva == nroreserva:
            self.cabeza = self.cabeza.prox
            return
        actual = self.cabeza
        while actual.prox:
            if actual.prox.reserva == reserva:
            #if actual.prox.nroreserva == nroreserva:
                actual.prox = actual.prox.prox
                return
            actual = actual.prox
        self.tamanio-=1

    def mostrar_reservas(self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.nroreserva}, Habitación: {actual.habitacion}, Llegada: {actual.fec_alta}, Salida: {actual.fec_baja}")
            actual = actual.prox
    
    def len_lista(self):
        return self.tamanio
    
    def historico_general_reservas(self):  #FALTAAAAAAAAA
        historico_gral_reservas = open('tp_estructura/txt/historico_gral_reservas.txt', 'a')
        for reserva in historico_gral_reservas:
            pass
        
        historico_gral_reservas.write(f'\n')
        historico_gral_reservas.close()
        

    
