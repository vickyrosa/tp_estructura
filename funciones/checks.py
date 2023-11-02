def check_dni(lista_clientes, dni):
    if len(lista_clientes) == 0:
        return True
    for cliente in lista_clientes:
        if cliente.dni == dni:
            return False
    return True

# PORFA PREGUNTENLE A AGOS SI ESTA BIEN ESTO, ES IGUAL AL CHECK DE ARRIBA (OSEA HAY UNO QUE NO VAMOS A USAR)
# SOLO QUE 'FORZANDO' EL USO DEL SET, ES ALGO QUE HABIAMOS HABLADO LA SEMANA PASADA, 
# PERO MAS QUE NADA PARA SABER SI ES PREFERIBLE QUE NO LO USEMOS O QUE LO USEMOS (XQ PIDE EL TP) AUNQUE NO SEA LO MAS EFECTIVO O PROLIJO

# def check_dni(lista_clientes, dni):
    # set_dni_clientes = set()
    # if len(lista_clientes) == 0:
    #     return True
    # for cliente in lista_clientes:
    #     set_dni_clientes.add(cliente.dni)
    # if dni in set_dni_clientes:
    #     return False
    # return True