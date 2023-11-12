import datetime
from collections import deque



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
    
    #Guarda en un archivo txt las reservas que se efectuaron - LO DEJO COMO COMMENT XQ NOSE SI SE PUEDE BORRAR
    # def historico_general_reservas(self):
    #     fecha_actual = datetime.date.today()
    #     actual = self.cabeza
    #     historico_gral_reservas = open('tp_estructura/txt/historico_gral_reservas.txt', 'w')
    #     while actual:
    #         if actual.fec_checkout < fecha_actual: 
    #             historico_gral_reservas.write(f'{self.nroreserva},{self.cliente},{self.habitacion},{self.fec_checkin},{self.fec_checkout}\n')
    #     historico_gral_reservas.close()
    #     print("El historial de reservas fue guardado con exito en 'historico_gral_reservas.txt' ")  
        
        
    # def historico_general_reservas2(self):
    #     fecha_actual = datetime.date.today()
    #     actual = self.cabeza
    #     pila_reservas = deque()
    #     historico_gral_reservas = open('tp_estructura/txt/historico_gral_reservas2.txt', 'w')
        
    #     while actual:
    #         if actual.fec_checkout < fecha_actual:
    #             pila_reservas.append(actual) 
    #         actual = actual.prox
        
        
    #     while pila_reservas:
    #              reserva = pila_reservas.pop()
    #              historico_gral_reservas.write(f'{reserva.nroreserva},{reserva.cliente},{reserva.habitacion},{reserva.fec_checkin},{reserva.fec_checkout}\n')
    #     historico_gral_reservas.close()
    

   



        
        
    
