import math
class EcuacionLineal2:
    def __init__(self):
        self.__a=float(input("Ingrese a ="))
        self.__b=float(input("Ingrese b ="))
        self.__c=float(input("Ingrese c ="))
    def getDiscriminante(self):
        if(2*(self.__b)-4*(self.__a*self.__c))>0:
            return 1
        elif (2*(self.__b)-4*(self.__a*self.__c))==0:
            return 0
        elif (2*(self.__b)-4*(self.__a*self.__c))<0:
            return -1
    def getRaiz1(self):
        return (-self.__b+math.sqrt(math.pow(self.__b,2)-4*(self.__a*self.__c)))/(2*self.__a)
    def getRaiz2(self):
        return (-self.__b-math.sqrt(math.pow(self.__b,2)-4*(self.__a*self.__c)))/(2*self.__a)
ecuacion=EcuacionLineal2()
if ecuacion.getDiscriminante()==1:
    print("Tienen raiz en =",ecuacion.getRaiz1()," y ",ecuacion.getRaiz2())
elif ecuacion.getDiscriminante()==0:
    print("Tiene raiz en =",ecuacion.getRaiz1())
elif ecuacion.getDiscriminante()==-1:
    print("No tiene raices reales")