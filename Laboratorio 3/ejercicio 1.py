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
    def  __init__(self,NumerodeVidas,Record,numeroAadivinar):
        super().__init__(NumerodeVidas,Record)
        self.NumeroAadivinar= random.randint(1,10)
    def juega(self):
        print("Intente adivinar el numero random de 1 a 10 =>\n")
        n=int(input())
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

class Aplicacion:
    def main():
        juego = JuegoAdivinaNumero(7, Record=0, numeroAadivinar=0)
        juego.juega()
Aplicacion.main()
