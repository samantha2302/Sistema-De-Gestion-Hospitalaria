# Fecha: 02/06/2021
# Hecho por: Katherine Amador Gonzalez y Samantha Acuña Montero.
# Objetivo: Clase Estadisticas.

from Oficial import ObtenerMedico
from Proyecto import ObtenerPaciente
from Proyecto import ObtenerParteMedico
from Oficial import ObtenerParteMedicoPaciente

'''
	Imprimir el total de pacientes atendidos.
	Imprimir el total de enfermedades atendidos en el hospital.
	Imprimir el total de enfermedades por sexo 
	Imprimir el desglose de los sentimientos más presentes en los diagnósticos 
	Imprimir los pacientes en donde el parte médico “sin problemas” es mayor a los diagnósticos “con enfermedades”.  

'''
class Estadistica:

    def __init__(self, listaMedico, listaPaciente, listaParteMedico,listaParteMedicoPaciente,TotalPacientes):
        self.listaMedico = listaMedico
        self.listaPaciente = listaPaciente
        self.listaParteMedico = listaParteMedico
        self.listaParteMedicoPaciente = listaParteMedicoPaciente
        self.TotalPacientes=TotalPacientes

    def ImprimirPacientes(self):
        file = open("Datos/paciente.txt", "r")
        filas = file.readlines()
        listaIds = []
        for fila in filas:
            paciente = fila.split(",")
            listaIds.append(paciente[0])
        total = listaIds[-1]
        self.TotalPacientes.set(total)

if __name__ == "__main__":
    lista1=ObtenerPaciente()
    lista2=ObtenerMedico()
    lista3=ObtenerParteMedico()
    lista4=ObtenerParteMedicoPaciente()
    estadistica = Estadistica(lista1, lista2, lista3, lista4,"")
    estadistica.ImprimirPacientes()