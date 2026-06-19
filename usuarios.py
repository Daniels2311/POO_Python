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
    
    #metodo que dejaremos para poder hacer el polimorfimos mas adelante
    def consultar_certificados(self):
        #cada clase hija decidira como implementar el certificado
        print(f"Certificados de {self.nombre} {self.apellido}")

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

#aplicando los 4 pilares de la programacion orientada a objetos
#Herencia y encapsulamiento

class Aprendiz(Usuario): 
    def __init__(self, id_usuario, documento, nombre, apellido, correo, telefono, direccion, programa, ficha, resultados = []):
        
        #usamos super para llamar al constructor de la clase padre
        super().__init__(id_usuario, documento, nombre, apellido, correo, telefono, direccion)
        
        #atributos propios del aprendiz
        
        self.programa = programa
        self.ficha = ficha
        
        #encapsulamos el atributo resultados en una lista
        #atributo privado
        self.__resultados = resultados
        
    # Get consultar o ver el atributo
    
    def get_resultados(self):
        return self.__resultados
    
    #Set modificar o actualizar el atributo
    
    def set_resultados(self, notas):
        self.__resultados.append(notas)
        print(f"Notas actualizadas {self.nombre} {self.apellido} total: {len(self.__resultados)}")
    
    #sobre escribimos el metodo de la clase padre para darle un comportamiento especifico
    def consultar_certificados(self):
        print(f"Certificados de aprendiz {self.nombre} {self.apellido}")

aprendiz_1 = Aprendiz(3, 2903657120, "Maria", "Leon", "alexlion23@gmail.com", "3103489005", "Cr 34 #09-34", "ADSO", "ficha342", [1,2,3,4])

aprendiz_ejemplo = Aprendiz(nombre = "Hector", apellido = "Leon", id_usuario = 4, documento = 1232780940, correo = "hectorlion23@gmail.com", telefono = "3209432890", programa = "ADSO", ficha = "ficha435", direccion = "Cr 34 #09-34", resultados = [1,2,3,4])

print(f"imprimir atributo private {aprendiz_1.get_resultados()}")
print(f"imprimir atributo publico {aprendiz_1.nombre}")

class Instructor(Usuario):
    def __init__(self, id_usuario, documento, nombre, apellido, correo, telefono, direccion, anios_experiencia, perfil_profesional):
        super().__init__(id_usuario, documento, nombre, apellido, correo, telefono, direccion)
        self.anios_experiencia = anios_experiencia
        self.perfil_profesional = perfil_profesional
    
    #sobre escribimos el metodo de la clase padre para darle un comportamiento especifico
    def consultar_certificados(self):
        print(f"Certificados de instructor {self.nombre} {self.apellido}")

instructor_1 = Instructor(5, 2903657120, "Guillermo", "Leon", "alexlion23@gmail.com", "3103489005", "Cr 34 #09-34", "9", "waza")
print(instructor_1.nombre)

#Polimorfismo

aprendiz_1.consultar_certificados()#llamamos al metodo de la clase aprendiz
instructor_1.consultar_certificados()#llamamos al metodo de la clase instructor