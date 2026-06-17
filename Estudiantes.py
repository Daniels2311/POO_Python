listas_estudiantes = []

class Estudiantes:
    def __init__(self, id_estudiante, nombre, apellido, edad, grado):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.grado = grado
    
    #metodos 
    def ingresar_curso(self):
        print(f"Ingresando al curso {self.nombre} {self.apellido} Bienvenido")

estudiante_1 = Estudiantes(1, "Miguel", "Tortuga", 10, "Quinto")
estudiante_2 = Estudiantes(2, "Donatelo", "Tortuga", 14, "Septimo")
estudiante_3 = Estudiantes(3, "Rafael", "Tortuga", 17, "Undecimo")

estudiante_1.ingresar_curso()
estudiante_2.ingresar_curso()
estudiante_3.ingresar_curso()

