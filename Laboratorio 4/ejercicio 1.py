from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self,nombre):
        self.Nombre = nombre
    def toString(self):
        return (f"Nombre: {self.Nombre}")
    @abstractmethod
    def CalcularSalarioMensual(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self,nombre,salario_anual):
        super().__init__(nombre)
        self.Salario_anual = salario_anual
    def CalcularSalarioMensual(self):
        return self.Salario_anual/12
    def toString(self):
        return (f"Nombre: {self.Nombre}\nSalario: {self.Salario_anual}")
    
class EmpleadoTiempoHorario(Empleado):
    def __init__(self,nombre,horas_trabajadas,tarifa_por_hora):
        super().__init__(nombre)
        self.horas=horas_trabajadas
        self.Tarifa=tarifa_por_hora
    def CalcularSalarioMensual(self):
        return self.horas*self.Tarifa
    def toString(self):
        return (f"Nombre: {self.Nombre}\nHoras: {self.horas}\nTarifa: {self.Tarifa}")



empleado1=EmpleadoTiempoCompleto("Pedro",120000)
empleado2=EmpleadoTiempoCompleto("Juan",150000)
empleado3=EmpleadoTiempoCompleto("Sofia",200000)
empleado4=EmpleadoTiempoHorario("Jorge",1500,20)
empleado5=EmpleadoTiempoHorario("Juana",600,30)
Empleados=[empleado1,empleado2,empleado3,empleado4,empleado5]
for a in Empleados:
    if isinstance(a,EmpleadoTiempoCompleto):
        print("\nEmpleado a Tiempo completo")
        print(f"{a.toString()}\nsalario mensual: {a.CalcularSalarioMensual()}")
    elif isinstance(a,EmpleadoTiempoHorario):
        print("\nEmpleado a Tiempo Horario")
        print(f"{a.toString()}\nsalario mensual: {a.CalcularSalarioMensual()}")