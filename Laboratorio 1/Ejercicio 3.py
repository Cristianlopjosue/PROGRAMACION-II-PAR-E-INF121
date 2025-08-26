import math
class Problema3:
    def __init__(self):
        print("Ingrese los datos del 1 al 10 =")
        self.__d1=float(input())
        self.__d2=float(input())
        self.__d3=float(input())
        self.__d4=float(input())
        self.__d5=float(input())
        self.__d6=float(input())
        self.__d7=float(input())
        self.__d8=float(input())
        self.__d9=float(input())
        self.__d10=float(input())
    def promedio(self):
        self.__P=self.__d1+self.__d2+self.__d3+self.__d4+self.__d5+self.__d6+self.__d7+self.__d8+self.__d9+self.__d10
        self.__t=self.__P/10
        return self.__t
    def desviacion(self):
        self.__C=((self.__d1-self.__t)**2+(self.__d2-self.__t)**2+(self.__d3-self.__t)**2+(self.__d4-self.__t)**2+(self.__d5-self.__t)**2+(self.__d6-self.__t)**2+(self.__d7-self.__t)**2+(self.__d8-self.__t)**2+(self.__d9-self.__t)**2+(self.__d10-self.__t)**2)
        self.__D=math.sqrt(self.__C/9)
        return self.__D
print("Ingrese los numeros =")
ecuacion=Problema3()
print("El promedio es =",ecuacion.promedio())
print("La desviacion es =",ecuacion.desviacion())
