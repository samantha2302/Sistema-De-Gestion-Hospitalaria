# Fecha: 02/06/2021
# Hecho por: Katherine Amador Gonzalez y Samantha Acuña Montero.
# Objetivo: Clase Facturacion
import os
import tkinter as tk
from datetime import date
from Facturacion import Facturacion

def CrearArchivoFactura():
    existe =os.path.exists("Datos/facturacion.txt")
    if existe:
        print()
    else:
        file =open("Datos/facturacion.txt" ,"w")
def ObtenerFactura():
    CrearArchivoFactura()
    file = open("Datos/facturacion.txt ", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        factura = fila.split(",")
        filasTemporal.append({'Id':factura[0],
                                  'Id medico':factura[1],
                                  'Nombre medico':factura[2],
                                  'Id paciente':factura[3],
                                  'Nombre paciente':factura[4],
                                  'Fecha':factura[5],
                                  'Estado':factura[6],
                                  'Monto':factura[7],
                                  'Minutos':factura[8],
                                  'Salario':factura[9],
                                  'Sub total factura':factura[10],
                                  'Total factura':factura[11],
                                  'Impuesto':factura[12],
                                  'Total impuesto':factura[13],
                                  'Enfermedades':factura[14]})
        file.close()
        return filasTemporal


class ManejoFacturas(Facturacion):

    def __init__(self, idMedico,nombreMedico, idPaciente, nombrePaciente, fecha, idFactura, estado, monto,
                 minutos, salarioHora, totalFactura, subTotalFactura, impuesto, totalImpuesto, enfermedades,listaFactura, month, year):
        Facturacion.__init__(self,idMedico,nombreMedico, idPaciente, nombrePaciente, fecha, idFactura, estado, monto,
                 minutos, salarioHora, totalFactura, subTotalFactura, impuesto, totalImpuesto,enfermedades)
        self.listaFactura=listaFactura
        self.month = month
        self.year = year


    def AgregarFactura(self,idFactura, idMedico, nombreMedico, idPaciente,nombrePaciente, fecha, estado,
                        monto, minutos, salarioHora, totalFactura,subTotalFactura, impuesto, totalImpuesto,enfermedades):
        CrearArchivoFactura()
        file = open("Datos/facturacion.txt", "a")
        file.write(str(self.idFactura) + ",")
        file.write(str(self.idMedico) + ",")
        file.write(str(self.nombreMedico) + ",")
        file.write(str(self.idPaciente) + ",")
        file.write(str(self.nombrePaciente) + ",")
        file.write(str(self.fecha) + ",")
        file.write(str(self.estado) + ",")
        file.write(str(self.monto) + ",")
        file.write(str(self.minutos) + ",")
        file.write(str(self.salarioHora) + ",")
        file.write(str(self.totalFactura) + ",")
        file.write(str(self.subTotalFactura) + ",")
        file.write(str(self.impuesto) + ",")
        file.write(str(self.totalImpuesto) + ",")
        file.write(str(self.enfermedades))
        file.write("\n")
        file.close()






