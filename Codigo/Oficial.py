# Fecha: 19/04/2021
# Hecho por: Katherine Amador Gonzalez y Samantha Acuña Montero.
# Objetivo: Proyecto de reconocimiento de emociones.


'''
Pseudocodigo Etapa 1:
1. Creacion de dos listas globales llamadas "listamedico" y "listapaciente"
2. Creación de funciones, llamadas "registromedico" y "registropaciente" para el registro de los usuarios medico y paciente.
3. Se adjunto el codigo para el reconocimiento facial llamado emotion.
4. Se crea un ciclo while para crear un menu.
5. El menu tiene tres opciones, la primera opcion es para registrarse, la segunda para loguearse y la tercera para salir.
6. En la primera y segunda opcion se le solicita si quiere ingresar como paciente o como medico.
7. Si se quiere registrar como medico se le solicita nombre, apellido, codigomedico, codigorostro, contrasena, salario.
8. Si se quiere registrar como paciente se le solicita nombre, apellido, direccion, genero, nacimiento, cedula.
9. En el login se le pregunta si quiere ingresar como medico o como paciente.
10. Si ingresa como medico se le pregunta si quiere ingresar con usuario y contraseña o con una imagen.
11. Si ingresa como paciente se le pregunta si quiere ingresar con el numero de cedula o con una imagen.
12. La tercera opcion es salir del ciclo.
'''

'''
Pseudocodigo Etapa 2:
1. Creamos txt para cada usuario, cada historial y para la parte medico. 
2. Creamos las funciones de crear, agregar, editar, existir, eliminar y obtener para cada usuario
3. Creamos las funcines de crear, agregar, eliminar y obtener para cada historial.
4. Para la parte medico creamos funciones de crear, agregar y obtener.
5. Modificamos el menu.
    Parte medico:
        Creamos 6 opciones:
            Editar medico.
            Eliminar medico.
            Exite medico.
            Crear un nuevo historial medico.
            Obtener historial medico.
            Obtener historial paciente.
    Parte paciente:
        Creamos 4 opciones:
            Editar paciente.
            Exitir paciente.
            Crear una cita.
            Obtener diagnostico de enfermedades.
'''

'''
Psudocodigo Etapa 3:
Implementacion de interfaz grafica.
Trabajo terminado 
'''

import os
from Manejo_Facturas import ManejoFacturas
from Reconocimiento import Reconocimiento
from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
################################---PARTE MÉDICO FUNCIONES---####################################
def CrearArchivoMedico():
    existe = os.path.exists("Datos/medico.txt")
    if existe:
        print()
    else:
        file = open("Datos/medico.txt", "w")
        file.close()
def ExisteMedico(id):
    CrearArchivoMedico()
    file = open("Datos/medico.txt", "r")
    filas = file.readlines()
    for fila in filas:
        medico = fila.split(",")
        if str(medico[0]) == id:
            print("El medico ya existe")
            file.close()
            return True
    file.close()
    return False
def EditarMedico(id, nombre, apellido, codigomedico, contrasena, salario):
    CrearArchivoMedico()
    file = open("Datos/medico.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        medico = fila.split(",")
        if str(medico[0]) == id:
            filaModificada = str(id) + ","
            filaModificada = filaModificada + str(nombre) + ","
            filaModificada = filaModificada + str(apellido) + ","
            filaModificada = filaModificada + str(codigomedico) + ","
            filaModificada = filaModificada + str(contrasena) + ","
            filaModificada = filaModificada + str(salario)
            filaModificada = filaModificada + "\n"
            filasTemporal.append(filaModificada)
        else:
            filasTemporal.append(fila)
    file.close()
    file = open("Datos/medico.txt", "w")
    for fila in filasTemporal:
        file.write(fila)
    file.close()
def EliminarMedico(id):
    CrearArchivoMedico()
    file = open("Datos/medico.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        medico = fila.split(",")
        if medico[0] != id:
            filasTemporal.append(fila)
    file.close()
    file = open("Datos/medico.txt", "w")
    for fila in filasTemporal:
        file.write(fila)
    file.close()
def ObtenerMedico():
    CrearArchivoMedico()
    file = open("Datos/medico.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        medico = fila.split(",")
        filasTemporal.append({'Id': medico[0],
                              "Nombre": medico[1],
                              "Apellido": medico[2],
                              "Codigo de medico": medico[3],
                              "Contraseña": medico[4],
                              "Salario": medico[5]})
    file.close()
    return filasTemporal
### Historial Medico ###
#################################################################################################
def CrearArchivoHistorialMedico():
    existe = os.path.exists("Datos/historial_medico.txt")
    if existe:
        print()
    else:
        file = open("Datos/historial_medico.txt", "w")
        file.close()
def AgregarHistorialMedico():
    imagenes_path = input("Introduzca el path de la imagen: ")

    fecha = input("Ingrese la fecha: ")
    paciente = input("Ingrese el paciente: ")
    medico = input("Ingrese el médico: ")
    #emociones = EmocionesParteMedico(imagenes_path)
    #parteMedico = ParteMedico(imagenes_path)
    cantidadMinutos = input("Cantidad de minutos:")
    precioHora = input("Digite el precio por hora: ")
    precioTotal = input("Digite el precio total: ")
    CrearArchivoHistorialMedico()
    file = open("Datos/historial_medico.txt", "a")

    file.write(str(fecha) + ", ")
    file.write(str(paciente) + ", ")
    file.write(str(medico) + ", ")
    #file.write(str(emociones) + ", ")
    #file.write(str(parteMedico) + ", ")
    file.write(str(cantidadMinutos) + ", ")
    file.write(str(precioHora) + ", ")
    file.write(str(precioTotal) + ", ")
    file.write("\n")
    file.close()
    return {
            'Fecha': fecha,
            'Paciente': paciente,
            'Medico': medico,
            #'Emociones': emociones,
            #'Parte Medico': parteMedico,
            'Minutos': cantidadMinutos,
            'Precio por hora': precioHora,
            'Precio total': precioTotal
            }
def EliminarHistorialMedico():
    CrearArchivoHistorialMedico()
    file = open("Datos/historial_medico.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        hisMedico = fila.split(",")
        if str(hisMedico[0]) != id:
            filasTemporal.append(fila)
    file.close()
    file = open("Datos/historial_medico.txt", "w")
    for fila in filasTemporal:
        file.write(fila)
    file.close()
def ObtenerHistorialMedico():
    CrearArchivoHistorialMedico()
    file = open("Datos/historial_medico.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        hisMedico = fila.split(",")
        filasTemporal.append({'Id': hisMedico[0],
                              "Medico": hisMedico[1],
                              "Paciente": hisMedico[2],
                              'Fecha': hisMedico[3],
                              "Minutos": hisMedico[4],
                              "Precio por hora": hisMedico[5],
                              "Precio total": hisMedico[6],
                                "Parte medico": hisMedico[7]})
    file.close()
    return filasTemporal
###########################################---PARTE PACIENTE FUNCIONES---#########################
def CrearArchivoPaciente():
    existe = os.path.exists("Datos/paciente.txt")
    if existe:
        print()
    else:
        file = open("Datos/paciente.txt", "w")
        file.close()
def ObtenerPaciente():
    CrearArchivoPaciente()
    file = open("Datos/paciente.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        paciente = fila.split(",")
        filasTemporal.append({'Id': paciente[0],
                              'Nombre': paciente[1],
                              'Apellido': paciente[2],
                              'Cedula': paciente[3],
                              'Contraseña': paciente[4],
                              'Direccion': paciente[5],
                              'Genero': paciente[6],
                              'Nacimiento': paciente[7]
                              })

    file.close()
    return filasTemporal
### HISTORIAL MÉDICO DE PACIENTE ###
##################################################################################################
def CrearArchivoHistorialPaciente():
    existe = os.path.exists("Datos/historial_paciente.txt")
    if existe:
        print()
    else:
        file = open("Datos/historial_paciente.txt", "w")
        file.close()
def EliminarHistorialPaciente(id):
    CrearArchivoHistorialPaciente()
    file = open("Datos/historial_paciente.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        hisPaciente = fila.split(",")
        if str(hisPaciente[0]) != id:
            filasTemporal.append(fila)
    file.close()
    file = open("Datos/historial_paciente.txt", "w")
    for fila in filasTemporal:
        file.write(fila)
    file.close()
def ObtenerHistorialPaciente():
    CrearArchivoHistorialPaciente()
    file = open("Datos/historial_paciente.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        hisPaciente = fila.split(",")
        filasTemporal.append({'Id': hisPaciente[0],
                              'Fecha': hisPaciente[1],
                              'Genero': hisPaciente[2],
                              "Paciente": hisPaciente[3],
                              "Medico": hisPaciente[4],
                              "Parte medico": hisPaciente[5]
                              })
    file.close()
    return filasTemporal
##################################################################################################
def CrearArchivoParteMedico():
    existe = os.path.exists("Datos/parte_medico.txt.txt")
    if existe:
        print()
    else:
        file = open("Datos/parte_medico.txt", "w")
        file.close()
def ObtenerParteMedico():
    CrearArchivoParteMedico()
    file = open("Datos/parte_medico.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        parteMedico = fila.split(",")
        filasTemporal.append({'Id': parteMedico[0],
                              'Enfermedades': parteMedico[1]})
    file.close()
    return filasTemporal
##################################################################################################
def CrearArchivoParteMedicoPaciente():
    existe = os.path.exists("Datos/parte_medico_paciente.txt.txt")
    if existe:
        print()
    else:
        file = open("Datos/parte_medico_paciente.txt", "w")
        file.close()
def ObtenerParteMedicoPaciente():
    CrearArchivoParteMedico()
    file = open("Datos/parte_medico_paciente.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        parteMedicoPaciente = fila.split(",")
        filasTemporal.append({'Id': parteMedicoPaciente[0],
                              'Genero': parteMedicoPaciente[1],
                              'Enfermedades': parteMedicoPaciente[2]})
    file.close()
    return filasTemporal
#################################################################################################
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

################################################################################################
def CrearArchivoEmociones():
    existe =os.path.exists("Datos/emociones.txt")
    if existe:
        print()
    else:
        file =open("Datos/emociones.txt" ,"w")
def ObtenerEmociones():
    CrearArchivoFactura()
    file = open("Datos/emociones.txt ", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        emocion = fila.split(",")
        filasTemporal.append({'Id':emocion[0],
                              'Genero' : emocion[1],
                              'Emociones' : emocion[2]
                              })
#################################################################################################
def CrearArchivoEmocionesMedico():
    existe =os.path.exists("Datos/emociones_medico.txt")
    if existe:
        print()
    else:
        file =open("Datos/emociones_medico.txt" ,"w")
def ObtenerEmocionesMedico():
    CrearArchivoFactura()
    file = open("Datos/emociones_medico.txt ", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        emocionM = fila.split(",")
        filasTemporal.append({'Id':emocionM[0],
                              'Genero' : emocionM[1],
                              'Emociones' : emocionM[2]
                              })
###################################---CLASE PARA TODAS LAS VENTANAS---#############################################
class registro(tk.Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        registro.configure(root, bg="light cyan")
        root.geometry("300x100")
        self.master = master

        self.lbmensaje = tk.Label(root, text="¿Desea iniciar sesion cómo médico o paciente?", bg="light cyan")
        self.lbmensaje.grid(column=0, row=1, padx=(20, 10))

        self.btnMedico = tk.Button(root, text="Médico", command=self.VentanaInicioSesionMedico, bg="pale turquoise",
                                        fg="black")
        self.btnMedico.grid(column=0, row=2, pady=5, columnspan=1, padx=(20, 10))

        self.btnPaciente = tk.Button(root, text="Paciente", command=self.VentanaInicioSesionPaciente, bg="pale turquoise",
                                          fg="black")
        self.btnPaciente.grid(column=0, row=3, pady=5, columnspan=1, padx=(20, 10))

##################################-------PARTE MÉDICO-------###################################################
################################################################################################################
    def VentanaInicioSesionMedico(self):
        ventanaInicioMedico = tk.Toplevel(bg="light cyan")
        ventanaInicioMedico.title("Inicio Sesion Médico.")
        ventanaInicioMedico.geometry("450x125")

        ventanaInicioMedico.lbUsuario = tk.Label(ventanaInicioMedico, text="Usuario", bg="light cyan")
        self.usuario = tk.StringVar()
        ventanaInicioMedico.entryUs = tk.Entry(ventanaInicioMedico, textvariable=self.usuario, width=45)
        ventanaInicioMedico.lbUsuario.grid(column=0, row=0, padx=(20, 10))
        ventanaInicioMedico.entryUs.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))

        ventanaInicioMedico.lbContrasena = tk.Label(ventanaInicioMedico, text="Contraseña", bg="light cyan")
        self.contrasena = tk.StringVar()
        ventanaInicioMedico.entryCon = tk.Entry(ventanaInicioMedico, text=self.contrasena, width=45)
        ventanaInicioMedico.lbContrasena.grid(column=0, row=1, padx=(20, 10))
        ventanaInicioMedico.entryCon.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))

        ventanaInicioMedico.button1 = tk.Button(ventanaInicioMedico, text="Iniciar Sesión",
                                                command=self.IniciarSesionMedico, bg="white", fg='black')
        ventanaInicioMedico.button1.grid(column=1, row=3, pady=15)

        ventanaInicioMedico.button1 = tk.Button(ventanaInicioMedico, text="Registrarse", command=self.RegistroMedico,
                                                bg="white", fg='black')
        ventanaInicioMedico.button1.grid(column=2, row=3, pady=15)

        ventanaInicioMedico.button1 = tk.Button(ventanaInicioMedico, text="Salir", command=self.SalirMedico, bg="white",
                                                fg='black')
        ventanaInicioMedico.button1.grid(column=3, row=3, pady=15)
    def SalirMedico(self):
        MsgBox = tk.messagebox.askquestion("Salir", "¿Está seguro que desea salir?", icon="warning")
        if MsgBox == 'yes':
            root.destroy()
        else:
            tk.messagebox.showinfo("Listo!", "Se ha regresado a la pantalla principal")

    def IniciarSesionMedico(self):
        lista = ObtenerMedico()
        for x in lista:
            usuario = x['Codigo de medico']
            contra = x['Contraseña']
            if self.usuario.get() == usuario and self.contrasena.get() == contra:
                self.VentanaMedico()
                return
            if self.usuario.get() == usuario and self.contrasena.get() != contra:
                messagebox.showinfo("Error", "Contreseña Incorrecta. Verifique que este correcta.")
                break

    def VentanaMedico(self):
        ventana = tk.Toplevel()
        ventana.title("Hospital")
        ventana.geometry("500x300")
        barra = tk.Menu(ventana)

        # OPCIONES DE LA BARRA DE MÉDICO
        medico = tk.Menu(barra, tearoff=0)
        medico.add_command(label="Editar", command=self.VentanaEditarMedico)
        medico.add_separator()
        medico.add_command(label="Mostrar", command=self.VentanaMostrarMedico)
        medico.add_separator()
        medico.add_command(label="Eliminar", command=self.VentanaEliminarMedico)

        # OPCIONES DE LA BARRA HISTORIAL
        historial = tk.Menu(barra, tearoff=0)
        historial.add_command(label="Médico", command=self.HistorialMedico)
        historial.add_separator()
        historial.add_command(label="Obtener Historial Paciente", command=self.ObtenerHistorialPaciente)

        # OPCIONES DE LA BARRA PARTE MEDICO
        partemedico = tk.Menu(barra, tearoff=0)
        partemedico.add_command(label="Diagnostico", command=self.ParteMedico)

        # OPCIONES DE LA BARRA FACTURACIÓN
        facturacion = tk.Menu(barra, tearoff=0)
        facturacion.add_command(label="Crear", command=self.VentanaCrearFactura)
        facturacion.add_separator()
        facturacion.add_command(label="Obtener", command=self.VentanaObtenerFactura)
        facturacion.add_separator()
        facturacion.add_command(label="Cambiar estatus", command=self.CambiarEstatusFactura)

        # OPCIONES DE LA BARRA ESTADISTICA
        estadistica = tk.Menu(barra, tearoff=0)
        estadistica.add_command(label="Obtener", command=self.VentanaObtenerEstadistica)

        # BARRAS DE LA VENTANA DE INICIO DE SESIÓN
        barra.add_cascade(label="Médico", menu=medico)
        barra.add_cascade(label="Historial", menu=historial)
        barra.add_cascade(label="Parte Médico", menu=partemedico)
        barra.add_cascade(label="Facturación", menu=facturacion)
        barra.add_cascade(label="Estadisticas", menu=estadistica)

        ventana.config(menu=barra)

        ventana.mainloop()

    def RegistroMedico(self):
        ventana1 = tk.Toplevel()
        ventana1.title("Crear Medico")
        ventana1.geometry("450x250")

        # Ventanas de medico

        ventana1.lbImagen = tk.Label(ventana1, text="Id")
        ventana1.lbNombre = tk.Label(ventana1, text="Nombre del médico")
        ventana1.lbApeliido = tk.Label(ventana1, text="Apellido del médico")
        ventana1.lbCodigoMedico = tk.Label(ventana1, text="Codigo médico")
        ventana1.lbContrasenna = tk.Label(ventana1, text="Contraseña")
        ventana1.lbSalario = tk.Label(ventana1, text="Salario")

        # Campos para escribir
        self.idMedico = tk.StringVar()
        ventana1.entryIdMedico = tk.Entry(ventana1, textvariable=self.idMedico, width=40)

        self.nombreMedico = tk.StringVar()
        ventana1.entryNombreMedico = tk.Entry(ventana1, textvariable=self.nombreMedico, width=40)

        self.ApellidoMedico = tk.StringVar()
        ventana1.entryApellidoMedico = tk.Entry(ventana1, textvariable=self.ApellidoMedico, width=40)

        self.CodigoMedico = tk.StringVar()
        ventana1.entryCodigoMedico = tk.Entry(ventana1, textvariable=self.CodigoMedico, width=40)

        self.Contrasenna = tk.StringVar()
        ventana1.entryContrasenna = tk.Entry(ventana1, textvariable=self.Contrasenna, width=40)

        self.Salario = tk.StringVar()
        ventana1.entrySalario = tk.Entry(ventana1, textvariable=self.Salario, width=40)
        # Boton Salir
        ventana1.btnSalir = tk.Button(ventana1, text="Salir",
                                      command=lambda: self.CerrarVentanaMedico(ventana1.destroy()))
        # Boton Guardar
        ventana1.btnGuardar = tk.Button(ventana1, text="Guardar",
                                        command=lambda: self.GuardarRegistroMedico(
                                            self.idMedico.get(),
                                            self.nombreMedico.get(),
                                            self.ApellidoMedico.get(),
                                            self.CodigoMedico.get(),
                                            self.Contrasenna.get(),
                                            self.Salario.get()))

        ventana1.lbImagen.grid(column=0, row=0, padx=(20, 10))
        ventana1.lbNombre.grid(column=0, row=1, padx=(20, 10))
        ventana1.lbApeliido.grid(column=0, row=2, padx=(20, 10))
        ventana1.lbCodigoMedico.grid(column=0, row=3, padx=(20, 10))
        ventana1.lbContrasenna.grid(column=0, row=4, padx=(20, 10))
        ventana1.lbSalario.grid(column=0, row=5, padx=(20, 10))

        ventana1.entryIdMedico.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventana1.entryNombreMedico.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventana1.entryApellidoMedico.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        ventana1.entryCodigoMedico.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        ventana1.entryContrasenna.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        ventana1.entrySalario.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))

        ventana1.btnSalir.grid(column=1, row=6, pady=15)
        ventana1.btnGuardar.grid(column=0, row=6, pady=15)

    def GuardarRegistroMedico(self, *argumentos):
        messagebox.showinfo("Información", "Registro almacenado")
        nuevoCurso = [argumentos[0], argumentos[1], argumentos[2], argumentos[3], argumentos[4], argumentos[5]]
        CrearArchivoMedico()
        file = open("Datos/medico.txt", "a")
        file.write(str(argumentos[0]) + ",")
        file.write(str(argumentos[1]) + ",")
        file.write(str(argumentos[2]) + ",")
        file.write(str(argumentos[3]) + ",")
        file.write(str(argumentos[4]) + ",")
        file.write(str(argumentos[5]) + ",")
        file.write("\n")
        file.close()
        return {'Id': argumentos[0],
                'Nombre': argumentos[1],
                'Apellido': argumentos[2],
                'Codigo de medico': argumentos[3],
                'Contraseña': argumentos[4],
                'Salario por hora': argumentos[5]
                }

    # DATOS DE MEDICO
    def VentanaEditarMedico(self):
        ventana = tk.Toplevel()
        ventana.title("Editar")
        ventana.geometry("450x250")

        ventana.lbId = tk.Label(ventana, text="Id")
        ventana.lbNombre = tk.Label(ventana, text="Nombre del médico")
        ventana.lbApeliido = tk.Label(ventana, text="Apellido del médico")
        ventana.lbCodigoMedico = tk.Label(ventana, text="Codigo médico")
        ventana.lbContrasenna = tk.Label(ventana, text="Contraseña")
        ventana.lbSalario = tk.Label(ventana, text="Salario")

        self.idMed = tk.StringVar()
        ventana.entryIdmed = tk.Entry(ventana, textvariable=self.idMed, width=40)

        self.nuevoNombreMedico = tk.StringVar()
        ventana.entryNuevoNombreMedico = tk.Entry(ventana, textvariable=self.nuevoNombreMedico, width=40)

        self.nuevoApellidoMedico = tk.StringVar()
        ventana.entryNuevoApellidoMedico = tk.Entry(ventana, textvariable=self.nuevoApellidoMedico, width=40)

        self.nuevoCodigoMedico = tk.StringVar()
        ventana.entryNuevoCodigoMedico = tk.Entry(ventana, textvariable=self.nuevoCodigoMedico, width=40)

        self.nuevaContrasennaMedico = tk.StringVar()
        ventana.entryNuevaContrasennaMedico = tk.Entry(ventana, textvariable=self.nuevaContrasennaMedico, width=40)

        self.nuevoSalarioMedico = tk.StringVar()
        ventana.entryNuevoSalarioMedico = tk.Entry(ventana, textvariable=self.nuevoSalarioMedico, width=40)

        ventana.lbId.grid(column=0, row=0, padx=(20, 10))
        ventana.lbNombre.grid(column=0, row=1, padx=(20, 10))
        ventana.lbApeliido.grid(column=0, row=2, padx=(20, 10))
        ventana.lbCodigoMedico.grid(column=0, row=3, padx=(20, 10))
        ventana.lbContrasenna.grid(column=0, row=4, padx=(20, 10))
        ventana.lbSalario.grid(column=0, row=5, padx=(20, 10))

        ventana.entryIdmed.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventana.entryNuevoNombreMedico.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventana.entryNuevoApellidoMedico.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        ventana.entryNuevoCodigoMedico.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        ventana.entryNuevaContrasennaMedico.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        ventana.entryNuevoSalarioMedico.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))

        ventana.btnSalir = tk.Button(ventana, text="Salir",
                                     command=lambda: self.CerrarVentanaMedico(ventana.destroy()))
        ventana.btnOk = tk.Button(ventana, text="Aceptar",
                                  command=lambda: self.EditarMedico(self.idMed.get(), self.nuevoNombreMedico.get(),
                                                                    self.nuevoApellidoMedico.get(),
                                                                    self.nuevoCodigoMedico.get(),
                                                                    self.nuevaContrasennaMedico.get(),
                                                                    self.nuevoSalarioMedico.get()))

        ventana.btnOk.grid(column=0, row=6, pady=15)
        ventana.btnSalir.grid(column=1, row=6, pady=15)

    def EditarMedico(self, id, nombre, apellido, codigomedico, contrasena, salario):
        CrearArchivoMedico()
        file = open("Datos/medico.txt", "r")
        filas = file.readlines()
        filasTemporal = []
        for fila in filas:
            medico = fila.split(",")
            if str(medico[0]) == id:
                filaModificada = str(id) + ","
                filaModificada = filaModificada + str(nombre) + ","
                filaModificada = filaModificada + str(apellido) + ","
                filaModificada = filaModificada + str(codigomedico) + ","
                filaModificada = filaModificada + str(contrasena) + ","
                filaModificada = filaModificada + str(salario)
                filaModificada = filaModificada + "\n"
                filasTemporal.append(filaModificada)
            else:
                filasTemporal.append(fila)
        file.close()
        file = open("Datos/medico.txt", "w")
        for fila in filasTemporal:
            file.write(fila)
        file.close()
        messagebox.showinfo("Información", "Editado")

    def VentanaMostrarMedico(self):
        ventanavermedico = tk.Toplevel()
        ventanavermedico.geometry("500x250")
        ventanavermedico.title("Agenda de medicos.")

        ventanavermedico.lbIdmedico = tk.Label(ventanavermedico, text="Id")
        ventanavermedico.lbNombremedico = tk.Label(ventanavermedico, text="Nombre")
        ventanavermedico.lbApellidomedico = tk.Label(ventanavermedico, text="Apellido")
        ventanavermedico.lbCodigomedico = tk.Label(ventanavermedico, text="Codigo de medico")
        ventanavermedico.lbContramedico = tk.Label(ventanavermedico, text="Contraseña")
        ventanavermedico.lbSalariomedico = tk.Label(ventanavermedico, text="Salario")

        self.IdMedi = tk.StringVar()
        ventanavermedico.txtidmedico = tk.Entry(ventanavermedico, textvariable=self.IdMedi, width=40)

        self.nombremedi = tk.StringVar()
        ventanavermedico.txtnombreMedi = tk.Entry(ventanavermedico, textvariable=self.nombremedi, width=40)

        self.apellidomedi = tk.StringVar()
        ventanavermedico.txtApellidomedi = tk.Entry(ventanavermedico, textvariable=self.apellidomedi, width=40)

        self.codigomedi = tk.StringVar()
        ventanavermedico.txtcodigoMedico = tk.Entry(ventanavermedico, textvariable=self.codigomedi, width=40)

        self.contramedi = tk.StringVar()
        ventanavermedico.txtcontraMedico = tk.Entry(ventanavermedico, textvariable=self.contramedi, width=40)

        self.salmedi = tk.StringVar()
        ventanavermedico.txtsalmedi = tk.Entry(ventanavermedico, textvariable=self.salmedi, width=40)

        ventanavermedico.btnSalir = tk.Button(ventanavermedico, text="Salir", command=self.SalirMedico)
        ventanavermedico.btnSiguiente = tk.Button(ventanavermedico, text="Siguiente", command=self.SiguienteRegistroMedico)
        ventanavermedico.btnAnterior = tk.Button(ventanavermedico, text="Anterior", command=self.AnteriorRegistroMedico)

        ventanavermedico.lbIdmedico.grid(column=0, row=0, padx=(20, 10))
        ventanavermedico.lbNombremedico.grid(column=0, row=1, padx=(20, 10))
        ventanavermedico.lbApellidomedico.grid(column=0, row=2, padx=(20, 10))
        ventanavermedico.lbCodigomedico.grid(column=0, row=3, padx=(20, 10))
        ventanavermedico.lbContramedico.grid(column=0, row=4, padx=(20, 10))
        ventanavermedico.lbSalariomedico.grid(column=0, row=5, padx=(20, 10))

        ventanavermedico.txtidmedico.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventanavermedico.txtnombreMedi.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventanavermedico.txtApellidomedi.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        ventanavermedico.txtcodigoMedico.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        ventanavermedico.txtcontraMedico.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        ventanavermedico.txtsalmedi.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))

        ventanavermedico.btnAnterior.grid(column=0, row=6, pady=15)
        ventanavermedico.btnSiguiente.grid(column=1, row=6, pady=15)
        ventanavermedico.btnSalir.grid(column=2, row=6, pady=15)


    def VerRegistroMedico(self):
        global registroActualMedico
        listaPersonasMedico = ObtenerMedico()
        personame = listaPersonasMedico[registroActualMedico]
        self.IdMedi.set(personame['Id'])
        self.nombremedi.set(personame["Nombre"])
        self.apellidomedi.set(personame["Apellido"])
        self.codigomedi.set(personame["Codigo de medico"])
        self.contramedi.set(personame["Contraseña"])
        self.salmedi.set(personame["Salario"])

    def SiguienteRegistroMedico(self):
        global registroActualMedico
        listaPersonasMedico = ObtenerMedico()
        if registroActualMedico < len(listaPersonasMedico) - 1:
            registroActualMedico += 1
            self.VerRegistroMedico()

    def AnteriorRegistroMedico(self):
        global registroActualMedico
        listaPersonas = ObtenerMedico()
        if registroActualMedico > 0:
            registroActualMedico -= 1
            self.VerRegistroMedico()

    def VentanaEliminarMedico(self):
        ventanaEliminarMedico = tk.Toplevel()
        ventanaEliminarMedico.title("Eliminar")
        ventanaEliminarMedico.geometry("350x100")

        # CAMPO PARA INGRESAR ID
        ventanaEliminarMedico.lbIdMedi = tk.Label(ventanaEliminarMedico, text="Id")
        self.idmedi = tk.StringVar()
        ventanaEliminarMedico.entryIdMedi = tk.Entry(ventanaEliminarMedico, textvariable=self.idmedi, width=40)
        ventanaEliminarMedico.lbIdMedi.grid(column=0, row=0, padx=(20, 10))
        ventanaEliminarMedico.entryIdMedi.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))

        # BOTON ELIMINAR
        ventanaEliminarMedico.btnOkMedi = tk.Button(ventanaEliminarMedico, text="Eliminar",
                                                      command=self.EliminarMedico)
        ventanaEliminarMedico.btnOkMedi.grid(column=0, row=5, pady=15)

        # BOTON SALIR
        ventanaEliminarMedico.btnSalir = tk.Button(ventanaEliminarMedico, text="Salir",
                                                     command=self.CerrarVentanaEliminar)
        ventanaEliminarMedico.btnSalir.grid(column=1, row=5, pady=15)

    def EliminarMedico(self):
        messagebox.showinfo("Eliminado", "Datos eliminados")
        CrearArchivoMedico()
        file = open("Datos/medico.txt", "r")
        filas = file.readlines()
        filasTemporal = []
        for fila in filas:
            medico = fila.split(",")
            if medico[0] != self.idmedi.get():
                filasTemporal.append(fila)
        file.close()
        file = open("Datos/medico.txt", "w")
        for fila in filasTemporal:
            file.write(fila)
        file.close()

        #### VENTANAS DE HISTORIALES ####

    def HistorialMedico(self):
        ventanahistorialme = tk.Toplevel()
        ventanahistorialme.title("Historial Médico")
        ventanahistorialme.geometry("250x150")

        ventanahistorialme.btnMedico = tk.Button(ventanahistorialme, text="Crear historial",
                                                 command=self.CrearHistorialMedico, bg="pale turquoise",
                                                 fg="black")
        ventanahistorialme.btnMedico.grid(column=3, row=3, pady=5, columnspan=2, padx=(30, 20))

        ventanahistorialme.btnPaciente = tk.Button(ventanahistorialme, text="Obtener historial",
                                                   command=self.ObtenerHistorialMedico,
                                                   bg="pale turquoise",
                                                   fg="black")
        ventanahistorialme.btnPaciente.grid(column=3, row=4, pady=5, columnspan=2, padx=(30, 20))

        ventanahistorialme.btnPaciente = tk.Button(ventanahistorialme, text="Emociones",
                                                   command=self.VentanaEmocionesMedico,
                                                   bg="pale turquoise",
                                                   fg="black")
        ventanahistorialme.btnPaciente.grid(column=3, row=5, pady=5, columnspan=2, padx=(30, 20))

    def CrearHistorialMedico(self):
        ventana3 = tk.Toplevel()
        ventana3.title("Crear Historial Medico")
        ventana3.geometry("450x270")

        # Ventanas de medico

        ventana3.lbId = tk.Label(ventana3, text="Id medico:")
        ventana3.lbMedico = tk.Label(ventana3, text="Medico")
        ventana3.lbPaciente = tk.Label(ventana3, text="Paciente")
        ventana3.lbFecha = tk.Label(ventana3, text="Fecha")
        ventana3.lbCantidadMinutos = tk.Label(ventana3, text="Cantidad de minutos")
        ventana3.lbPrecioHora = tk.Label(ventana3, text="Precio hora")
        ventana3.lbPrecioTotal = tk.Label(ventana3, text="Precio total")
        ventana3.lbParteMedicoMedico = tk.Label(ventana3, text="Parte Medico")

        # Campos para escribir

        self.IDMedico = tk.StringVar()
        ventana3.entryIDMedico = tk.Entry(ventana3, textvariable=self.IDMedico, width=40)

        self.medico = tk.StringVar()
        ventana3.entrymedico = tk.Entry(ventana3, textvariable=self.medico, width=40)

        self.paciente = tk.StringVar()
        ventana3.entrypaciente = tk.Entry(ventana3, textvariable=self.paciente, width=40)

        self.fecha = tk.StringVar()
        ventana3.entryfecha = tk.Entry(ventana3, textvariable=self.fecha, width=40)

        self.cantidadMinutos = tk.StringVar()
        ventana3.entrycantidadMinutos = tk.Entry(ventana3, textvariable=self.cantidadMinutos, width=40)

        self.preciohora = tk.StringVar()
        ventana3.entryPrecioHora = tk.Entry(ventana3, textvariable=self.preciohora, width=40)

        self.preciototal = tk.StringVar()
        ventana3.entryPrecioTotal = tk.Entry(ventana3, textvariable=self.preciototal, width=40)

        self.parteMedicoMedico = tk.StringVar()
        ventana3.entryParteMedicoMedico = tk.Entry(ventana3, textvariable=self.parteMedicoMedico, width=40)

        # Boton Salir
        ventana3.btnSalir = tk.Button(ventana3, text="Salir",
                                      command=lambda: self.CerrarVentanaMedico(ventana3.destroy()))
        # Boton Guardar
        ventana3.btnGuardar = tk.Button(ventana3, text="Guardar",
                                        command=lambda: self.GuardarHistorialMedico(
                                            self.IDMedico.get(),
                                            self.medico.get(),
                                            self.paciente.get(),
                                            self.fecha.get(),
                                            self.cantidadMinutos.get(),
                                            self.preciohora.get(),
                                            self.preciototal.get(),
                                            self.parteMedicoMedico.get()
                                        ))

        ventana3.lbId.grid(column=0, row=0, padx=(20, 10))
        ventana3.lbMedico.grid(column=0, row=1, padx=(20, 10))
        ventana3.lbPaciente.grid(column=0, row=2, padx=(20, 10))
        ventana3.lbFecha.grid(column=0, row=3, padx=(20, 10))
        ventana3.lbCantidadMinutos.grid(column=0, row=4, padx=(20, 10))
        ventana3.lbPrecioHora.grid(column=0, row=5, padx=(20, 10))
        ventana3.lbPrecioTotal.grid(column=0, row=6, padx=(20, 10))
        ventana3.lbParteMedicoMedico.grid(column=0, row=7, padx=(20, 10))

        ventana3.entryIDMedico.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventana3.entrymedico.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventana3.entrypaciente.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        ventana3.entryfecha.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        ventana3.entrycantidadMinutos.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        ventana3.entryPrecioHora.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))
        ventana3.entryPrecioTotal.grid(column=1, row=6, pady=5, columnspan=2, padx=(20, 10))
        ventana3.entryParteMedicoMedico.grid(column=1, row=7, pady=5, columnspan=2, padx=(20, 10))

        ventana3.btnSalir.grid(column=2, row=8, pady=15)
        ventana3.btnGuardar.grid(column=1, row=8, pady=15)

    def GuardarHistorialMedico(self, *argumentos):
        reconocimiento = Reconocimiento()
        reconocimiento.Configuracion()
        reconocimiento.Iniciar()
        parteMedico = reconocimiento.ReconocimientoEmociones(self.parteMedicoMedico.get())
        for x in parteMedico:
            anger = x['faceAttributes']['emotion']['anger']
            disgust = x['faceAttributes']['emotion']['disgust']
            contempt = x['faceAttributes']['emotion']['contempt']
            sadness = x['faceAttributes']['emotion']['sadness']
            happiness = x['faceAttributes']['emotion']['happiness']
            surprise = x['faceAttributes']['emotion']['surprise']
            fear = x['faceAttributes']['emotion']['fear']
            neutral = x['faceAttributes']['emotion']['neutral']
            if anger >= 0.500 or disgust >= 0.250:
                list.append("El diagnostico es problema de tiroides.")
            if contempt >= 0.700 or sadness >= 0.100:
                list.append("El diagnostico es trombo vascular en el cerebro.")
            if disgust >= 0.500 or anger >= 0.100:
                list.append("El diagnostico es malestar estomacal.")
            if happiness >= 0.500 or surprise >= 0.250:
                list.append("El diagnostico es adiccion a las drogas.")
            if fear >= 0.400 or neutral >= 0.200:
                list.append("El diagnostico es hipertencion arterial.")
            if sadness >= 0.250 or neutral >= 0.200 or disgust >= 0.250:
                list.append("El diagnostico es tension muscular.")
            if disgust >= 0.520 or neutral >= 0.100 or sadness >= 0.400:
                list.append("El diagnostico es trastorno bipolar.")
            if disgust >= 0.200 or sadness >= 0.100 or anger >= 0.200:
                list.append("El diagnostico es depresion.")
            if happiness >= 0.250 or surprise >= 0.200 or disgust >= 0.100:
                list.append("El diagnostico es desordenes de ansiedad.")
            elif anger >= 0.250 or neutral >= 0.100 or sadness >= 0.150:
                list.append("El diagnostico es gastritis.")
            else:
                list.append("El paciente es super sano")
        messagebox.showinfo("Información", "Registro almacenado")
        CrearArchivoHistorialMedico()
        file = open("Datos/historial_medico.txt", "a")
        file.write(str(argumentos[0]) + ", ")
        file.write(str(argumentos[1]) + ", ")
        file.write(str(argumentos[2]) + ", ")
        file.write(str(argumentos[3]) + ", ")
        file.write(str(argumentos[4]) + ", ")
        file.write(str(argumentos[5])+ ", ")
        file.write(str(argumentos[6]) + ", ")
        file.write(str(list))
        file.write("\n")
        file.close()
        return {'Id':argumentos[0],
            'Fecha': argumentos[1],
            'Paciente': argumentos[2],
            'Medico': argumentos[3],
            'Minutos': argumentos[4],
            'Precio por hora': argumentos[5],
            'Precio total': argumentos[6],
            'Parte Medico:': list
        }

    def VentanaEmocionesMedico(self):
        ventana9= tk.Toplevel()
        ventana9.title("Emociones")
        ventana9.geometry("400x150")

        ventana9.lbID = tk.Label(ventana9, text="Id")
        ventana9.lbG = tk.Label(ventana9, text="Genero")
        ventana9.lbE = tk.Label(ventana9, text="Emociones")

        self.idemoMedico = tk.StringVar()
        ventana9.entryID = tk.Entry(ventana9,textvariable=self.idemoMedico, width=40)
        self.generoemoMedico = tk.StringVar()
        ventana9.entryG = tk.Entry(ventana9, textvariable=self.generoemoMedico, width=40)
        self.emoMedico = tk.StringVar()
        ventana9.entryEmo = tk.Entry(ventana9, textvariable=self.emoMedico, width=40)

        ventana9.btnGuardar = tk.Button(ventana9, text="Guardar",
                                                        command= self.GuardarEmocionesMedico)
        ventana9.btnSalir = tk.Button(ventana9, text="Salir",
                                                      command=lambda: self.CerrarVentanaPaciente(
                                                          ventana9.destroy()))
        ventana9.lbID.grid(column=0, row=0, padx=(20, 10))
        ventana9.lbG.grid(column=0, row=1, padx=(20, 10))
        ventana9.lbE.grid(column=0, row=2, padx=(20, 10))

        ventana9.entryID.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventana9.entryG.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventana9.entryEmo.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))

        ventana9.btnGuardar.grid(column=0, row=3, pady=15)
        ventana9.btnSalir.grid(column=1, row=3, pady=15)

    def GuardarEmocionesMedico(self):
        messagebox.showinfo("Informacion","Emociones Guardadas")
        reconocimiento = Reconocimiento()
        reconocimiento.Configuracion()
        reconocimiento.Iniciar()
        emocion = reconocimiento.ReconocimientoEmociones(self.emoMedico.get())
        for x in emocion:
            e = x['faceAttributes']['emotion']
        file = open("Datos/emociones_medico.txt", "a")
        file.write(str(self.idemoMedico.get()) + ",")
        file.write(str(self.generoemoMedico.get()) + ",")
        file.write(str(e))
        file.write("\n")
        file.close()
        return {'Id': self.idemoMedico.get(),
                'Genero': self.generoemoMedico.get(),
                'Enfermedades': e
                }

    def ObtenerHistorialPaciente(self):
        venMostrarHistorialPaciente = tk.Toplevel()
        venMostrarHistorialPaciente.geometry("550x350")
        venMostrarHistorialPaciente.title("Mostrar historial Paciente")

        venMostrarHistorialPaciente.idPacienteeH = tk.Label(venMostrarHistorialPaciente, text="Id")
        venMostrarHistorialPaciente.Fechaa = tk.Label(venMostrarHistorialPaciente, text="Fecha")
        venMostrarHistorialPaciente.generoo = tk.Label(venMostrarHistorialPaciente, text="Genero")
        venMostrarHistorialPaciente.Pacientee = tk.Label(venMostrarHistorialPaciente, text="Paciente")
        venMostrarHistorialPaciente.Medicoo = tk.Label(venMostrarHistorialPaciente, text="Medico")
        venMostrarHistorialPaciente.ParteMedicoo = tk.Label(venMostrarHistorialPaciente, text="Parte medico")

        self.idPacienteMostrarH = tk.StringVar()
        venMostrarHistorialPaciente.idPacientee = tk.Entry(venMostrarHistorialPaciente, textvariable=self.idPacienteMostrarH, width=40)

        self.FechaMostrarM = tk.StringVar()
        venMostrarHistorialPaciente.FechaM = tk.Entry(venMostrarHistorialPaciente, textvariable=self.FechaMostrarM, width=40)

        self.GeneroMostrar = tk.StringVar()
        venMostrarHistorialPaciente.GeneroM = tk.Entry(venMostrarHistorialPaciente, textvariable=self.GeneroMostrar,width=40)

        self.pacienteMostrarM = tk.StringVar()
        venMostrarHistorialPaciente.pacienteM = tk.Entry(venMostrarHistorialPaciente,textvariable=self.pacienteMostrarM,width=40)

        self.medicoMostrarM = tk.StringVar()
        venMostrarHistorialPaciente.medicoM = tk.Entry(venMostrarHistorialPaciente, textvariable=self.medicoMostrarM,width=40)

        self.ParteMedicoMostrarPaciente = tk.StringVar()
        venMostrarHistorialPaciente.ParteMedico= tk.Entry(venMostrarHistorialPaciente, textvariable=self.ParteMedicoMostrarPaciente, width=40)


        venMostrarHistorialPaciente.btnSalir = tk.Button(venMostrarHistorialPaciente, text="Salir",
                                                       command=self.SalirPaciente)
        venMostrarHistorialPaciente.btnSiguiente = tk.Button(venMostrarHistorialPaciente, text="Siguiente",
                                                           command=self.SiguienteRegistroHistorialPaciente)
        venMostrarHistorialPaciente.btnAnterior = tk.Button(venMostrarHistorialPaciente, text="Anterior",
                                                          command=self.AnteriorRegistroHistorialPaciente)

        venMostrarHistorialPaciente.idPacienteeH.grid(column=0, row=0, padx=(20, 10))
        venMostrarHistorialPaciente.Fechaa.grid(column=0, row=1, padx=(20, 10))
        venMostrarHistorialPaciente.generoo.grid(column=0, row=2, padx=(20, 10))
        venMostrarHistorialPaciente.Pacientee.grid(column=0, row=3, padx=(20, 10))
        venMostrarHistorialPaciente.Medicoo.grid(column=0, row=4, padx=(20, 10))
        venMostrarHistorialPaciente.ParteMedicoo.grid(column=0, row=5, padx=(20, 10))

        venMostrarHistorialPaciente.idPacientee.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialPaciente.FechaM.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialPaciente.GeneroM.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialPaciente.pacienteM.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialPaciente.medicoM.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialPaciente.ParteMedico.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))

        venMostrarHistorialPaciente.btnAnterior.grid(column=0, row=8, pady=15)
        venMostrarHistorialPaciente.btnSiguiente.grid(column=1, row=8, pady=15)
        venMostrarHistorialPaciente.btnSalir.grid(column=2, row=8, pady=15)

    def VerRegistroHistorialPaciente(self):
        global registroActualHistorialPaciente
        listaHistorialPaciente = ObtenerHistorialPaciente()
        personaMostraPaciente = listaHistorialPaciente[registroActualHistorialPaciente]
        self.idPacienteMostrarH.set(personaMostraPaciente['Id'])
        self.FechaMostrarM.set(personaMostraPaciente['Fecha'])
        self.GeneroMostrar.set(personaMostraPaciente['Genero'])
        self.pacienteMostrarM.set(personaMostraPaciente['Paciente'])
        self.medicoMostrarM.set(personaMostraPaciente['Medico'])
        self.ParteMedicoMostrarPaciente.set(personaMostraPaciente['Parte medico'])

    def SiguienteRegistroHistorialPaciente(self):
        global registroActualHistorialPaciente
        listaHistorialPaciente = ObtenerHistorialPaciente()
        if registroActualHistorialPaciente < len(listaHistorialPaciente) - 1:
            registroActualHistorialPaciente += 1
            self.VerRegistroHistorialPaciente()

    def AnteriorRegistroHistorialPaciente(self):
        global registroActualHistorialPaciente
        listaHistorialMedico = ObtenerHistorialPaciente()
        if registroActualHistorialPaciente > 0:
            registroActualHistorialPaciente -= 1
            self.VerRegistroHistorialPaciente()

    def ParteMedico(self):
        ventana6 = tk.Toplevel()
        ventana6.title("Parte Médico")
        ventana6.geometry("350x150")

        ventana6.lbId = tk.Label(ventana6, text="Id")
        ventana6.lbImagen = tk.Label(ventana6, text="Imagen")

        self.Id = tk.StringVar()
        ventana6.entryId = tk.Entry(ventana6, textvariable=self.Id, width=40)

        self.Imagen = tk.StringVar()
        ventana6.entryImagen = tk.Entry(ventana6, textvariable=self.Imagen, width=40)

        # Boton Salir
        ventana6.btnSalir = tk.Button(ventana6, text="Salir",
                                                     command=lambda: self.CerrarVentanaPaciente(
                                                         ventana6.destroy()))
        # Boton Guardar
        ventana6.btnGuardar = tk.Button(ventana6, text="Guardar",
                                                       command=self.ReconocimientoEnfermedad)
        ventana6.lbId.grid(column=0, row=0, padx=(20, 10))
        ventana6.lbImagen.grid(column=0, row=1, padx=(20, 10))

        ventana6.entryId.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventana6.entryImagen.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))

        ventana6.btnGuardar.grid(column=0, row=2, pady=15)
        ventana6.btnSalir.grid(column=1, row=2, pady=15)

    def ReconocimientoEnfermedad(self):
        reconocimiento = Reconocimiento()
        reconocimiento.Configuracion()
        reconocimiento.Iniciar()
        texto = reconocimiento.ReconocimientoEmociones(self.Imagen.get())
        for x in texto:
            anger = x['faceAttributes']['emotion']['anger']
            disgust = x['faceAttributes']['emotion']['disgust']
            contempt = x['faceAttributes']['emotion']['contempt']
            sadness = x['faceAttributes']['emotion']['sadness']
            happiness = x['faceAttributes']['emotion']['happiness']
            surprise = x['faceAttributes']['emotion']['surprise']
            fear = x['faceAttributes']['emotion']['fear']
            neutral = x['faceAttributes']['emotion']['neutral']
            if anger >= 0.500 or disgust >= 0.250:
                list.append("El diagnostico es problema de tiroides.")
            if contempt >= 0.700 or sadness >= 0.100:
                list.append("El diagnostico es trombo vascular en el cerebro.")
            if disgust >= 0.500 or anger >= 0.100:
                list.append("El diagnostico es malestar estomacal.")
            if happiness >= 0.500 or surprise >= 0.250:
                list.append("El diagnostico es adiccion a las drogas.")
            if fear >= 0.400 or neutral >= 0.200:
                list.append("El diagnostico es hipertencion arterial.")
            if sadness >= 0.250 or neutral >= 0.200 or disgust >= 0.250:
                list.append("El diagnostico es tension muscular.")
            if disgust >= 0.520 or neutral >= 0.100 or sadness >= 0.400:
                list.append("El diagnostico es trastorno bipolar.")
            if disgust >= 0.200 or sadness >= 0.100 or anger >= 0.200:
                list.append("El diagnostico es depresion.")
            if happiness >= 0.250 or surprise >= 0.200 or disgust >= 0.100:
                list.append("El diagnostico es desordenes de ansiedad.")
            elif anger >= 0.250 or neutral >= 0.100 or sadness >= 0.150:
                list.append("El diagnostico es gastritis.")
            else:
                list.append("El paciente es super sano")
            file = open("Datos/parte_medico.txt", "a")
            file.write(str(self.Id.get())+ ",")
            file.write(str(list))
            file.write("\n")
            file.close()
            return {'Id':self.Id.get(),
                'Enfermedades': list
            }

    def ObtenerHistorialMedico(self):
        venMostrarHistorialMedico = tk.Toplevel()
        venMostrarHistorialMedico.geometry("550x350")
        venMostrarHistorialMedico.title("Mostrar historial Medico")

        venMostrarHistorialMedico.lblIdHisPaciM = tk.Label(venMostrarHistorialMedico, text="Id")
        venMostrarHistorialMedico.lblNombreMedHiM = tk.Label(venMostrarHistorialMedico, text="Medico")
        venMostrarHistorialMedico.lblnombrePasHisM = tk.Label(venMostrarHistorialMedico, text="Paciente")
        venMostrarHistorialMedico.lblFechaPasHisM = tk.Label(venMostrarHistorialMedico, text="Fecha")
        venMostrarHistorialMedico.lblCantidadMedHisM = tk.Label(venMostrarHistorialMedico, text="Cantidad de minutos")
        venMostrarHistorialMedico.lblPrecioMedHisM = tk.Label(venMostrarHistorialMedico, text="Precio hora")
        venMostrarHistorialMedico.lblPrecioToMedHisM= tk.Label(venMostrarHistorialMedico, text="Precio total")
        venMostrarHistorialMedico.lblParteMedicoMostrar = tk.Label(venMostrarHistorialMedico, text="Parte medico")

        self.idMostrar = tk.StringVar()
        venMostrarHistorialMedico.txtidPaciM = tk.Entry(venMostrarHistorialMedico, textvariable=self.idMostrar, width=40)

        self.medicoMostrar = tk.StringVar()
        venMostrarHistorialMedico.txtNompaciM = tk.Entry(venMostrarHistorialMedico, textvariable=self.medicoMostrar, width=40)

        self.pacienteMostrar = tk.StringVar()
        venMostrarHistorialMedico.txtApepaciM = tk.Entry(venMostrarHistorialMedico, textvariable=self.pacienteMostrar, width=40)

        self.FechaMostrar = tk.StringVar()
        venMostrarHistorialMedico.txtCedupaciM = tk.Entry(venMostrarHistorialMedico, textvariable=self.FechaMostrar, width=40)

        self.CantidadMostrar = tk.StringVar()
        venMostrarHistorialMedico.txtConpaciM = tk.Entry(venMostrarHistorialMedico, textvariable=self.CantidadMostrar, width=40)

        self.PrecioMostrar = tk.StringVar()
        venMostrarHistorialMedico.txtDicpaciM = tk.Entry(venMostrarHistorialMedico, textvariable=self.PrecioMostrar, width=40)

        self.PrecioTotMostrar = tk.StringVar()
        venMostrarHistorialMedico.txtGepaciM = tk.Entry(venMostrarHistorialMedico, textvariable=self.PrecioTotMostrar, width=40)

        self.ParteMedicoMostrar = tk.StringVar()
        venMostrarHistorialMedico.txtFepaciM = tk.Entry(venMostrarHistorialMedico, textvariable=self.ParteMedicoMostrar, width=40)

        venMostrarHistorialMedico.btnSalir = tk.Button(venMostrarHistorialMedico, text="Salir", command=self.SalirPaciente)
        venMostrarHistorialMedico.btnSiguiente = tk.Button(venMostrarHistorialMedico, text="Siguiente",
                                                        command=self.SiguienteRegistroHistorialMedico)
        venMostrarHistorialMedico.btnAnterior = tk.Button(venMostrarHistorialMedico, text="Anterior",
                                                       command=self.AnteriorRegistroHistorialMedico)

        venMostrarHistorialMedico.lblIdHisPaciM.grid(column=0, row=0, padx=(20, 10))
        venMostrarHistorialMedico.lblNombreMedHiM.grid(column=0, row=1, padx=(20, 10))
        venMostrarHistorialMedico.lblnombrePasHisM.grid(column=0, row=2, padx=(20, 10))
        venMostrarHistorialMedico.lblFechaPasHisM.grid(column=0, row=3, padx=(20, 10))
        venMostrarHistorialMedico.lblCantidadMedHisM.grid(column=0, row=4, padx=(20, 10))
        venMostrarHistorialMedico.lblPrecioMedHisM.grid(column=0, row=5, padx=(20, 10))
        venMostrarHistorialMedico.lblPrecioToMedHisM.grid(column=0, row=6, padx=(20, 10))
        venMostrarHistorialMedico.lblParteMedicoMostrar.grid(column=0, row=7, padx=(20, 10))

        venMostrarHistorialMedico.txtidPaciM.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialMedico.txtNompaciM.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialMedico.txtApepaciM.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialMedico.txtCedupaciM.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialMedico.txtConpaciM.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialMedico.txtDicpaciM.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialMedico.txtGepaciM.grid(column=1, row=6, pady=5, columnspan=2, padx=(20, 10))
        venMostrarHistorialMedico.txtFepaciM.grid(column=1, row=7, pady=5, columnspan=2, padx=(20, 10))

        venMostrarHistorialMedico.btnAnterior.grid(column=0, row=8, pady=15)
        venMostrarHistorialMedico.btnSiguiente.grid(column=1, row=8, pady=15)
        venMostrarHistorialMedico.btnSalir.grid(column=2, row=8, pady=15)

    def VerRegistroHistorialMedico(self):
        global registroActualHistorialMedico
        listaHistorialMedico = ObtenerHistorialMedico()
        personaMostrar = listaHistorialMedico[registroActualHistorialMedico]
        self.idMostrar.set(personaMostrar['Id'])
        self.medicoMostrar.set(personaMostrar['Medico'])
        self.pacienteMostrar.set(personaMostrar['Paciente'])
        self.FechaMostrar.set(personaMostrar['Fecha'])
        self.CantidadMostrar.set(personaMostrar['Minutos'])
        self.PrecioMostrar.set(personaMostrar['Precio por hora'])
        self.PrecioTotMostrar.set(personaMostrar['Precio total'])
        self.ParteMedicoMostrar.set(personaMostrar['Parte medico'])

    def SiguienteRegistroHistorialMedico(self):
        global registroActualHistorialMedico
        listaHistorialMedico = ObtenerPaciente()
        if registroActualHistorialMedico < len(listaHistorialMedico) - 1:
            registroActualHistorialMedico += 1
            self.VerRegistroHistorialMedico()

    def AnteriorRegistroHistorialMedico(self):
        global registroActualHistorialMedico
        listaHistorialMedico = ObtenerHistorialMedico()
        if registroActualHistorialMedico > 0:
            registroActualHistorialMedico -= 1
            self.VerRegistroHistorialMedico()

    def CerrarVentanaMedico(self, *argumentos):
        messagebox.showinfo("Datos Registrados", "Gracias por utilizar nuestros servicios")

    ########################################-----------PARTE PACIENTE-----############################################
###################################################################################################################
    def VentanaInicioSesionPaciente(self):
        ventanaInicioPaciente = tk.Toplevel(bg="light cyan")
        ventanaInicioPaciente.title("Inicio Sesion Paciente.")
        ventanaInicioPaciente.geometry("450x125")

        ventanaInicioPaciente.lbUsuario = tk.Label(ventanaInicioPaciente, text="Cédula", bg="light cyan")
        self.usuario = tk.StringVar()
        ventanaInicioPaciente.entryUs = tk.Entry(ventanaInicioPaciente, textvariable=self.usuario, width=45)
        ventanaInicioPaciente.lbUsuario.grid(column=0, row=0, padx=(20, 10))
        ventanaInicioPaciente.entryUs.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))

        ventanaInicioPaciente.lbContrasena = tk.Label(ventanaInicioPaciente, text="Contraseña", bg="light cyan")
        self.contrasena = tk.StringVar()
        ventanaInicioPaciente.entryCon = tk.Entry(ventanaInicioPaciente, text=self.contrasena, width=45)
        ventanaInicioPaciente.lbContrasena.grid(column=0, row=1, padx=(20, 10))
        ventanaInicioPaciente.entryCon.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))

        ventanaInicioPaciente.button1 = tk.Button(ventanaInicioPaciente, text="Iniciar Sesión",
                                                  command=self.InicioSesionPaciente, bg="white", fg='black')
        ventanaInicioPaciente.button1.grid(column=1, row=3, pady=15)

        ventanaInicioPaciente.button1 = tk.Button(ventanaInicioPaciente, text="Registrarse", command=self.RegistrarsePaciente,
                                                  bg="white", fg='black')
        ventanaInicioPaciente.button1.grid(column=2, row=3, pady=15)

        ventanaInicioPaciente.button1 = tk.Button(ventanaInicioPaciente, text="Salir", command=self.SalirPaciente, bg="white",
                                                  fg='black')
        ventanaInicioPaciente.button1.grid(column=3, row=3, pady=15)

    #BOTON SALIR PARA EL INICIO SESION PACIENTE
    def SalirPaciente(self):
        MsgBox = tk.messagebox.askquestion("Salir", "¿Está seguro que desea salir?", icon="warning")
        if MsgBox == 'yes':
            root.destroy()
        else:
            tk.messagebox.showinfo("Listo!", "Se ha regresado a la pantalla principal")

##############################################INICIO DE SESIÓN PACIENTE#######################################################
    def InicioSesionPaciente(self):
        lista = ObtenerPaciente()
        for x in lista:
            usuario = x['Cedula']
            contra = x['Contraseña']
            if self.usuario.get() == usuario and self.contrasena.get() == contra:
                self.VentanaPaciente()
                return
            if self.usuario.get() == usuario and self.contrasena.get() != contra:
                messagebox.showinfo("Error", "Contreseña Incorrecta. Verifique que este correcta.")
                break

##################################################################VENTADAS DEL MENÚ CUANDO INGRESA DEL PACIENTE##########################################################################
    def VentanaPaciente(self):
        ventanapaciente = tk.Toplevel()
        ventanapaciente.title("Hospital")
        ventanapaciente.geometry("400x250")
        barra = tk.Menu(ventanapaciente)

        # OPCIONES DE LA BARRA DE PACIENTE
        paciente = tk.Menu(barra, tearoff=0)
        paciente.add_command(label="Editar", command=self.VentanaEditarPaciente)
        paciente.add_separator()
        paciente.add_command(label="Mostrar", command=self.MostrarPaciente)
        paciente.add_separator()
        paciente.add_command(label="Eliminar", command=self.VentanaEliminarPaciente)

        # OPCIONES DE LA BARRA HISTORIAL
        historial = tk.Menu(barra, tearoff=0)
        historial.add_command(label="Crear cita", command=self.CrearHistorialPaciente)
        historial.add_separator()
        historial.add_command(label="Emociones", command=self.VentanaEmociones)

        # OPCIONES DE LA BARRA PARTE MEDICO
        partemedico = tk.Menu(barra, tearoff=0)
        partemedico.add_command(label="Diagnostico", command=self.ParteMedicoPaciente)

        # OPCIONES DE LA BARRA FACTURACIÓN
        facturacion = tk.Menu(barra, tearoff=0)
        facturacion.add_command(label="Obtener", command=self.VentanaObtenerFactura)

        # BARRAS DE LA VENTANA DE INICIO DE SESIÓN
        barra.add_cascade(label="Paciente", menu=paciente)
        barra.add_cascade(label="Historial", menu=historial)
        barra.add_cascade(label="Parte Médico", menu=partemedico)
        barra.add_cascade(label="Facturación", menu=facturacion)

        ventanapaciente.config(menu=barra)

        ventanapaciente.mainloop()

########################################################VETANAS DEL EDITAR PACIENTE###########################################################################
    def VentanaEditarPaciente(self):
        ventanaeditarpaciente = tk.Toplevel()
        ventanaeditarpaciente.title("Editar")
        ventanaeditarpaciente.geometry("450x300")

        #ESCRIBIR ID PARA EDITAR
        ventanaeditarpaciente.lbIdPaciente = tk.Label(ventanaeditarpaciente, text="Id")
        self.idPaciente = tk.StringVar()
        ventanaeditarpaciente.entryIdPaciente = tk.Entry(ventanaeditarpaciente, textvariable=self.idPaciente, width=40)
        ventanaeditarpaciente.lbIdPaciente.grid(column=0, row=0, padx=(20, 10))
        ventanaeditarpaciente.entryIdPaciente.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))

        # ESCRIBIR NOMBRE PARA EDITAR
        ventanaeditarpaciente.lbNombrePaciente = tk.Label(ventanaeditarpaciente, text="Nombre del paciente")
        self.nuevoNombrePaciente = tk.StringVar()
        ventanaeditarpaciente.entryNuevoNombrePaciente = tk.Entry(ventanaeditarpaciente, textvariable=self.nuevoNombrePaciente, width=40)
        ventanaeditarpaciente.lbNombrePaciente.grid(column=0, row=1, padx=(20, 10))
        ventanaeditarpaciente.entryNuevoNombrePaciente.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))

        # ESCRIBIR APELLIDO PARA EDITAR
        ventanaeditarpaciente.lbApellidoPaciente = tk.Label(ventanaeditarpaciente, text="Apellido del paciente")
        self.nuevoApellidoPaciente = tk.StringVar()
        ventanaeditarpaciente.entryNuevoApellidoPaciente = tk.Entry(ventanaeditarpaciente, textvariable=self.nuevoApellidoPaciente, width=40)
        ventanaeditarpaciente.lbApellidoPaciente.grid(column=0, row=2, padx=(20, 10))
        ventanaeditarpaciente.entryNuevoApellidoPaciente.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))

        # ESCRIBIR CEDULA PARA EDITAR
        ventanaeditarpaciente.lbCedulaPaciente = tk.Label(ventanaeditarpaciente, text="Cedula")
        self.nuevaCedulaPaciente = tk.StringVar()
        ventanaeditarpaciente.entryNuevaCedulaPaciente = tk.Entry(ventanaeditarpaciente, textvariable=self.nuevaCedulaPaciente, width=40)
        ventanaeditarpaciente.lbCedulaPaciente.grid(column=0, row=3, padx=(20, 10))
        ventanaeditarpaciente.entryNuevaCedulaPaciente.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))

        # ESCRIBIR CONTRASEÑA PARA EDITAR
        ventanaeditarpaciente.lbContrasenaPaciente = tk.Label(ventanaeditarpaciente, text="Contraseña")
        self.nuevaContrasenaPaciente = tk.StringVar()
        ventanaeditarpaciente.entryNuevaContrasenaPaciente = tk.Entry(ventanaeditarpaciente, textvariable=self.nuevaContrasenaPaciente, width=40)
        ventanaeditarpaciente.lbContrasenaPaciente.grid(column=0, row=4, padx=(20, 10))
        ventanaeditarpaciente.entryNuevaContrasenaPaciente.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))

        #ESCRIBIR DIRECCION PARA EDITAR
        ventanaeditarpaciente.lbnuevaDireccion = tk.Label(ventanaeditarpaciente, text="Dirección")
        self.nuevadireccion = tk.StringVar()
        ventanaeditarpaciente.entryNuevaDireccion = tk.Entry(ventanaeditarpaciente, textvariable=self.nuevadireccion, width=40)
        ventanaeditarpaciente.lbnuevaDireccion.grid(column=0, row=5, padx=(20, 10))
        ventanaeditarpaciente.entryNuevaDireccion.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))

        # ESCRIBIR GENERO PARA EDITAR
        ventanaeditarpaciente.lbGeneroPaciente = tk.Label(ventanaeditarpaciente, text="Género")
        self.generoPaciente = tk.StringVar()
        ventanaeditarpaciente.entryGeneroPaciente = tk.Entry(ventanaeditarpaciente, textvariable=self.generoPaciente, width=40)
        ventanaeditarpaciente.lbGeneroPaciente.grid(column=0, row=6, padx=(20, 10))
        ventanaeditarpaciente.entryGeneroPaciente.grid(column=1, row=6, pady=5, columnspan=2, padx=(20, 10))

        # ESCRIBIR NACIMIENTO PARA EDITAR
        ventanaeditarpaciente.lbNacimientoPaciente = tk.Label(ventanaeditarpaciente, text="Nacimiento")
        self.nacimientoPaciente = tk.StringVar()
        ventanaeditarpaciente.entryNacimientoPaciente = tk.Entry(ventanaeditarpaciente, textvariable=self.nacimientoPaciente, width=40)
        ventanaeditarpaciente.lbNacimientoPaciente.grid(column=0, row=7, padx=(20, 10))
        ventanaeditarpaciente.entryNacimientoPaciente.grid(column=1, row=7, pady=5, columnspan=2, padx=(20, 10))

        #BOTON DE EDITAR
        ventanaeditarpaciente.btnOk = tk.Button(ventanaeditarpaciente, text="Editar",
                                                command=lambda:self.EditarPaciente(
                                                    self.idPaciente.get(),
                                                    self.nuevoNombrePaciente.get(),
                                                    self.nuevoApellidoPaciente.get(),
                                                    self.nuevaCedulaPaciente.get(),
                                                    self.nuevaContrasenaPaciente.get(),
                                                    self.nuevadireccion.get(),
                                                    self.generoPaciente.get(),
                                                    self.nacimientoPaciente.get()))
        ventanaeditarpaciente.btnOk.grid(column=0, row=8, pady=15)

        #BOTON DE SALIR
        ventanaeditarpaciente.btnSalir = tk.Button(ventanaeditarpaciente, text="Salir",
                                     command=lambda: self.CerrarVentanaPaciente(ventanaeditarpaciente.destroy()))
        ventanaeditarpaciente.btnSalir.grid(column=1, row=8, pady=15)

    def EditarPaciente(self,id, nombre, apellido, cedula,contrasena, direccion, genero, nacimiento):
        messagebox.showinfo("Editar", "Datos editados")
        CrearArchivoPaciente()
        file = open("Datos/paciente.txt", "r")
        filas = file.readlines()
        filasTemporal = []
        for fila in filas:
            paciente = fila.split(",")
            if str(paciente[0]) == id:
                filaModificada = str(id) + ","
                filaModificada = filaModificada + str(nombre) + ","
                filaModificada = filaModificada + str(apellido) + ","
                filaModificada = filaModificada + str(cedula) + ","
                filaModificada = filaModificada + str(contrasena) + ","
                filaModificada = filaModificada + str(direccion) + ","
                filaModificada = filaModificada + str(genero) + ","
                filaModificada = filaModificada + str(nacimiento)
                filaModificada = filaModificada + "\n"
                filasTemporal.append(filaModificada)
            else:
                filasTemporal.append(fila)
        file.close()
        file = open("Datos/paciente.txt", "w")
        for fila in filasTemporal:
            file.write(fila)
        file.close()

    #VENTANAS MOSTRAR PACIENTE
    def MostrarPaciente(self):
        ventanamostrarpaciente = tk.Toplevel()
        ventanamostrarpaciente.geometry("500x300")
        ventanamostrarpaciente.title("Mostrar paciente")

        ventanamostrarpaciente.lblIdPaci = tk.Label(ventanamostrarpaciente, text="Id")
        ventanamostrarpaciente.lblNomPaci = tk.Label(ventanamostrarpaciente, text="Nombre")
        ventanamostrarpaciente.lblApePaci = tk.Label(ventanamostrarpaciente, text="Apellido")
        ventanamostrarpaciente.lblCeduPaci = tk.Label(ventanamostrarpaciente, text="Número de cédula")
        ventanamostrarpaciente.lblConPaci = tk.Label(ventanamostrarpaciente, text="Contraseña")
        ventanamostrarpaciente.lblDicPaci = tk.Label(ventanamostrarpaciente, text="Dirreción")
        ventanamostrarpaciente.lblGePaci = tk.Label(ventanamostrarpaciente, text="Género")
        ventanamostrarpaciente.lblFePaci = tk.Label(ventanamostrarpaciente, text="Fecha de nacimiento")

        self.idpaci = tk.StringVar()
        ventanamostrarpaciente.txtidPaci = tk.Entry(ventanamostrarpaciente, textvariable=self.idpaci, width=40)

        self.nompaci= tk.StringVar()
        ventanamostrarpaciente.txtNompaci = tk.Entry(ventanamostrarpaciente, textvariable=self.nompaci, width=40)

        self.apepaci = tk.StringVar()
        ventanamostrarpaciente.txtApepaci = tk.Entry(ventanamostrarpaciente, textvariable=self.apepaci, width=40)

        self.cedupaci = tk.StringVar()
        ventanamostrarpaciente.txtCedupaci = tk.Entry(ventanamostrarpaciente, textvariable=self.cedupaci, width=40)

        self.conpaci = tk.StringVar()
        ventanamostrarpaciente.txtConpaci = tk.Entry(ventanamostrarpaciente, textvariable=self.conpaci, width=40)

        self.dicpaci = tk.StringVar()
        ventanamostrarpaciente.txtDicpaci = tk.Entry(ventanamostrarpaciente, textvariable=self.dicpaci, width=40)

        self.gepaci = tk.StringVar()
        ventanamostrarpaciente.txtGepaci = tk.Entry(ventanamostrarpaciente, textvariable=self.gepaci, width=40)

        self.fepaci = tk.StringVar()
        ventanamostrarpaciente.txtFepaci = tk.Entry(ventanamostrarpaciente, textvariable=self.fepaci, width=40)

        ventanamostrarpaciente.btnSalir = tk.Button(ventanamostrarpaciente, text="Salir", command=self.SalirPaciente)
        ventanamostrarpaciente.btnSiguiente = tk.Button(ventanamostrarpaciente, text="Siguiente", command=self.SiguienteRegistroPaciente)
        ventanamostrarpaciente.btnAnterior = tk.Button(ventanamostrarpaciente, text="Anterior", command=self.AnteriorRegistroPaciente)

        ventanamostrarpaciente.lblIdPaci.grid(column=0, row=0, padx=(20, 10))
        ventanamostrarpaciente.lblNomPaci.grid(column=0, row=1, padx=(20, 10))
        ventanamostrarpaciente.lblApePaci.grid(column=0, row=2, padx=(20, 10))
        ventanamostrarpaciente.lblCeduPaci.grid(column=0, row=3, padx=(20, 10))
        ventanamostrarpaciente.lblConPaci.grid(column=0, row=4, padx=(20, 10))
        ventanamostrarpaciente.lblDicPaci.grid(column=0, row=5, padx=(20, 10))
        ventanamostrarpaciente.lblGePaci.grid(column=0, row=6, padx=(20, 10))
        ventanamostrarpaciente.lblFePaci.grid(column=0, row=7, padx=(20, 10))

        ventanamostrarpaciente.txtidPaci.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventanamostrarpaciente.txtNompaci.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventanamostrarpaciente.txtApepaci.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        ventanamostrarpaciente.txtCedupaci.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        ventanamostrarpaciente.txtConpaci.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        ventanamostrarpaciente.txtDicpaci.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))
        ventanamostrarpaciente.txtGepaci.grid(column=1, row=6, pady=5, columnspan=2, padx=(20, 10))
        ventanamostrarpaciente.txtFepaci.grid(column=1, row=7, pady=5, columnspan=2, padx=(20, 10))


        ventanamostrarpaciente.btnAnterior.grid(column=0, row=8, pady=15)
        ventanamostrarpaciente.btnSiguiente.grid(column=1, row=8, pady=15)
        ventanamostrarpaciente.btnSalir.grid(column=2, row=8, pady=15)


    def VerRegistroPaciente(self):
        global registroActualPaciente
        listaPersonasPaciente = ObtenerPaciente()
        personapa = listaPersonasPaciente[registroActualPaciente]
        self.idpaci.set(personapa['Id'])
        self.nompaci.set(personapa['Nombre'])
        self.apepaci.set(personapa['Apellido'])
        self.cedupaci.set(personapa['Cedula'])
        self.conpaci.set(personapa['Contraseña'])
        self.dicpaci.set(personapa['Direccion'])
        self.gepaci.set(personapa['Genero'])
        self.fepaci.set(personapa['Nacimiento'])

    def SiguienteRegistroPaciente(self):
        global registroActualPaciente
        listaPersonasPaciente = ObtenerPaciente()
        if registroActualPaciente < len(listaPersonasPaciente)-1:
            registroActualPaciente += 1
            self.VerRegistroPaciente()

    def AnteriorRegistroPaciente(self):
        global registroActualPaciente
        listaPersonas = ObtenerPaciente()
        if registroActualPaciente > 0:
            registroActualPaciente -= 1
            self.VerRegistroPaciente()


################################################VENTANAS ELIMINAR PACIENTE#############################################################
    def VentanaEliminarPaciente(self):
        ventanaEliminarPaciente = tk.Toplevel()
        ventanaEliminarPaciente.title("Eliminar")
        ventanaEliminarPaciente.geometry("350x100")

        #CAMPO PARA INGRESAR ID
        ventanaEliminarPaciente.lbIdPaci = tk.Label(ventanaEliminarPaciente, text="Id")
        self.idPaci = tk.StringVar()
        ventanaEliminarPaciente.entryIdPaci = tk.Entry(ventanaEliminarPaciente, textvariable=self.idPaci, width=40)
        ventanaEliminarPaciente.lbIdPaci.grid(column=0, row=0, padx=(20, 10))
        ventanaEliminarPaciente.entryIdPaci.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))

        #BOTON ELIMINAR
        ventanaEliminarPaciente.btnOkPaci = tk.Button(ventanaEliminarPaciente, text="Eliminar",
                                                  command=self.EliminarPaciente)
        ventanaEliminarPaciente.btnOkPaci.grid(column=0, row=5, pady=15)

        #BOTON SALIR
        ventanaEliminarPaciente.btnSalir = tk.Button(ventanaEliminarPaciente, text="Salir",
                                      command=self.CerrarVentanaEliminar)
        ventanaEliminarPaciente.btnSalir.grid(column=1, row=5, pady=15)


    def EliminarPaciente(self):
        messagebox.showinfo("Eliminado", "Datos eliminados")
        CrearArchivoPaciente()
        file = open("Datos/paciente.txt", "r")
        filas = file.readlines()
        filasTemporal = []
        for fila in filas:
            paciente = fila.split(",")
            if paciente[0] != self.idPaci.get():
                filasTemporal.append(fila)
        file.close()
        file = open("Datos/paciente.txt", "w")
        for fila in filasTemporal:
            file.write(fila)
        file.close()

    def CerrarVentanaEliminar(self):
        MsgBox = tk.messagebox.askquestion("Salir", "¿Está seguro que desea salir?", icon="warning")
        if MsgBox == 'yes':
            root.destroy()
        else:
            tk.messagebox.showinfo("Listo!", "Se ha regresado a la pantalla principal")

#########################################################VENTANA PARA CREAR HISTORIAL PACIENTE###########################################################
    def CrearHistorialPaciente(self):
        ventanahistorialpaciente=tk.Toplevel()
        ventanahistorialpaciente.title("Crear cita")
        ventanahistorialpaciente.geometry("450x250")

        #ESTAPACIO ESCRIBIR ID
        ventanahistorialpaciente.lbIdhistorialpa = tk.Label(ventanahistorialpaciente, text="Id")
        self.idhistorialpa = tk.StringVar()
        ventanahistorialpaciente.entryIdHistorialPa = tk.Entry(ventanahistorialpaciente, textvariable=self.idhistorialpa, width=40)
        ventanahistorialpaciente.lbIdhistorialpa.grid(column=0, row=0, padx=(20, 10))
        ventanahistorialpaciente.entryIdHistorialPa.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))

        #ESPACIO ESCRIBIR FECHA
        ventanahistorialpaciente.lbFechapa = tk.Label(ventanahistorialpaciente, text="Fecha")
        self.fechapa = tk.StringVar()
        ventanahistorialpaciente.entryFechaPa = tk.Entry(ventanahistorialpaciente,
                                                               textvariable=self.fechapa, width=40)
        ventanahistorialpaciente.lbFechapa.grid(column=0, row=1, padx=(20, 10))
        ventanahistorialpaciente.entryFechaPa.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))

        # ESPACIO ESCRIBIR GENERO
        ventanahistorialpaciente.lbGenero = tk.Label(ventanahistorialpaciente, text="Genero")
        self.Genero = tk.StringVar()
        ventanahistorialpaciente.entrygenero = tk.Entry(ventanahistorialpaciente,
                                                        textvariable=self.Genero, width=40)
        ventanahistorialpaciente.lbGenero.grid(column=0, row=2, padx=(20, 10))
        ventanahistorialpaciente.entrygenero.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))

        #ESPACIO ESCRIBIR NOMBRE PACIENTE
        ventanahistorialpaciente.lbPacienten = tk.Label(ventanahistorialpaciente, text="Paciente")
        self.pacienteN = tk.StringVar()
        ventanahistorialpaciente.entryPacienteN = tk.Entry(ventanahistorialpaciente,
                                                         textvariable=self.pacienteN, width=40)
        ventanahistorialpaciente.lbPacienten.grid(column=0, row=3, padx=(20, 10))
        ventanahistorialpaciente.entryPacienteN.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))

        #ESPACIO ESCRIBIR NOMBRE MEDICO
        ventanahistorialpaciente.lbMedicon = tk.Label(ventanahistorialpaciente, text="Médico")
        self.medicoN = tk.StringVar()
        ventanahistorialpaciente.entryMedicoN = tk.Entry(ventanahistorialpaciente,
                                                           textvariable=self.medicoN, width=40)
        ventanahistorialpaciente.lbMedicon.grid(column=0, row=4, padx=(20, 10))
        ventanahistorialpaciente.entryMedicoN.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))

        #ESPACIO ESCRIBIR PARTE MEDICO
        ventanahistorialpaciente.lbPartemedico = tk.Label(ventanahistorialpaciente, text="Parte médico")
        self.parteMedicoPa = tk.StringVar()
        ventanahistorialpaciente.entryParteMedico = tk.Entry(ventanahistorialpaciente,
                                                            textvariable=self.parteMedicoPa, width=40)
        ventanahistorialpaciente.lbPartemedico.grid(column=0, row=5, padx=(20, 10))
        ventanahistorialpaciente.entryParteMedico.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))

        #BOTON DE GUARDAR HISTORIAL
        ventanahistorialpaciente.btnGuardar = tk.Button(ventanahistorialpaciente, text="Guardar",
                                                       command=lambda: self.GuardarHistorialPaciente(
                                                           self.idhistorialpa.get(),
                                                           self.fechapa.get(),
                                                           self.Genero.get(),
                                                           self.pacienteN.get(),
                                                           self.medicoN.get(),
                                                           self.parteMedicoPa.get()))
        ventanahistorialpaciente.btnGuardar.grid(column=0, row=7, pady=15)

        #BOTON DE SALIR DEL HISTORIAL
        ventanahistorialpaciente.btnSalir = tk.Button(ventanahistorialpaciente, text="Salir",
                                                     command=lambda: self.CerrarVentanaPaciente(ventanahistorialpaciente.destroy()))
        ventanahistorialpaciente.btnSalir.grid(column=1, row=7, pady=15)

    def GuardarHistorialPaciente(self,*argumentos):
        reconocimiento = Reconocimiento()
        reconocimiento.Configuracion()
        reconocimiento.Iniciar()
        parteM = reconocimiento.ReconocimientoEmociones(self.parteMedicoPa.get())
        for x in parteM:
            anger = x['faceAttributes']['emotion']['anger']
            disgust = x['faceAttributes']['emotion']['disgust']
            contempt = x['faceAttributes']['emotion']['contempt']
            sadness = x['faceAttributes']['emotion']['sadness']
            happiness = x['faceAttributes']['emotion']['happiness']
            surprise = x['faceAttributes']['emotion']['surprise']
            fear = x['faceAttributes']['emotion']['fear']
            neutral = x['faceAttributes']['emotion']['neutral']
            if anger >= 0.500 or disgust >= 0.250:
                list.append("El diagnostico es problema de tiroides.")
            if contempt >= 0.700 or sadness >= 0.100:
                list.append("El diagnostico es trombo vascular en el cerebro.")
            if disgust >= 0.500 or anger >= 0.100:
                list.append("El diagnostico es malestar estomacal.")
            if happiness >= 0.500 or surprise >= 0.250:
                list.append("El diagnostico es adiccion a las drogas.")
            if fear >= 0.400 or neutral >= 0.200:
                list.append("El diagnostico es hipertencion arterial.")
            if sadness >= 0.250 or neutral >= 0.200 or disgust >= 0.250:
                list.append("El diagnostico es tension muscular.")
            if disgust >= 0.520 or neutral >= 0.100 or sadness >= 0.400:
                list.append("El diagnostico es trastorno bipolar.")
            if disgust >= 0.200 or sadness >= 0.100 or anger >= 0.200:
                list.append("El diagnostico es depresion.")
            if happiness >= 0.250 or surprise >= 0.200 or disgust >= 0.100:
                list.append("El diagnostico es desordenes de ansiedad.")
            elif anger >= 0.250 or neutral >= 0.100 or sadness >= 0.150:
                list.append("El diagnostico es gastritis.")
            else:
                list.append("El paciente es super sano")
        messagebox.showinfo("Información", "Registro almacenado")
        CrearArchivoHistorialPaciente()
        file = open("Datos/historial_paciente.txt", "a")
        file.write(str(argumentos[0]) + ", ")
        file.write(str(argumentos[1]) + ", ")
        file.write(str(argumentos[2]) + ", ")
        file.write(str(argumentos[3]) + ", ")
        file.write(str(argumentos[4]) + ", ")
        file.write(str(list))
        file.write("\n")
        file.close()
        return {'Id Paciente': argumentos[0],
                'Fecha': argumentos[1],
                'Genero': argumentos[2],
                'paciente': argumentos[3],
                'medico': argumentos[4],
                'Parte medico': list}

    def  VentanaEmociones(self):
        ventana9= tk.Toplevel()
        ventana9.title("Emociones")
        ventana9.geometry("400x150")

        ventana9.lbID = tk.Label(ventana9, text="Id")
        ventana9.lbG = tk.Label(ventana9, text="Genero")
        ventana9.lbE = tk.Label(ventana9, text="Emociones")

        self.idemo = tk.StringVar()
        ventana9.entryID = tk.Entry(ventana9,textvariable=self.idemo, width=40)
        self.generoemo = tk.StringVar()
        ventana9.entryG = tk.Entry(ventana9, textvariable=self.generoemo, width=40)
        self.emo = tk.StringVar()
        ventana9.entryEmo = tk.Entry(ventana9, textvariable=self.emo, width=40)

        ventana9.btnGuardar = tk.Button(ventana9, text="Guardar",
                                                        command= self.GuardarEmociones)
        ventana9.btnSalir = tk.Button(ventana9, text="Salir",
                                                      command=lambda: self.CerrarVentanaPaciente(
                                                          ventana9.destroy()))
        ventana9.lbID.grid(column=0, row=0, padx=(20, 10))
        ventana9.lbG.grid(column=0, row=1, padx=(20, 10))
        ventana9.lbE.grid(column=0, row=2, padx=(20, 10))

        ventana9.entryID.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventana9.entryG.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventana9.entryEmo.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))

        ventana9.btnGuardar.grid(column=0, row=3, pady=15)
        ventana9.btnSalir.grid(column=1, row=3, pady=15)

    def GuardarEmociones(self):

        reconocimiento = Reconocimiento()
        reconocimiento.Configuracion()
        reconocimiento.Iniciar()
        emocion = reconocimiento.ReconocimientoEmociones(self.emo.get())
        for x in emocion:
            e = x['faceAttributes']['emotion']
        messagebox.showinfo("Informacion", "Emociones Guardadas")
        file = open("Datos/emociones.txt", "a")
        file.write(str(self.idemo.get()) + ",")
        file.write(str(self.generoemo.get()) + ",")
        file.write(str(e))
        file.write("\n")
        file.close()
        return {'Id': self.idemo.get(),
                'Genero': self.generoemo.get(),
                'Enfermedades': e
                }


    def ParteMedicoPaciente(self):
        ventana6 = tk.Toplevel()
        ventana6.title("Parte Médico")
        ventana6.geometry("450x150")

        ventana6.lbId = tk.Label(ventana6, text="Id")
        ventana6.lbGenero = tk.Label(ventana6, text="Genero")
        ventana6.lbImagen = tk.Label(ventana6, text="Imagen")

        self.Id = tk.StringVar()
        ventana6.entryId = tk.Entry(ventana6, textvariable=self.Id, width=40)

        self.genero = tk.StringVar()
        ventana6.entrgenero = tk.Entry(ventana6, textvariable=self.genero, width=40)

        self.Imagen = tk.StringVar()
        ventana6.entryImagen = tk.Entry(ventana6, textvariable=self.Imagen, width=40)

        # Boton Salir
        ventana6.btnSalir = tk.Button(ventana6, text="Salir",
                                                     command=lambda: self.CerrarVentanaPaciente(
                                                         ventana6.destroy()))
        # Boton Guardar
        ventana6.btnGuardar = tk.Button(ventana6, text="Guardar",
                                                       command=self.ReconocimientoEnfermedadPaciente)
        ventana6.lbId.grid(column=0, row=0, padx=(20, 10))
        ventana6.lbGenero.grid(column=0, row=1, padx=(20, 10))
        ventana6.lbImagen.grid(column=0, row=2, padx=(20, 10))

        ventana6.entryId.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventana6.entrgenero.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventana6.entryImagen.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))

        ventana6.btnGuardar.grid(column=0, row=3, pady=15)
        ventana6.btnSalir.grid(column=1, row=3, pady=15)

    def ReconocimientoEnfermedadPaciente(self):
        reconocimiento = Reconocimiento()
        reconocimiento.Configuracion()
        reconocimiento.Iniciar()
        texto = reconocimiento.ReconocimientoEmociones(self.Imagen.get())
        for x in texto:
            anger = x['faceAttributes']['emotion']['anger']
            disgust = x['faceAttributes']['emotion']['disgust']
            contempt = x['faceAttributes']['emotion']['contempt']
            sadness = x['faceAttributes']['emotion']['sadness']
            happiness = x['faceAttributes']['emotion']['happiness']
            surprise = x['faceAttributes']['emotion']['surprise']
            fear = x['faceAttributes']['emotion']['fear']
            neutral = x['faceAttributes']['emotion']['neutral']
            if anger >= 0.500 or disgust >= 0.250:
                list.append("El diagnostico es problema de tiroides.")
            if contempt >= 0.700 or sadness >= 0.100:
                list.append("El diagnostico es trombo vascular en el cerebro.")
            if disgust >= 0.500 or anger >= 0.100:
                list.append("El diagnostico es malestar estomacal.")
            if happiness >= 0.500 or surprise >= 0.250:
                list.append("El diagnostico es adiccion a las drogas.")
            if fear >= 0.400 or neutral >= 0.200:
                list.append("El diagnostico es hipertencion arterial.")
            if sadness >= 0.250 or neutral >= 0.200 or disgust >= 0.250:
                list.append("El diagnostico es tension muscular.")
            if disgust >= 0.520 or neutral >= 0.100 or sadness >= 0.400:
                list.append("El diagnostico es trastorno bipolar.")
            if disgust >= 0.200 or sadness >= 0.100 or anger >= 0.200:
                list.append("El diagnostico es depresion.")
            if happiness >= 0.250 or surprise >= 0.200 or disgust >= 0.100:
                list.append("El diagnostico es desordenes de ansiedad.")
            elif anger >= 0.250 or neutral >= 0.100 or sadness >= 0.150:
                list.append("El diagnostico es gastritis.")
            else:
                list.append("El paciente es super sano")
            file = open("Datos/parte_medico_paciente.txt", "a")
            file.write(str(self.Id.get())+ ",")
            file.write(str(self.genero.get()) + ",")
            file.write(str(list))
            file.write("\n")
            file.close()
            return {'Id':self.Id.get(),
                    'Genero': self.genero.get(),
                    'Enfermedades': list
                    }
    def ObtenerFactura(self):
        print()


######################################################REGISTRO DEL PACIENTE############################################################
    def RegistrarsePaciente(self):
        ventanaRegistroPaciente = tk.Toplevel()
        ventanaRegistroPaciente.title("Registrar Paciente")
        ventanaRegistroPaciente.geometry("450x300")

        # Ventanas de medico
        ventanaRegistroPaciente.lbidpaciente = tk.Label(ventanaRegistroPaciente, text="Id")
        ventanaRegistroPaciente.lbNombre = tk.Label(ventanaRegistroPaciente, text="Nombre del paciente")
        ventanaRegistroPaciente.lbApellido = tk.Label(ventanaRegistroPaciente, text="Apellido del paciente")
        ventanaRegistroPaciente.lbCedula = tk.Label(ventanaRegistroPaciente, text="Número de cedula")
        ventanaRegistroPaciente.lbContrasena = tk.Label(ventanaRegistroPaciente, text="Contraseña")
        ventanaRegistroPaciente.lbDireccion = tk.Label(ventanaRegistroPaciente, text="Dirección")
        ventanaRegistroPaciente.lbGenero = tk.Label(ventanaRegistroPaciente, text="Género")
        ventanaRegistroPaciente.lbNacimiento = tk.Label(ventanaRegistroPaciente, text="Fecha de nacimiento")

        # Campos para escribir
        self.idPaciente = tk.StringVar()
        ventanaRegistroPaciente.entryIdPaciente = tk.Entry(ventanaRegistroPaciente,textvariable=self.idPaciente, width=40)

        self.nombrePaciente = tk.StringVar()
        ventanaRegistroPaciente.entryNombrePaciente = tk.Entry(ventanaRegistroPaciente, textvariable=self.nombrePaciente, width=40)

        self.ApellidoPaciente = tk.StringVar()
        ventanaRegistroPaciente.entryApellidoPaciente = tk.Entry(ventanaRegistroPaciente, textvariable=self.ApellidoPaciente, width=40)

        self.Cedula = tk.StringVar()
        ventanaRegistroPaciente.entryCedula = tk.Entry(ventanaRegistroPaciente, textvariable=self.Cedula, width=40)

        self.Contrasena = tk.StringVar()
        ventanaRegistroPaciente.entryContrasena = tk.Entry(ventanaRegistroPaciente, textvariable=self.Contrasena, width=40)

        self.Direccion = tk.StringVar()
        ventanaRegistroPaciente.entryDireccion = tk.Entry(ventanaRegistroPaciente, textvariable=self.Direccion, width=40)

        self.Genero = tk.StringVar()
        ventanaRegistroPaciente.entryGenero = tk.Entry(ventanaRegistroPaciente, textvariable=self.Genero, width=40)

        self.Nacimiento = tk.StringVar()
        ventanaRegistroPaciente.entryNacimiento = tk.Entry(ventanaRegistroPaciente, textvariable=self.Nacimiento, width=40)

        # Boton Salir
        ventanaRegistroPaciente.btnSalir = tk.Button(ventanaRegistroPaciente, text="Salir",
                                      command=lambda: self.CerrarVentanaPaciente(ventanaRegistroPaciente.destroy()))
        # Boton Guardar
        ventanaRegistroPaciente.btnGuardar = tk.Button(ventanaRegistroPaciente, text="Guardar",
                                        command=lambda: self.GuardarRegistroPaciente(
                                            self.idPaciente.get(),
                                            self.nombrePaciente.get(),
                                            self.ApellidoPaciente.get(),
                                            self.Cedula.get(),
                                            self.Contrasena.get(),
                                            self.Direccion.get(),
                                            self.Genero.get(),
                                            self.Nacimiento.get()))

        ventanaRegistroPaciente.lbidpaciente.grid(column=0, row=0, padx=(20, 10))
        ventanaRegistroPaciente.lbNombre.grid(column=0, row=1, padx=(20, 10))
        ventanaRegistroPaciente.lbApellido.grid(column=0, row=2, padx=(20, 10))
        ventanaRegistroPaciente.lbCedula.grid(column=0, row=3, padx=(20, 10))
        ventanaRegistroPaciente.lbContrasena.grid(column=0, row=4, padx=(20, 10))
        ventanaRegistroPaciente.lbDireccion.grid(column=0, row=5, padx=(20, 10))
        ventanaRegistroPaciente.lbGenero.grid(column=0, row=6, padx=(20, 10))
        ventanaRegistroPaciente.lbNacimiento.grid(column=0, row=7, padx=(20, 10))

        ventanaRegistroPaciente.entryIdPaciente.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventanaRegistroPaciente.entryNombrePaciente.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventanaRegistroPaciente.entryApellidoPaciente.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        ventanaRegistroPaciente.entryCedula.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        ventanaRegistroPaciente.entryContrasena.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        ventanaRegistroPaciente.entryDireccion.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))
        ventanaRegistroPaciente.entryGenero.grid(column=1, row=6, pady=5, columnspan=2, padx=(20, 10))
        ventanaRegistroPaciente.entryNacimiento.grid(column=1, row=7, pady=5, columnspan=2, padx=(20, 10))

        ventanaRegistroPaciente.btnSalir.grid(column=1, row=8, pady=15)
        ventanaRegistroPaciente.btnGuardar.grid(column=0, row=8, pady=15)

    def CerrarVentanaPaciente(self, *argumentos):
        messagebox.showinfo("Datos Registrados", "Gracias por utilizar nuestros servicios")

    def GuardarRegistroPaciente(self, *argumentos):
        messagebox.showinfo("Información", "Registro almacenado")
        nuevoCurso = [argumentos[0], argumentos[1], argumentos[2], argumentos[3], argumentos[4], argumentos[5],
                      argumentos[6], argumentos[7]]
        CrearArchivoPaciente()
        file = open("Datos/paciente.txt", "a")
        file.write(str(argumentos[0]) + ",")
        file.write(str(argumentos[1]) + ",")
        file.write(str(argumentos[2]) + ",")
        file.write(str(argumentos[3]) + ",")
        file.write(str(argumentos[4]) + ",")
        file.write(str(argumentos[5]) + ",")
        file.write(str(argumentos[6]) + ",")
        file.write(str(argumentos[7]))
        file.write("\n")
        file.close()
        return {'Id': argumentos[0],
                'Nombre': argumentos[1],
                'Apellido': argumentos[2],
                'Cedula': argumentos[3],
                'Contraseña': argumentos[4],
                'Direccion': argumentos[5],
                'Genero': argumentos[6],
                'Nacimiento': argumentos[7]
                }

############################################---FACTURACIÓN---########################################################
    def VentanaCrearFactura(self):
        ventana5 = tk.Toplevel()
        ventana5.title("Crear Factura")
        ventana5.geometry("500x500")

        ventana5.lbIdFactura = tk.Label(ventana5, text="Id Factura")
        ventana5.lbMedico = tk.Label(ventana5, text="Id Medico")
        ventana5.lbMediconombre = tk.Label(ventana5, text="Nombre medico")
        ventana5.lbPaciente = tk.Label(ventana5, text="Id Paciente")
        ventana5.lbPacientenombre = tk.Label(ventana5, text="Nombre paciente")
        ventana5.lbFecha = tk.Label(ventana5, text="Fecha")
        ventana5.lbEstado = tk.Label(ventana5, text="Estado")
        ventana5.lbMonto = tk.Label(ventana5, text="Monto")
        ventana5.lbMinutos = tk.Label(ventana5, text="Cantidad de minutos")
        ventana5.lbSalarioHora = tk.Label(ventana5, text="Salario hora")
        ventana5.lbSubFactura = tk.Label(ventana5, text="Subtotal factura")
        ventana5.lbtotalFactura = tk.Label(ventana5, text="Total factura")
        ventana5.lbImpuesto = tk.Label(ventana5, text="Impuesto")
        ventana5.lbtotalImpuesto = tk.Label(ventana5, text="Total impuesto")
        ventana5.lbenfermedades = tk.Label(ventana5, text="Enfermedades")

        self.idFactura = tk.StringVar()
        ventana5.entryIdFactura = tk.Entry(ventana5, textvariable=self.idFactura, width=40)

        self.idMedico = tk.StringVar()
        ventana5.entryIdmedico = tk.Entry(ventana5, textvariable=self.idMedico, width=40)

        self.nombreMedico = tk.StringVar()
        ventana5.entrynombremedico = tk.Entry(ventana5, textvariable=self.nombreMedico, width=40)

        self.idPaciente = tk.StringVar()
        ventana5.entryidpaciente = tk.Entry(ventana5, textvariable=self.idPaciente, width=40)

        self.nombrePaciente = tk.StringVar()
        ventana5.entrynombrepaciente = tk.Entry(ventana5, textvariable=self.nombrePaciente, width=40)

        self.fecha = tk.StringVar()
        ventana5.entryfecha = tk.Entry(ventana5, textvariable=self.fecha, width=40)

        self.estado = tk.StringVar()
        ventana5.entryestado = tk.Entry(ventana5, textvariable=self.estado, width=40)

        self.monto = tk.StringVar()
        ventana5.entrymonto = tk.Entry(ventana5, textvariable=self.monto, width=40)

        self.minutos = tk.StringVar()
        ventana5.entryminutos = tk.Entry(ventana5, textvariable=self.minutos, width=40)

        self.salarioHora = tk.StringVar()
        ventana5.entrysalarioHora = tk.Entry(ventana5, textvariable=self.salarioHora, width=40)

        self.subTotalFactura = tk.StringVar()
        ventana5.entrysubtotalfactura = tk.Entry(ventana5, textvariable=self.subTotalFactura, width=40)

        self.totalFactura = tk.StringVar()
        ventana5.entrytotalfactura = tk.Entry(ventana5, textvariable=self.totalFactura, width=40)

        self.impuesto = tk.StringVar()
        ventana5.entryimpuesto = tk.Entry(ventana5, textvariable=self.impuesto, width=40)

        self.totalImpuesto = tk.StringVar()
        ventana5.entrytotalImpuesto = tk.Entry(ventana5, textvariable=self.totalImpuesto, width=40)

        self.enfermedades = tk.StringVar()
        ventana5.entryenfermedades = tk.Entry(ventana5, textvariable=self.enfermedades, width=40)

        # Boton Salir
        ventana5.btnSalir = tk.Button(ventana5, text="Salir",
                                      command=lambda: self.CerrarVentanaPaciente(ventana5.destroy()))
        # Boton Guardar

        ventana5.btnGuardar = tk.Button(ventana5, text="Guardar",
                                        command=self.GuardarFactura)

        ventana5.lbIdFactura.grid(column=0, row=0, padx=(20, 10))
        ventana5.lbMedico.grid(column=0, row=1, padx=(20, 10))
        ventana5.lbMediconombre.grid(column=0, row=2, padx=(20, 10))
        ventana5.lbPaciente.grid(column=0, row=3, padx=(20, 10))
        ventana5.lbPacientenombre.grid(column=0, row=4, padx=(20, 10))
        ventana5.lbFecha.grid(column=0, row=5, padx=(20, 10))
        ventana5.lbEstado.grid(column=0, row=6, padx=(20, 10))
        ventana5.lbMonto.grid(column=0, row=7, padx=(20, 10))
        ventana5.lbMinutos.grid(column=0, row=8, padx=(20, 10))
        ventana5.lbSalarioHora.grid(column=0, row=9, padx=(20, 10))
        ventana5.lbSubFactura.grid(column=0, row=10, padx=(20, 10))
        ventana5.lbtotalFactura.grid(column=0, row=11, padx=(20, 10))
        ventana5.lbImpuesto.grid(column=0, row=12, padx=(20, 10))
        ventana5.lbtotalImpuesto.grid(column=0, row=13, padx=(20, 10))
        ventana5.lbenfermedades.grid(column=0, row=14, padx=(20, 10))

        ventana5.entryIdFactura.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entryIdmedico.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entrynombremedico.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entryidpaciente.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entrynombrepaciente.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entryfecha.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entryestado.grid(column=1, row=6, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entrymonto.grid(column=1, row=7, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entryminutos.grid(column=1, row=8, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entrysalarioHora.grid(column=1, row=9, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entrysubtotalfactura.grid(column=1, row=10, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entrytotalfactura.grid(column=1, row=11, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entryimpuesto.grid(column=1, row=12, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entrytotalImpuesto.grid(column=1, row=13, pady=5, columnspan=2, padx=(20, 10))
        ventana5.entryenfermedades.grid(column=1, row=14, pady=5, columnspan=2, padx=(20, 10))

        ventana5.btnSalir.grid(column=1, row=15, pady=15)
        ventana5.btnGuardar.grid(column=0, row=15, pady=15)

    def GuardarFactura(self):
        reconocimiento = Reconocimiento()
        reconocimiento.Configuracion()
        reconocimiento.Iniciar()
        texto2 = reconocimiento.ReconocimientoEmociones(self.enfermedades.get())
        for x in texto2:
            anger = x['faceAttributes']['emotion']['anger']
            disgust = x['faceAttributes']['emotion']['disgust']
            contempt = x['faceAttributes']['emotion']['contempt']
            sadness = x['faceAttributes']['emotion']['sadness']
            happiness = x['faceAttributes']['emotion']['happiness']
            surprise = x['faceAttributes']['emotion']['surprise']
            fear = x['faceAttributes']['emotion']['fear']
            neutral = x['faceAttributes']['emotion']['neutral']
            if anger >= 0.500 or disgust >= 0.250:
                list.append("El diagnostico es problema de tiroides.")
            if contempt >= 0.700 or sadness >= 0.100:
                list.append("El diagnostico es trombo vascular en el cerebro.")
            if disgust >= 0.500 or anger >= 0.100:
                list.append("El diagnostico es malestar estomacal.")
            if happiness >= 0.500 or surprise >= 0.250:
                list.append("El diagnostico es adiccion a las drogas.")
            if fear >= 0.400 or neutral >= 0.200:
                list.append("El diagnostico es hipertencion arterial.")
            if sadness >= 0.250 or neutral >= 0.200 or disgust >= 0.250:
                list.append("El diagnostico es tension muscular.")
            if disgust >= 0.520 or neutral >= 0.100 or sadness >= 0.400:
                list.append("El diagnostico es trastorno bipolar.")
            if disgust >= 0.200 or sadness >= 0.100 or anger >= 0.200:
                list.append("El diagnostico es depresion.")
            if happiness >= 0.250 or surprise >= 0.200 or disgust >= 0.100:
                list.append("El diagnostico es desordenes de ansiedad.")
            elif anger >= 0.250 or neutral >= 0.100 or sadness >= 0.150:
                list.append("El diagnostico es gastritis.")
            else:
                list.append("El paciente es super sano")
        messagebox.showinfo("Información", "Registro almacenado")
        self.tx = ManejoFacturas(self.idFactura.get(), self.idMedico.get(), self.nombreMedico.get(), self.idPaciente.get(),
                                 self.nombrePaciente.get(), self.fecha.get(), self.estado.get(),
                                 self.monto.get(), self.minutos.get(), self.salarioHora.get(), self.totalFactura.get(),
                                 self.subTotalFactura.get(), self.impuesto.get(), self.totalImpuesto.get(),
                                 list, "", "","")
        self.tx.AgregarFactura(self.idFactura.get(), self.idMedico.get(), self.nombreMedico.get(), self.idPaciente.get(),
                                 self.nombrePaciente.get(), self.fecha.get(), self.estado.get(),
                                 self.monto.get(), self.minutos.get(), self.salarioHora.get(), self.totalFactura.get(),
                                 self.subTotalFactura.get(), self.impuesto.get(), self.totalImpuesto.get(),
                                 list)

    def VentanaObtenerFactura(self):
        ventanaObtener = tk.Toplevel()
        ventanaObtener.title("Obtener Factura")
        ventanaObtener.geometry("500x500")
        ventanaObtener.lbfacturaid = tk.Label(ventanaObtener, text="Id Factura")
        ventanaObtener.lbmedico = tk.Label(ventanaObtener, text="Id Medico")
        ventanaObtener.lbnombremedico = tk.Label(ventanaObtener, text="Nombre medico")
        ventanaObtener.lbpaciente = tk.Label(ventanaObtener, text="Id Paciente")
        ventanaObtener.lbnombrepaciente = tk.Label(ventanaObtener, text="Nombre paciente")
        ventanaObtener.lbfecha = tk.Label(ventanaObtener, text="Fecha")
        ventanaObtener.lbestado = tk.Label(ventanaObtener, text="Estado")
        ventanaObtener.lbmonto = tk.Label(ventanaObtener, text="Monto")
        ventanaObtener.lbminutos = tk.Label(ventanaObtener, text="Cantidad de minutos")
        ventanaObtener.lbsalariohora = tk.Label(ventanaObtener, text="Salario hora")
        ventanaObtener.lbsubtotalfactura = tk.Label(ventanaObtener, text="Subtotal factura")
        ventanaObtener.lbtotalfactura = tk.Label(ventanaObtener, text="Total factura")
        ventanaObtener.lbimpuesto = tk.Label(ventanaObtener, text="Impuesto")
        ventanaObtener.lbtotalimpuesto = tk.Label(ventanaObtener, text="Total impuesto")
        ventanaObtener.lbenfermedad= tk.Label(ventanaObtener, text="Enfermedades")

        self.Facturaid= tk.StringVar()
        ventanaObtener.entryFacturaId = tk.Entry(ventanaObtener, textvariable=self.Facturaid, width=40)

        self.medicoid = tk.StringVar()
        ventanaObtener.entrymedicoid = tk.Entry(ventanaObtener, textvariable=self.medicoid, width=40)

        self.mediconombre = tk.StringVar()
        ventanaObtener.entrymedicoNombre = tk.Entry(ventanaObtener, textvariable=self.mediconombre, width=40)

        self.pacienteid = tk.StringVar()
        ventanaObtener.entrypacienteid = tk.Entry(ventanaObtener, textvariable=self.pacienteid, width=40)

        self.pacientenombre = tk.StringVar()
        ventanaObtener.entrypacientenombre = tk.Entry(ventanaObtener, textvariable=self.pacientenombre, width=40)

        self.Fecha = tk.StringVar()
        ventanaObtener.entryFech = tk.Entry(ventanaObtener, textvariable=self.Fecha, width=40)

        self.Estado = tk.StringVar()
        ventanaObtener.entryEstado = tk.Entry(ventanaObtener, textvariable=self.Estado, width=40)

        self.Monto = tk.StringVar()
        ventanaObtener.entryMonto = tk.Entry(ventanaObtener, textvariable=self.Monto, width=40)

        self.Minutos = tk.StringVar()
        ventanaObtener.entryMinutos= tk.Entry(ventanaObtener, textvariable=self.Minutos, width=40)

        self.SalarioHora = tk.StringVar()
        ventanaObtener.entrySalarioHora = tk.Entry(ventanaObtener, textvariable=self.SalarioHora, width=40)

        self.SubTotalFactura = tk.StringVar()
        ventanaObtener.entrySubTotalFactura = tk.Entry(ventanaObtener, textvariable=self.SubTotalFactura, width=40)

        self.TotalFacturA = tk.StringVar()
        ventanaObtener.entryTotalFacturA = tk.Entry(ventanaObtener, textvariable=self.TotalFacturA, width=40)

        self.Impuesto = tk.StringVar()
        ventanaObtener.entryimpuesto = tk.Entry(ventanaObtener, textvariable=self.Impuesto, width=40)

        self.TotalImpuesto = tk.StringVar()
        ventanaObtener.entrytotalImpuesto = tk.Entry(ventanaObtener, textvariable=self.TotalImpuesto, width=40)

        self.Enfermedades = tk.StringVar()
        ventanaObtener.entryenfermedades = tk.Entry(ventanaObtener, textvariable=self.Enfermedades, width=40)

        # Boton Salir

        ventanaObtener.btnSalirFac = tk.Button(ventanaObtener, text="Salir", command=self.SalirPaciente)
        ventanaObtener.btnSiguienteFac = tk.Button(ventanaObtener, text="Siguiente", command=self.SiguienteRegistroFactura)
        ventanaObtener.btnAnteriorFac = tk.Button(ventanaObtener, text="Anterior", command=self.AnteriorRegistroFactura)

        ventanaObtener.btnAnteriorFac.grid(column=0, row=15, pady=15)
        ventanaObtener.btnSiguienteFac.grid(column=1, row=15, pady=15)
        ventanaObtener.btnSalirFac.grid(column=2, row=15, pady=15)

        ventanaObtener.lbfacturaid.grid(column=0, row=0, padx=(20, 10))
        ventanaObtener.lbmedico.grid(column=0, row=1, padx=(20, 10))
        ventanaObtener.lbnombremedico.grid(column=0, row=2, padx=(20, 10))
        ventanaObtener.lbpaciente.grid(column=0, row=3, padx=(20, 10))
        ventanaObtener.lbnombrepaciente.grid(column=0, row=4, padx=(20, 10))
        ventanaObtener.lbfecha.grid(column=0, row=5, padx=(20, 10))
        ventanaObtener.lbestado.grid(column=0, row=6, padx=(20, 10))
        ventanaObtener.lbmonto.grid(column=0, row=7, padx=(20, 10))
        ventanaObtener.lbminutos.grid(column=0, row=8, padx=(20, 10))
        ventanaObtener.lbsalariohora.grid(column=0, row=9, padx=(20, 10))
        ventanaObtener.lbsubtotalfactura.grid(column=0, row=10, padx=(20, 10))
        ventanaObtener.lbtotalfactura.grid(column=0, row=11, padx=(20, 10))
        ventanaObtener.lbimpuesto.grid(column=0, row=12, padx=(20, 10))
        ventanaObtener.lbtotalimpuesto.grid(column=0, row=13, padx=(20, 10))
        ventanaObtener.lbenfermedad.grid(column=0, row=14, padx=(20, 10))

        ventanaObtener.entryFacturaId.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entrymedicoid.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entrymedicoNombre.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entrypacienteid.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entrypacientenombre.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entryFech.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entryEstado.grid(column=1, row=6, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entryMonto.grid(column=1, row=7, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entryMinutos.grid(column=1, row=8, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entrySalarioHora.grid(column=1, row=9, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entrySubTotalFactura.grid(column=1, row=10, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entryTotalFacturA.grid(column=1, row=11, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entryimpuesto.grid(column=1, row=12, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entrytotalImpuesto.grid(column=1, row=13, pady=5, columnspan=2, padx=(20, 10))
        ventanaObtener.entryenfermedades.grid(column=1, row=14, pady=5, columnspan=2, padx=(20, 10))


    def SiguienteRegistroFactura(self):
        global registroActualFactura
        listaPersonasfactura = ObtenerFactura()
        for x in listaPersonasfactura:
           if registroActualFactura > len(x):
               self.Facturaid.set(x['Id'])
               self.medicoid.set(x['Nombre medico'])
               self.mediconombre.set(x['Nombre medico'])
               self.pacienteid.set(x['Id paciente'])
               self.pacientenombre.set(x['Nombre paciente'])
               self.Fecha.set(x['Fecha'])
               self.Estado.set(x['Estado'])
               self.Monto.set(x['Monto'])
               self.Minutos.set(x['Minutos'])
               self.SalarioHora.set(x['Salario'])
               self.SubTotalFactura.set(x['Sub total factura'])
               self.TotalFacturA.set(x['Total factura'])
               self.Impuesto.set(x['Impuesto'])
               self.TotalImpuesto.set(x['Total impuesto'])
               self.Enfermedades.set(x['Enfermedades'])

    def AnteriorRegistroFactura(self):
        global registroActualFactura
        listaPersonasfactura = ObtenerFactura()
        for x in listaPersonasfactura:
            if registroActualFactura < len(x) - 1:
                self.Facturaid.set(x['Id'])
                self.medicoid.set(x['Nombre medico'])
                self.mediconombre.set(x['Nombre medico'])
                self.pacienteid.set(x['Id paciente'])
                self.pacientenombre.set(x['Nombre paciente'])
                self.Fecha.set(x['Fecha'])
                self.Estado.set(x['Estado'])
                self.Monto.set(x['Monto'])
                self.Minutos.set(x['Minutos'])
                self.SalarioHora.set(x['Salario'])
                self.SubTotalFactura.set(x['Sub total factura'])
                self.TotalFacturA.set(x['Total factura'])
                self.Impuesto.set(x['Impuesto'])
                self.TotalImpuesto.set(x['Total impuesto'])
                self.Enfermedades.set(x['Enfermedades'])
            registroActualFactura -= 1
####################################################
    def CambiarEstatusFactura(self):
        print("No se logro. :(")
###################################################ESTADISTICAS#########################################################
    def VentanaObtenerEstadistica(self):
        ventana7= tk.Toplevel()
        ventana7.title("Estadisticas.")
        ventana7.geometry("600x300")

        ventana7.lbpacientesA = tk.Label(ventana7, text="Total de pacientes atendidos")
        ventana7.lbenfermedadesA = tk.Label(ventana7, text="Total de enfermedades atendidas en el hospita")
        ventana7.lbenfermedadesSexo = tk.Label(ventana7, text="Total de enfermedades por sexo")
        ventana7.lbsentimientosP = tk.Label(ventana7, text="Desglose de los sentimientos más presentes")
        ventana7.lbparteMedicoSana = tk.Label(ventana7, text="Parte médico “sin problemas” es mayor a los diagnósticos “con enfermedades")
        ventana7.btnObtener1 = tk.Button(ventana7, text="Obtener",
                                      command=self.VentanaPacientesAtendidos)
        ventana7.btnObtener2 = tk.Button(ventana7, text="Obtener",
                                      command= self.VentanaEnfermedadessAtendidas)
        ventana7.btnObtener3= tk.Button(ventana7, text="Obtener",
                                      command=self.VentanaEnfermosGenero)
        ventana7.btnObtener4 = tk.Button(ventana7, text="Obtener",
                                      command=self.VentanaSentimientosPresente)
        ventana7.btnObtener5 = tk.Button(ventana7, text="Obtener",
                                      command=self.VentanaPersonasSanas)

        ventana7.lbpacientesA.grid(column=0, row=0, padx=(20, 10))
        ventana7.lbenfermedadesA.grid(column=0, row=1, padx=(20, 10))
        ventana7.lbenfermedadesSexo.grid(column=0, row=2, padx=(20, 10))
        ventana7.lbsentimientosP.grid(column=0, row=3, padx=(20, 10))
        ventana7.lbparteMedicoSana.grid(column=0, row=4, padx=(20, 10))

        ventana7.btnObtener1.grid(column=1, row=0, pady=15)
        ventana7.btnObtener2.grid(column=1, row=1, pady=15)
        ventana7.btnObtener3.grid(column=1, row=2, pady=15)
        ventana7.btnObtener4.grid(column=1, row=3, pady=15)
        ventana7.btnObtener5.grid(column=1, row=4, pady=15)


        ventana7.mainloop()

    def VentanaPacientesAtendidos(self):
        ventanaPaciente = tk.Toplevel()
        ventanaPaciente.title("Pacientes Atendidos")

        ventanaPaciente.lbPaciente = tk.Label(ventanaPaciente, text="Total pacientes Atendidos es: ")

        ventanaPaciente.btnMostrar = tk.Button(ventanaPaciente, text="Mostrar",
                                               command=lambda: self.ImprimirTotalPacientesAtendidos())

        ventanaPaciente.btnSalir = tk.Button(ventanaPaciente, text="Salir",
                                             command=lambda: self.CerrarVentana(ventanaPaciente.destroy()))

        self.TotalPacientes = tk.StringVar()
        ventanaPaciente.entryPacientes = tk.Entry(ventanaPaciente, textvariable=self.TotalPacientes, width=40)

        ventanaPaciente.lbPaciente.grid(column=0, row=0, padx=(20, 10))
        ventanaPaciente.entryPacientes.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))

        ventanaPaciente.btnMostrar.grid(column=1, row=2, pady=15)
        ventanaPaciente.btnSalir.grid(column=0, row=2, pady=15)

    def ImprimirTotalPacientesAtendidos(self):
        file = open("Datos/paciente.txt", "r")
        filas = file.readlines()
        listaIds = []
        for fila in filas:
            paciente = fila.split(",")
            listaIds.append(paciente[0])
        total = listaIds[-1]
        self.TotalPacientes.set(total)

    def CerrarVentana(self, *argumentos):
        messagebox.showinfo("Datos Registrados", "Gracias por utilizar nuestros servicios")

    def VentanaEnfermedadessAtendidas(self):
        ventanaPaciente = tk.Toplevel()
        ventanaPaciente.title("Enfermedades Atendidas")

        ventanaPaciente.lbPaciente = tk.Label(ventanaPaciente, text="Total enfermedades atendidas es: ")

        ventanaPaciente.btnMostrar = tk.Button(ventanaPaciente, text="Mostrar",
                                               command=lambda: self.ImprimirTotalPacientesAtendidos())

        ventanaPaciente.btnSalir = tk.Button(ventanaPaciente, text="Salir",
                                             command=lambda: self.CerrarVentana(ventanaPaciente.destroy()))

        self.TotalPacientes = tk.StringVar()
        ventanaPaciente.entryPacientes = tk.Entry(ventanaPaciente, textvariable=self.TotalPacientes, width=40)

        ventanaPaciente.lbPaciente.grid(column=0, row=0, padx=(20, 10))
        ventanaPaciente.entryPacientes.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))

        ventanaPaciente.btnMostrar.grid(column=1, row=2, pady=15)
        ventanaPaciente.btnSalir.grid(column=0, row=2, pady=15)

    def ImprimirTotalEnfermedades(self):
        file = open("Datos/parte_medico.txt", "r")
        filas = file.readlines()
        listaIds = []
        for fila in filas:
            paciente = fila.split(",")
            listaIds.append(paciente[0])
        total = listaIds[-1]
        self.TotalPacientes.set(total)


    def VentanaEnfermosGenero(self):
        ventanaGenero= tk.Toplevel()
        ventanaGenero.title("Enfermedades por genero")
        ventanaGenero.geometry("400x120")

        ventanaGenero.mujer = tk.Label(ventanaGenero, text="Mujer")
        ventanaGenero.hombre= tk.Label(ventanaGenero, text="Hombre")

        self.Mujer= tk.StringVar()
        ventanaGenero.entrymujer= tk.Entry(ventanaGenero, textvariable=self.Mujer, width=40)

        self.Hombre = tk.StringVar()
        ventanaGenero.entryhombre = tk.Entry(ventanaGenero, textvariable=self.Hombre, width=40)

        ventanaGenero.mujer.grid(column=0, row=0, padx=(20, 10))
        ventanaGenero.hombre.grid(column=0, row=1, padx=(20, 10))

        ventanaGenero.entrymujer.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventanaGenero.entryhombre.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))

        ventanaGenero.btnMostrar = tk.Button(ventanaGenero, text="Mostrar",
                                               command=lambda: self.ImprimirGenero())

        ventanaGenero.btnSalir = tk.Button(ventanaGenero, text="Salir",
                                             command=lambda: self.CerrarVentana(ventanaGenero.destroy()))

        ventanaGenero.btnMostrar.grid(column=1, row=2, pady=15)
        ventanaGenero.btnSalir.grid(column=0, row=2, pady=15)

    def ImprimirGenero(self):
        lista1 = ObtenerParteMedicoPaciente()
        hombre = 0
        mujer = 0
        for x in lista1:
            genero = x['Genero']
            if genero == "F" or genero == "f":
                mujer += 1
            if genero == "M" or genero == "m":
                hombre += 1
        self.Mujer.set(hombre)
        self.Hombre.set(mujer)

    def VentanaSentimientosPresente(self):
        ventana11= tk.Toplevel()
        ventana11.title("Sentimientos presentes")
        ventana11.geometry("400x300")

        ventana11.lbSentimiento = tk.Label(ventana11, text="Sentimiento")
        ventana11.lbSentimiento1 = tk.Label(ventana11, text="Sentimiento")
        ventana11.lbSentimiento2= tk.Label(ventana11, text="Sentimiento")
        ventana11.lbSentimiento3 = tk.Label(ventana11, text="Sentimiento")
        ventana11.lbSentimiento4 = tk.Label(ventana11, text="Sentimiento")
        ventana11.lbSentimiento5 = tk.Label(ventana11, text="Sentimiento")
        ventana11.lbSentimiento6= tk.Label(ventana11, text="Sentimiento")
        ventana11.lbSentimiento7 = tk.Label(ventana11, text="Sentimiento")


        self.sentimiento = tk.StringVar()
        ventana11.entrySentimiento = tk.Entry(ventana11, textvariable=self.sentimiento, width=20)
        self.sentimiento1 = tk.StringVar()
        ventana11.entrySentimiento1 = tk.Entry(ventana11, textvariable=self.sentimiento1, width=20)
        self.sentimiento2 = tk.StringVar()
        ventana11.entrySentimiento2 = tk.Entry(ventana11, textvariable=self.sentimiento2, width=20)
        self.sentimiento3 = tk.StringVar()
        ventana11.entrySentimiento3 = tk.Entry(ventana11, textvariable=self.sentimiento3, width=20)
        self.sentimiento4 = tk.StringVar()
        ventana11.entrySentimiento4 = tk.Entry(ventana11, textvariable=self.sentimiento4, width=20)
        self.sentimiento5 = tk.StringVar()
        ventana11.entrySentimiento5 = tk.Entry(ventana11, textvariable=self.sentimiento5, width=20)
        self.sentimiento6 = tk.StringVar()
        ventana11.entrySentimiento6 = tk.Entry(ventana11, textvariable=self.sentimiento6, width=20)
        self.sentimiento7 = tk.StringVar()
        ventana11.entrySentimiento7 = tk.Entry(ventana11, textvariable=self.sentimiento7, width=20)

        ventana11.lbSentimiento.grid(column=0, row=0, padx=(20, 10))
        ventana11.lbSentimiento1.grid(column=0, row=1, padx=(20, 10))
        ventana11.lbSentimiento2.grid(column=0, row=2, padx=(20, 10))
        ventana11.lbSentimiento3.grid(column=0, row=3, padx=(20, 10))
        ventana11.lbSentimiento4.grid(column=0, row=4, padx=(20, 10))
        ventana11.lbSentimiento5.grid(column=0, row=5, padx=(20, 10))
        ventana11.lbSentimiento6.grid(column=0, row=6, padx=(20, 10))
        ventana11.lbSentimiento7.grid(column=0, row=7, padx=(20, 10))

        ventana11.entrySentimiento.grid(column=1, row=0, padx=(20, 10))
        ventana11.entrySentimiento1.grid(column=1, row=1, padx=(20, 10))
        ventana11.entrySentimiento2.grid(column=1, row=2, padx=(20, 10))
        ventana11.entrySentimiento3.grid(column=1, row=3, padx=(20, 10))
        ventana11.entrySentimiento4.grid(column=1, row=4, padx=(20, 10))
        ventana11.entrySentimiento5.grid(column=1, row=5, padx=(20, 10))
        ventana11.entrySentimiento6.grid(column=1, row=6, padx=(20, 10))
        ventana11.entrySentimiento7.grid(column=1, row=7, padx=(20, 10))

        ventana11.btnMostrar = tk.Button(ventana11, text="Mostrar",
                                             command=lambda: self.ImprimirSentimientosMasPresentes)

        ventana11.btnSalir = tk.Button(ventana11, text="Salir",
                                           command=lambda: self.CerrarVentana(ventana11.destroy()))

        ventana11.btnMostrar.grid(column=1, row=8, pady=15)
        ventana11.btnSalir.grid(column=0, row=8, pady=15)

    def ImprimirSentimientosMasPresentes(self):
        lista14= ObtenerEmociones()
        emo1=0
        emo2=0
        emo3=0
        emo4=0
        emo5=0
        emo6=0
        emo7=0
        emo8=0
        for x in lista14:
            emocion = x['Emociones']['anger']
            emocion1 = x['Emociones']['contempt']
            emocion2 = x['Emociones']['disgust']
            emocion3 = x['Emociones']['fear']
            emocion4 = x['Emociones']['happiness']
            emocion5 = x['Emociones']['neutral']
            emocion6 = x['Emociones']['sadness']
            emocion7 = x['Emociones']['surprise']

            if emocion > 0:
                emo1=emo1+1
                self.sentimiento.set(emo1)
            if emocion1 < 0:
                emo2=emo2+1
                self.sentimiento1.set(emo2)
            if emocion2 > 0:
                emo3=emo3+1
                self.sentimiento2.set(emo3)
            if emocion3 > 0:
                emo4=emo4+1
                self.sentimiento3.set(emo4)
            if emocion4 > 0:
                emo5=emo5+1
                self.sentimiento4.set(emo5)
            if emocion5 > 0:
                emo6=emo6+1
                self.sentimiento5.set(emo6)
            if emocion6>0:
                emo7=emo7+1
                self.sentimiento6.set(emo7)
            if emocion7 >0:
                emo8=emo8+1
                self.sentimiento7.set(emo8)
    def ImprimirSentimientosMasPresentes2(self):
        lista = ObtenerEmociones()
        sentimientos = []
        for x in lista:
            emocion = x['Emociones']['anger']
            emocion1 = x['Emociones']['contempt']
            emocion2 = x['Emociones']['disgust']
            emocion3 = x['Emociones']['fear']
            emocion4 = x['Emociones']['happiness']
            emocion5 = x['Emociones']['neutral']
            emocion6 = x['Emociones']['sadness']
            emocion7 = x['Emociones']['surprise']
            listaContador = [0, 0, 0, 0, 0, 0, 0, 0]

        for x in sentimientos:
            for y in x.keys():
                if float(x[emocion]) > 0 and y == "anger":
                    listaContador[0] = listaContador[0] + 1

                elif float(x[emocion1]) > 0 and y == "contempt":
                    listaContador[1] = listaContador[1] + 1

                elif float(x[emocion2]) > 0 and y == "disgust":
                    listaContador[2] = listaContador[2] + 1

                elif float(x[emocion3]) > 0 and y == "fear":
                    listaContador[3] = listaContador[3] + 1

                elif float(x[emocion4]) > 0 and y == "happiness":
                    listaContador[4] = listaContador[4] + 1

                elif float(x[emocion5]) > 0 and y == "neutral":
                    listaContador[5] = listaContador[5] + 1

                elif float(x[emocion6]) > 0 and y == "sadness":
                    listaContador[6] = listaContador[6] + 1

                elif float(x[emocion7]) > 0 and y == "surprise":
                    listaContador[7] = listaContador[7] + 1

            print(listaContador)
            mayor = max(listaContador)
            indice = listaContador.index(mayor)
            if indice == 0:
                emocion = "Anger" + str(mayor).replace("{}", "")
                self.sentimiento.set(emocion)
            elif indice == 1:
                emocion1 = "Contempt" + str(mayor).replace("{}", "")
                self.sentimiento.set(emocion1)
            elif indice == 2:
                emocion2 = "Disgust" + str(mayor).replace("{}", "")
                self.sentimiento.set(emocion2)
            elif indice == 3:
                emocion3 = "Fear" + str(mayor).replace("{}", "")
                self.sentimiento.set(emocion3)
            elif indice == 4:
                emocion4 = "Happiness" + str(mayor).replace("{}", "")
                self.sentimiento.set(emocion4)
            elif indice == 5:
                emocion5 = "Neutral" + str(mayor).replace("{}", "")
                self.sentimiento.set(emocion5)
            elif indice == 6:
                emocion6 = "Sadness" + str(mayor).replace("{}", "")
                self.sentimiento.set(emocion6)
            elif indice == 7:
                emocion7 = "Surprise" + str(mayor).replace("{}", "")
                self.sentimiento.set(emocion7)

    def VentanaPersonasSanas(self):
        ventana12= tk.Toplevel()
        ventana12.title("Pacientes Sanos")
        ventana12.geometry("350x120")

        ventana12.personaSana = tk.Label(ventana12, text="Personas Sanas")
        ventana12.personaEnferma =tk.Label(ventana12, text="Personas Enfermas")

        self.personaSana = tk.StringVar()
        ventana12.entrypersonaSana = tk.Entry(ventana12, textvariable=self.personaSana, width=30)

        self.personaEnferma = tk.StringVar()
        ventana12.entrypersonaEnferma = tk.Entry(ventana12, textvariable=self.personaEnferma, width=30)

        ventana12.personaSana.grid(column=0, row=0, padx=(20, 10))
        ventana12.personaEnferma.grid(column=0, row=1, padx=(20, 10))

        ventana12.entrypersonaSana.grid(column=1, row=0, padx=(20, 10))
        ventana12.entrypersonaEnferma.grid(column=1, row=1, padx=(20, 10))

        ventana12.btnMostrar = tk.Button(ventana12, text="Mostrar",
                                         command= self.ImprimirPersonaSana)

        ventana12.btnSalir = tk.Button(ventana12, text="Salir",
                                       command=lambda: self.CerrarVentana(ventana12.destroy()))

        ventana12.btnMostrar.grid(column=0, row=2, pady=15)
        ventana12.btnSalir.grid(column=1, row=2, pady=15)
        ventana12.mainloop()

    def ImprimirPersonaSana(self):
        lista12 = ObtenerParteMedicoPaciente()
        sana = 0
        enferma = 0
        for x in lista12:
            enfermedad = x['Enfermedades']
            if enfermedad == "El paciente es super sano":
                sana = sana + 1
                self.personaSana.set(sana)
            else:
                enferma = enferma + 1
                self.personaEnferma.set(enferma)



    def CerrarVentana(self, *argumentos):
        messagebox.showinfo("Datos Registrados", "Gracias por utilizar nuestros servicios")





if __name__ == "__main__":
    root = tk.Tk()
    root.title("Inicio de Sesión")
    main = registro(root)
    registroActualPaciente = 0
    registroActualMedico = 0
    registroActualFactura = 0
    registroActualHistorialMedico = 0
    registroActualHistorialPaciente = 0
    listaFactura=[]
    list=[]
    root.mainloop()