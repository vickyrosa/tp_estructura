from usuario.usuario import Usuario
from hotel.reservas import Reserva
from hotel.buffet import Buffet
from collections import deque
import funciones.metodos_de_pagos as mp
import datetime
import random

class Cliente(Usuario):

    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta, historico_gastos):
        super().__init__(tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta)
        self.historico_gastos = int(historico_gastos)
    
    def ver_categoria(self):
        if self.historico_gastos in range(0,50000):
            print('Su categoria es Nivel Bajo')
        elif self.historico_gastos in range(50000,250000):
            print('Su categoria es Nivel Medio')
        else:
            print('Su categoria es Nivel Alto')
            
    def reservar(self, hotel):
        while True:
            tipo = input(''' Elija un tipo de habitacion:
                    a. Simple ---> $1000 por noche
                    b. Doble ----> $2000 por noche
                    c. Familiar ----> $3000 por noche
                    d. Suite ----> $4000 por noche
                        
                    ''')
            match tipo:
                case 'a':
                    tipo = 'Simple'
                    break
                case 'b':
                    tipo = 'Doble'
                    break
                case 'c':
                    tipo = 'Familiar'
                    break
                case 'd':
                    tipo = 'Suite'
                    break
                case _:
                    print('Por favor elija una de las opciones (a | b | c | d)')
        while True:
            # Utilizamos dos While diferentes para cada fecha, asi el usuario en caso de ingresar una de las dos en un formato incorrecto
            # no precisa volver a ingresar la anterior
            while True:
                try:
                    dia, mes, ano = map(int, input("Ingrese fecha de check-in en formato DD/MM/YYYY: ").split('/'))
                    fec_checkin = datetime.date(ano, mes, dia)
                    break
                except:
                    print('Porfavor ingrese una fecha valida en el formato pedido (Ej: 29/01/2023)')
                    
            while True:
                try:
                    dia, mes, ano = map(int, input("Ingrese fecha de check-out en formato DD/MM/YYYY: ").split('/'))
                    fec_checkout = datetime.date(ano, mes, dia)
                    break
                except:
                    print('Porfavor ingrese una fecha valida en el formato pedido (Ej: 29/01/2023)')
            if fec_checkin < fec_checkout:
                if datetime.date.today() < fec_checkin:
                    dias_totales = (fec_checkout - fec_checkin).days
                    # Una vez que verificamos que las fechas son correctas cronologicamente, las pasamos a str en el formato que queremos
                    fec_checkin = fec_checkin.strftime('%d/%m/%Y')
                    fec_checkout = fec_checkout.strftime('%d/%m/%Y')
                    break
                else:
                    print('Porfavor ingrese una fecha de check-in posterior al dia de hoy')
            else:
                print('Porfavor ingrese una fecha de check-in anterior a fecha de check-out')
                    
        # En caso de que el usuario decida salir directamente sin elegir, consideramos que es indiferente cual sea su habitacion,
        # por ende solo filtramos por tipo y fechas
        conbano = None
        conventana = None
        while True:
            accion = input(''' 
                    a. Elegir con o sin baño
                    b. Elegir con o sin ventana
                    c. Continuar (si no ha seleccionado ninguna opcion se le considerara como indiferente)
                        
                    ''')
            match accion:
                case 'a':
                    bano = input('''Elija si quiere con baño privado o no:
                    a. Con baño privado
                    b. Sin baño privado
                    c. Indiferente
                                 
                    ''')
                    match bano:
                        case 'a': 
                            conbano = True
                        case 'b':
                            conbano = False
                        case 'c':
                            conbano = None
                        case _: 
                            print("Porfavor elija una de las opciones (a | b | c)")
                case 'b':
                    ventana = input('''Elija si quiere con ventana o no:
                    a. Con ventana
                    b. Sin ventana
                    c. Indiferente
                                    
                    ''')
                    match ventana:
                        case 'a':
                            conventana = True
                        case 'b': 
                            conventana = False
                        case 'c':
                            conventana = None
                        case _:
                            print("Porfavor elija una de las opciones (a | b | c)")
                case 'c':
                    break
                case _: 
                    print("Porfavor elija una de las opciones (a | b | c)")

        for hab in hotel.lista_habitaciones:
            numero_reserva = random.randint(1,999999)
            if hab.get_tipo() == tipo:
                if conbano is not None:
                    if conventana is not None:
                        if conbano == hab.tiene_bano_privado() and conventana == hab.tiene_ventana_balcon():
                            if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                                hotel.lista_reservas_activas.agregar_reserva(Reserva(numero_reserva, self, hab, fec_checkin, fec_checkout))
                                Reserva.confirmacion_reserva(numero_reserva, self, hab, fec_checkin, fec_checkout, dias_totales)
                                self.historico_gastos += hab.precio_noche*dias_totales
                                return True
                    else:
                        if conbano == hab.tiene_bano_privado():
                            if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                                hotel.lista_reservas_activas.agregar_reserva(Reserva(numero_reserva, self, hab, fec_checkin, fec_checkout))
                                Reserva.confirmacion_reserva(numero_reserva, self, hab, fec_checkin, fec_checkout, dias_totales)
                                self.historico_gastos += hab.precio_noche*dias_totales
                                return True
                else:
                    if conventana is not None:
                        if conventana == hab.tiene_ventana_balcon():
                            if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                                hotel.lista_reservas_activas.agregar_reserva(Reserva(numero_reserva, self, hab, fec_checkin, fec_checkout))
                                Reserva.confirmacion_reserva(numero_reserva, self, hab, fec_checkin, fec_checkout, dias_totales)
                                self.historico_gastos += hab.precio_noche*dias_totales
                                return True
                    else:
                        if Reserva.disponibilidad(fec_checkin,fec_checkout,hab, hotel):
                            hotel.lista_reservas_activas.agregar_reserva(Reserva(numero_reserva, self, hab, fec_checkin, fec_checkout))
                            Reserva.confirmacion_reserva(numero_reserva, self, hab, fec_checkin, fec_checkout, dias_totales)
                            self.historico_gastos += hab.precio_noche*dias_totales
                            return True
        print('No se encontro una habitacion disponible en las fechas con sus preferencias, porfavor realize una nueva reserva cambiando los parametros y/o fechas')
        
    def ordenar_del_buffet(self):
        total = 0
        cola_pedidos = deque()
        buffet = Buffet()
        while True:
            print("Menu del buffet:")
            buffet.mostrar_menu()
            ans = input("Escriba lo que quiera ordenar (Escriba 'salir' si ya no desea ordenar): ").capitalize().strip()
            if ans == 'Salir':
                break
            elif ans in buffet.menu.keys():
                total += buffet.menu[ans]
                print(f"Ordenaste {ans}.")
                
                # Agregar el pedido a la cola
                cola_pedidos.append(ans)
            else:
                print("Comando incorrecto. Por favor, elija un plato del menu o salir.")
        
        print(f'Precio total: ${total}')
        mp.metodo_de_pago()
        buffet.procesar_pedidos(cola_pedidos)
        self.historico_gastos += total
        
    def cancelar_reserva(self, hotel):
        num_reserva_cancelar = input("Ingrese el número de reserva que desea cancelar: ")
        lista_reservas = hotel.lista_reservas_activas
        nodo = lista_reservas.cabeza
        while nodo:
            if nodo.nroreserva == num_reserva_cancelar:
                fec_checkin = datetime.strptime(nodo.fec_checkin, '%d/%m/%Y')
                if datetime.today() < fec_checkin:
                    lista_reservas.eliminar_reserva(nodo.nroreserva)
                    print(f'Reserva {num_reserva_cancelar} cancelada exitosamente.')
                    return
                else:
                    print("No es posible cancelar reservas activas.")
                    return 
            nodo = nodo.prox
        print(f'No se encontró la reserva con el número {num_reserva_cancelar}.')