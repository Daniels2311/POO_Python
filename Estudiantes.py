#lista vacia
listas_estudiantes = []

#clase estudiantes
class Estudiantes:
    
    #Atributos
    def __init__(self, id_estudiante, nombre, apellido, edad, grado):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.grado = grado
    
    #metodos
    #metodo para polimorfismo
    def ingresar_curso(self):
        print(f"Ingresando al curso {self.nombre} {self.apellido} Bienvenido")

#Instancias de la clase Estudiantes
estudiante_1 = Estudiantes(1, "Miguel", "Tortuga", 10, "Quinto")
estudiante_2 = Estudiantes(2, "Donatelo", "Tortuga", 14, "Septimo")
estudiante_3 = Estudiantes(3, "Rafael", "Tortuga", 17, "Undecimo")

#llamamos el metodo ingresar_curso
estudiante_1.ingresar_curso()
estudiante_2.ingresar_curso()
estudiante_3.ingresar_curso()

#Herencia de la clase Estudiantes
#Clase estudiantes primaria
class Estudiantes_primaria(Estudiantes):
    def __init__(self, id_estudiante, nombre, apellido, edad, grado, contacto_familiar = [], notas = []):
        super().__init__(id_estudiante, nombre, apellido, edad, grado)
        
        #atributo propio de la clase estudiantes primaria
        self.contacto_familiar = contacto_familiar
        
    #encapsulamiento de un atributo
        #atributo privado 
        self.__notas = notas
    
    #funcion para ver el atributo
    def get_notas(self):
        return self.__notas
    
    #funcion para modificar el atributo
    def set_notas(self, notas_nuevas):
        self.__notas.appened(notas_nuevas)
        print(f"Las notas actualizadas de {self.nombre} {self.apellido} son {self.__notas}")
    
    #metodo para polimorfismo
    def ingresar_curso(self):
        print(f"Ingresando al curso {self.nombre} {self.apellido} Bienvenido a primaria")

estudiante_primaria1 = Estudiantes_primaria(1, "Juan", "Tortuga", 12, "Cuarto", ["Splinter", 3209453790], [4.5, 3.0, 5.0])
print(estudiante_primaria1.nombre)

#Clase estudiantes secundaria
class Estudiantes_secundaria(Estudiantes):
    def __init__(self, id_estudiante, nombre, apellido, edad, grado):
        super().__init__(id_estudiante, nombre, apellido, edad, grado)
    
    #metodo para polimorfismo
    def ingresar_curso(self):
        print(f"Ingresando al curso {self.nombre} {self.apellido} Bienvenido a secundaria")
    
    #metodos propio de la clase estudiantes secundaria
    def utilizar_internet(self):
        print(f"Utilizando el internet del colegio\n la contraseña es: 123admin\n el estudiante {self.nombre} {self.apellido} esta conectado a la red.")
    
    def hablar_docentes(self):
        print(f"Estudiante {self.nombre} {self.apellido} se lanzo a personeria para hablar con los docentes de la institucion")

estudiante_secundaria1 = Estudiantes_secundaria(2, "Pedro", "Tortuga", 14, "Octavo")
print(estudiante_secundaria1.nombre)

#Clase estudiantes bachillerato
class Estudiantes_bachillerato(Estudiantes):
    def __init__(self, id_estudiante, nombre, apellido, edad, grado, correo, telefono):
        super().__init__(id_estudiante, nombre, apellido, edad, grado)
        
        #atributo propio de la clase estudiantes bachillerato
        self.correo = correo
        self.telefono = telefono
        
    #metodo para polimorfismo
    def ingresar_curso(self):
        print(f"Ingresando al curso {self.nombre} {self.apellido} Bienvenido a bachillerato")
    
    #Metodos propios de la clase estudiantes bachillerato
    def utilizar_internet(self):
        print(f"Utilizando el internet del colegio\n la contraseña es: 123admin\n el estudiante {self.nombre} {self.apellido} esta conectado a la red.")
    
    def hablar_docentes(self):
        print(f"Estudiante {self.nombre} {self.apellido} se lanzo a personeria para hablar con los docentes de la institucion")
    
    def manipulacion_computadores(self):
        print(f"Estudiante {self.nombre} {self.apellido} esta utilizando el computador 12, de la sala 2 para realizar sus tareas")

estudiante_bachillerato1 = Estudiantes_bachillerato(3, "Jose", "Tortuga", 17, "Once", "juan.tortuga@gmail.com", "3103489005")
print(estudiante_bachillerato1.nombre)

#Polimorfismo entre las clases
estudiante_primaria1.ingresar_curso()
estudiante_secundaria1.ingresar_curso()
estudiante_bachillerato1.ingresar_curso()
