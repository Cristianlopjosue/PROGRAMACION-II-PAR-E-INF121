class EcuacionLineal:
    def __init__(self):
        self.__a=float(input("Ingrese a ="))
        self.__b=float(input("Ingrese b ="))
        self.__c=float(input("Ingrese c ="))
        self.__d=float(input("Ingrese d ="))
        self.__e=float(input("Ingrese e ="))
        self.__f=float(input("Ingrese f ="))
    def tieneSolucion(self):
        if (self.__a*self.__d-self.__b*self.__c) != 0:
            return True
        else:
            return False 
    def getX(self):
        return ((self.__e*self.__d)-(self.__b*self.__f))/((self.__a*self.__d)-(self.__b*self.__c))
    def getY(self):
        return ((self.__a*self.__f)-(self.__e*self.__c))/((self.__a*self.__d)-(self.__b*self.__c))

ecuacion=EcuacionLineal()
if ecuacion.tieneSolucion():
    print("X =",ecuacion.getX(),"Y =",ecuacion.getY())
else:
    print("No tiene solucion")
