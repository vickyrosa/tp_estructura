import datetime
import hotel.hotel as hotel
def load_historico_gastos(costo):
    # Paso la fecha de hoy a formato deseado (primero a str y despues devuelta a fecha)
    fecha_hoy = datetime.datetime.now().strftime('%d/%m/%Y')
    with open('txt/gastos_diarios_aux.txt', 'r') as archivo_aux:
        fecha = archivo_aux.read(10)
    archivo_aux.close()
    if fecha_hoy == fecha:    
        hotel.ingresos_diarios += costo
    else:
        hotel.ingresos_diarios = costo
    #Recorro el txt de clientes.
    with open('txt/recaudacion.txt', 'a') as archivo_recaudacion_total:
        archivo_recaudacion_total.write(f"Fecha: {fecha_hoy}, Gasto: {costo}\n")
    archivo_recaudacion_total.close()
    #Guardo la ultima fecha con el ultimo total de ingresos diarios
    with open('txt/gastos_diarios_aux.txt', 'w') as archivo_aux:
        archivo_aux.write(f"{fecha_hoy}, {hotel.ingresos_diarios}\n")
    archivo_aux.close()
    return fecha_hoy
    

    