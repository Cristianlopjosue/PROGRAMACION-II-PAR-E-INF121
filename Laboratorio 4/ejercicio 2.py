from abc import ABC, abstractmethod
import random
import math
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self):
        pass

class Figura(ABC):
    def __init__(self,color):
        self.color = color
    def setColor(self,otro):
        self.color = otro
    def getColor(self):
        return self.color
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def toString(self):
        pass

class Cuadrado(Figura,Coloreado):
    def __init__(self, lados):
        self.lados=lados
    def comoColorear(self):
        return ("Colorear los cuatro lados")
    def area(self):
        return self.lados**2
    def perimetro(self):
        return self.lados*4
    def toString(self):
        return (f"el lado es: {self.lados}\nel area es : {self.area()},\nel perimetro es: {self.perimetro()}")

class Circulo(Figura):
    def __init__(self,radio):
        self.radio=radio
    def area(self):
        return math.pi*self.radio**2
    def perimetro(self):
        return 2*math.pi*self.radio
    def toString(self):
        return (f"El radio es: {self.radio}\nel area es: {self.area()}\nel perimetro es: {self.perimetro()}")

figuras=[]
for i in range(5):
    numero=random.randint(1,2)
    if (numero==1):
        lado=random.randint(1,50)
        figuras.append(Cuadrado(lado))
    elif (numero==2):
        radio=random.randint(1,50)
        figuras.append(Circulo(radio))
for a in figuras:
    if isinstance(a,Circulo):
        print("Circulo")
        print(a.toString(),"\n")
    if isinstance(a,Cuadrado):
        print("Cuadrado")
        print(a.toString())
        print(a.comoColorear(),"\n")