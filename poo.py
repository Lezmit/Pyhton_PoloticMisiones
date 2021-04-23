class Perro:
    especie ="canis lupus familiaris"
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def description(self):
        return f"{self.nombre} tiene {self.edad} años."

    def ladrar(self,sonido):
        return f"{self.nombre} dice {sonido}"        
