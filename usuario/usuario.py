class Usuario:
    def __init__(self, tipo_usuario, dni, nombre, contra, edad, sexo, telefono, mail, domicilio, fec_alta):
            self.tipo_usuario = tipo_usuario
            self.dni= dni
            self.nombre = nombre
            self.contra = contra
            self.edad = edad
            self.sexo = sexo
            self.telefono = telefono
            self.mail = mail 
            self.domicilio = domicilio 
            self.fec_alta = fec_alta
        
    def __str__(self):
        return f'''
    DNI: {self.dni}
    Nombre: {self.nombre}
    Edad: {self.edad}
    Sexo: {self.edad}
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