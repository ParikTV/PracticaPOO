class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def  estudiar(self):
        print("Estudiando...")


nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese el edad: "))
grado = int(input("Ingrese su nivel de grado: "))

estudiante = Estudiante(nombre, edad, grado)

print(f"""
    DATOS DEL ESTUDIANTE: \n
    Nombre: {estudiante.nombre} \n
    Edad: {estudiante.edad} \n
    Grado: {estudiante.grado} \n
    """)

while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
