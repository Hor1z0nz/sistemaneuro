from datetime import date, time, datetime

class Paciente:
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__visitas = {}

    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verVisitas(self):
        return self.__visitas

    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarVisitas(self,v):
        self.__visitas = v

class Visitas:
    def __init__(self):
        self.__fecha = 0
        self.__re = ""
        self.__notas = ""
        self.__indices = Indices

    def asignarFecha(self):
        self.__fecha = date.today()
    def asignarRe(self):
        self.__re = ######
    def asignarNotas(self):
        self.__notas = input("Ingrese notas de la visita")

    def verFecha(self):
        return self.__fecha
    def verRe(self):
        return self.__re
    def verNotas(self):
        return self.__notas
    
class Indices:
    def __init__(self):
        self.__pt = 0
        self.__pa1 = 0
        self.__pa2 = 0
        self.__pt = 0
        self.__pg = 0
 
    def asignarPt(self):
        self.__pt = float(input("Ingrese la Potencia Theta de el paciente"))
    def asignarPa1(self):
        self.__pa1 = float(input("Ingrese la Potencia Alfa1 de el paciente"))
    def asignarPa2(self):
        self.__pa2 = float(input("Ingrese la Potencia Alfa2 de el paciente"))
    def asignarPb(self):
        self.__pb = float(input("Ingrese la Potencia Beta de el paciente"))
    def asignarPg(self):
        self.__pg = float(input("Ingrese la Potencia Gamma de el paciente"))
    
    def verPt(self):
        return self.__pt
    def verPa1(self):
        return self.__pa1
    def verPa2(self):
        return self.__pa2
    def verPb(self):
        return self.__pb
    def verPg(self):
        return self.__pg
    
class Sys:
    def __init__(self):
        self.__listapacientes = {}
    
    def verificarExiste(self,cedula):
        for p in self.__listapacientes:
            if cedula == p.verCedula():
                return True
        return False
    
    def verificarVisitas(self,fecha)
        

    def ingresarPaciente(self,cedula):
        if not self.verificarExiste(cedula.verCedula()):
            
    
     