import math
class Problema3:
    def __init__(self):
        self.__numeros=[0]*10
        for i in range(0,10):
            self.__numeros[i]=float(input())
    def promedio(self):
        T=0
        for i in range (0,10):
            aux=self.__numeros[i]
            T=T+aux
        T=T/10
        self.__t=T
        return T
    def desviacion(self):
        D=0
        for i in range (0,10):
            aux2=(math.pow((self.__numeros[i]-self.__t),2))
            D=D+aux2
        D=math.sqrt(D/9)
        return D
print("Ingrese los numeros =")
ecuacion=Problema3()
print("El promedio es =",ecuacion.promedio())
print("La desviacion es =",ecuacion.desviacion())