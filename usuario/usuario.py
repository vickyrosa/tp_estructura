class Usuario:
    
    set_dni = set()

    def __init__(self, tipo_usuario, dni, nombre, contra, fec_nac, genero, tel, mail, domicilio, fec_alta):
            self.tipo_usuario = tipo_usuario
            self.dni= dni
            self.nombre = nombre
            self.contra = contra
            self.fec_nac = fec_nac
            self.genero = genero
            self.tel = tel
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
    Telefono: {self.tel}
    Mail: {self.mail}
    Domicilio: {self.domicilio}
    Fecha de alta: {self.fec_alta}
    '''

    # Permite a cualquier usuario del sistema cambiar su contraseña
    def cambiar_contra(self):
        while True:
            self.contra = input('Ingrese nueva contraseña: ')
            if len(self.contra) == 0:
                print('Porfavor ingrese una contraseña')
            else:
                print('Su contraseña fue actualizada con exito')
                break