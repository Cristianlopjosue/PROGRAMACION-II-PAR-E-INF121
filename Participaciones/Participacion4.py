import math
class Circulo2D:
    def __init__(self,x=0.0,y=0.0,r=1.0):
        self.x=x
        self.y=y
        self.r=r
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getR(self):
        return self.r
    
    def getArea(self):
        return math.pi*self.r**2
    
    def getPerimetro(self):
        return 2*math.pi*self.r
    
    def Contiene(self,Px,Py):
        D=math.sqrt(math.pow(Px-self.x,2)+math.pow(Py-self.y,2))
        if(D<=self.r):
            return True  
    def Circulodentro(self,Circulo):
        D=math.sqrt(math.pow(Circulo.x-self.x,2)+math.pow(Circulo.y-self.y,2))
        if(D+Circulo.r<=self.r):
            return True
        
    def Sobrepone(self,Circulo):
        D=math.sqrt(math.pow(Circulo.x-self.x,2)+math.pow(Circulo.y-self.y,2))
        if (abs(self.r-Circulo.r)<=D<=(self.r+Circulo.r)):
            return True
c1 = Circulo2D(2, 0, 1)
print("Area =",c1.getArea(),"\nPerimetro =",c1.getPerimetro())
print("Contiene el punto? =",c1.Contiene(2.5,0))
print("Contiene el Circulo? =",c1.Circulodentro(Circulo2D(2,0,0.5)))
print("Se sobreponen? =",c1.Sobrepone(Circulo2D(0,0,2)))
