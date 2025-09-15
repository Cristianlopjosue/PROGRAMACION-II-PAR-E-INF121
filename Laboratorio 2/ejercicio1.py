import math
class AlgebraVectorial:
    def __init__(self, a, b):
        self.a = a  
        self.b = b  
    def Perpendicular(self, metodo=None):
        if (abs(self.a[0] + self.b[0]) == abs(self.a[0] - self.b[0])):
            if (abs(self.a[1] - self.b[1]) == abs(self.b[1] - self.a[1])):
                if (self.a[2] * self.b[2] == 0):
                    if (abs(math.pow(self.a[2] + self.b[2], 2)) ==
                        (abs(math.pow(self.a[2], 2) + abs(math.pow(self.b[2], 2))))):
                        return "Es perpendicular"
        return "No es perpendicular"
    def Paralela(self, metodo=None):
        if (self.a[0] == self.b[0]):
            if ((self.a[1] * self.b[1]) == 0):
                return "es paralela"
        return "No es paralela"
    def Proyecciona_b(self):
        return ( (self.a[0]*self.b[0] + self.a[1]*self.b[1] + self.a[2]*self.b[2]) /
                 abs(math.pow(self.b[0],2) + math.pow(self.b[1],2) + math.pow(self.b[2],2)) ) * self.b[0]
    def Componentea_b(self):
        return (self.a[0]*self.b[0] + self.a[1]*self.b[1] + self.a[2]*self.b[2]) / abs(self.b[0])
prueba1 = AlgebraVectorial((2, 1, -1), (4, 2, -2))
print(prueba1.Perpendicular())
print(prueba1.Paralela())
print("Proyección:", prueba1.Proyecciona_b())
print("Componente:", prueba1.Componentea_b())
