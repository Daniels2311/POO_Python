#Clase Usuario
# class Usuario:
#     id_usuario = 1
#     documento = 2903657120
#     nombre = "Alex"
#     apellido = "Leon"
#     correo = "alexlion23@gmail.com"
#     telefono = "3103489005"
#     direccion = "Cr 34 #09-34"

#creando una instancia de la clase Usuario
# usuario_1 = Usuario()
# usuario_2 = Usuario()

# usuario_2.nombre = "Edison"
#  print(usuario_1.nombre)

lista_usuarios = []
class Usuario:
    def __init__(self, id_usuario, documento, nombre, apellido, correo, telefono, direccion):
        self.id_usuario = id_usuario
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}")
    #metodos base crud
    
    #crear usuarios
    def crear_usuario(self):
        lista_usuarios.append(self)
        print(f"Usuario {self.nombre} creado con exito")
    
    #ver usuarios
    def ver_usuario(self):
        print(f"id: {self.id_usuario}, nombre: {self.nombre} {self.apellido}")
    
    #actualizar usuarios
    def actualizar_usuario(self, nuevo_nombre, nuevo_apellido):
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
        print(f"Usuario {self.nombre} {self.apellido} actualizado con exito")
    
    #eliminar usuarios
    def eliminar_usuario(self):
        if self in lista_usuarios:
            lista_usuarios.remove(self)
            print(f"El usuario {self.nombre} {self.apellido} a sido eliminado correctamente")
        else:
            print(f"No se encontro el usuario {self.nombre} {self.apellido} en el sistema")

#creando una instancia de la clase Usuario
usuario_1 = Usuario(1, 2903657120, "Alex", "Leon", "alexlion23@gmail.com", "3103489005", "Cr 34 #09-34")
usuario_2 = Usuario(2, 2903657120, "Edison", "Leon", "edisonleon@gmail.com", "3103489005", "Cr 34 #09-34")
#llamamos al metodo saludar
usuario_1.saludar()

usuario_1.ver_usuario()

print(f"lista_usuarios: {lista_usuarios}")
usuario_1.crear_usuario()
print(f"lista_usuarios: {lista_usuarios[0].nombre}")

usuario_1.actualizar_usuario("Edison", "Leon")
usuario_1.ver_usuario()

usuario_2.eliminar_usuario()

#llamamos los atributos de la clase
print(usuario_1.nombre)


