class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Estoy hablando un poco")


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
            super().__init__(nombre, edad, nacionalidad)
            self.trabajo = trabajo
            self.salario = salario


Roberto = Empleado("Robert", 43, "Argentino", "Programador", 100000)

Roberto.hablar()
