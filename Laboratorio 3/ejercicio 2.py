import random
class Juego:
    def __init__(self,NumerodeVidas,Record=0):
        self.NumerodeVidas = NumerodeVidas
        self.Record = Record
    def reiniciarPartida(self):
        return self.NumerodeVidas
    def actualizarPartida(self):
        self.Record = self.Record+1
    def Quitavida(self):
        if (self.NumerodeVidas == 0):
            return False
        else:
            return True


class JuegoAdivinaNumero(Juego):
    def  __init__(self,NumerodeVidas,Record=0):
        super().__init__(NumerodeVidas,Record)
        self.NumeroAadivinar= random.randint(1,10)
    def validaNumero(self,numero):
        if (0<=numero<=10):
            return True
        else:
            return False
    def juega(self):
        print("Intente adivinar el numero random de 1 a 10 =>\n")
        n=int(input())
        if self.validaNumero(n):
            if (n==self.NumeroAadivinar):
                print("Acertaste en el numero correcto :D \n")
                self.actualizarPartida()
            else:
                self.NumerodeVidas -=1
                if self.Quitavida():
                    if(n>self.NumeroAadivinar):
                        print("El numero es menor al ingresado vuelve a intentarlo :D \n")
                    else:
                        print("El numero es mayor al ingresado vuelve a intentarlo :D \n")
                else:
                    print ("Perdiste :c")
                    print (f"El mejor record es => {self.Record}")


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if (0<=numero<=10):
            if(numero%2==0):
                return True
            else:
                print("Error")
                return False
        else:
            return False


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self,numero):
        if (0<=numero<=10):
            if(numero%2==0):
                print("Error")
                return False
            else:
                return True
        else:
            return False
        


class Aplicacion:
    def main():
        juego_numero = JuegoAdivinaNumero(3)
        juego_par = JuegoAdivinaPar(3)
        juego_impar = JuegoAdivinaImpar(3)
        print("\nAdivina número")
        juego_numero.juega()
        print("\nAdivina par")
        juego_par.juega()
        print("\nAdivina impar")
        juego_impar.juega()

Aplicacion.main()