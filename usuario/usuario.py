class Usuario:
    
    set_dni = set()
    set_cuil = set()

    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, telefono, mail, domicilio, fec_alta):
            self.tipo_usuario = tipo_usuario
            self.dni= dni
            self.nombre = nombre
            self.contra = contra
            self.fec_nac = fec_nac
            self.genero = genero
            self.telefono = telefono
            self.mail = mail 
            self.domicilio = domicilio 
            self.fec_alta = fec_alta
            self.set_dni.add(dni)
        
    def __str__(self):
        return f'''
    DNI: {self.dni}
    Nombre: {self.nombre}
    Fecha de nacimiento: {self.fec_nac}
    Genero: {self.genero}
    Telefono: {self.telefono}
    Mail: {self.mail}
    Domicilio: {self.domicilio}
    Fecha de alta: {self.fec_alta}
    '''
    # FALTA MODIFICAR EL TXT AL FINAL ASI LA PROXIMA VEZ QUE ENTRE SE GUARDA EL CAMBIO DE CONTRASENA
    # PARA ESO VOY A HACER QUE SE MODIFIQUE EL OBJETO, LUEGO CUANDO SELECCIONE CERRAR PROGRAMA TODOS!!! LOS TXT
    # SE VUELVEN A ESCRIBIR
    def cambiar_contra(self):
        while True:
            self.contra = input('Ingrese nueva contraseña: ')
            if len(self.contra) == 0:
                print('Porfavor ingrese una contraseña')
            else:
                print('Su contraseña fue actualizada con exito')
                break