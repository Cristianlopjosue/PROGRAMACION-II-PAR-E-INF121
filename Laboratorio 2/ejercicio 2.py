import math
class AlgebraVectorial:
    def __init__(self, a):
        self.a = list(a)

    def __add__(self, otro):
        return AlgebraVectorial([self.a[i] + otro.a[i] for i in range(3)])

    def __rmul__(self, k):
        return AlgebraVectorial([k * self.a[i] for i in range(3)])

    def __abs__(self):
        N = 0
        for i in range(3):
            N += self.a[i]**2
        return math.sqrt(N)

    def Normal(self):
        N = abs(self)
        return AlgebraVectorial([self.a[i]/N for i in range(3)])

    def __matmul__(self, otro):
        C = 0
        for i in range(3):
            C += self.a[i] * otro.a[i]
        return C

    def __xor__(self, otro):
        c = [0]*3
        c[0] = self.a[1]*otro.a[2] - self.a[2]*otro.a[1]
        c[1] = self.a[2]*otro.a[0] - self.a[0]*otro.a[2]
        c[2] = self.a[0]*otro.a[1] - self.a[1]*otro.a[0]
        return AlgebraVectorial(c)

    def __str__(self):
        return f"{self.a}"

v1 = AlgebraVectorial([2,1,-1])
v2 = AlgebraVectorial([4,2,-2])
Suma = v1 + v2
Escalar = 3 * v1
Longitud = abs(v1)
Normal = v1.Normal()
P_Escalar = v1 @ v2
P_Vectorial = v1 ^ v2
print("Suma:", Suma)
print("Escalar:", Escalar)
print("Longitud :", Longitud)
print("Normal :", Normal)
print("Producto escalar:", P_Escalar)
print("Producto vectorial :", P_Vectorial)

