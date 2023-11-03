def check_dni(lista_clientes, dni):
    if len(lista_clientes) == 0:
        return True
    for cliente in lista_clientes:
        if cliente.dni == dni:
            return False
    return True
