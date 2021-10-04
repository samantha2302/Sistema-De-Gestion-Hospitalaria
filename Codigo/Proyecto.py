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
'''

# Imports
import os
import sys
import requests
import json
import cognitive_face as CF
from PIL import Image, ImageDraw, ImageFont

from tkinter import *
import tkinter as tk
from PIL import ImageTk
from PIL import Image
from tkinter import filedialog
import io
import requests
from io import BytesIO
import tkinter.messagebox as messagebox
# Listas

# Reconocimiento Facial.
SUBSCRIPTION_KEY = None
SUBSCRIPTION_KEY = 'dbab3ae6c0bf483aa2b696698d1711e1'
BASE_URL = 'https://southcentralus.api.cognitive.microsoft.com'
OPTION = '/face/v1.0/'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)

def emotions(picture):
    imagenes_path = picture
    imagenes_data = open(imagenes_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
               'Content-Type': 'application/octet-stream'}

    params = {
        'detectionModel:detection_01'
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    response = requests.post(
        BASE_URL + OPTION + "detect/", headers=headers, params=params, data=imagenes_data)
    analysis = response.json()
    for x in analysis:
        analysis = x
        faceId = analysis['faceId']
        cuadroRostro = analysis['faceRectangle']
        top = cuadroRostro['top']
        left = cuadroRostro['left']
        width = cuadroRostro['width']
        height = cuadroRostro['height']
        letra = faceId
        Cuadro(top, left, width, height, letra, picture)
        return top
def Cuadro(top, left, width, height, letra, urlImagenes):
    image = Image.open(urlImagenes)
    draw = ImageDraw.Draw(image)
    draw.rectangle((left, top, left + width, top + height), outline='red', width=3)
    font = ImageFont.truetype('Fonts/ExtraLight.ttf', 15)
    text = letra
    draw.text((50, 50), text, fill='red', font=font, align='center')
    image.show(image)

### MEDICO ###
######################################################################################################################
def CrearArchivoMedico():
    existe =os.path.exists("Datos/medico.txt")
    if existe:
        print()
    else:
        file =open("Datos/medico.txt" ,"w")
        file.close()
def ExisteMedico(id):
    CrearArchivoMedico()
    file = open("Datos/medico.txt", "r")
    filas=file.readlines()
    for fila in filas:
        medico=fila.split(",")
        if str(medico[0])==id:
            print("El medico ya existe")
            file.close()
            return True
    file.close()
    return False
def EditarMedico():
    id=input("Ingrese el Id del medico")
    nombre=input("Ingrese el nuevo nombre del medico: ")
    apellido=input("Ingrese el nuevo apellido del medico: ")
    codigomedico=input("Ingrese el nuevo codigo de medico: ")
    contrasena=input("Ingrese la nueva contraseña: ")
    salario=input("Ingrese el nuevo salario: ")
    CrearArchivoMedico()
    file = open("Datos/medico.txt", "r")
    filas = file.readlines()
    filasTemporal=[]
    for fila in filas:
        medico = fila.split(",")
        if str(medico[0]) == id:
            filaModificada=str(id) + ","
            filaModificada=filaModificada+str(nombre) + ","
            filaModificada=filaModificada+str(apellido) + ","
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
        if medico[0] == id:
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
        filasTemporal.append({'Id':medico[0],
                            'Nombre':medico[1],
                            "Apellido":medico[2],
                            "Codigo de medico":medico[3],
                            "Contraseña":medico[4],
                            "Salario":medico[5]})
    file.close()
    return filasTemporal

### PACIENTE ####
######################################################################################################################
def CrearArchivoPaciente():
    existe = os.path.exists("Datos/paciente.txt")
    if existe:
        print()
    else:
        file = open("Datos/paciente.txt", "w")
        file.close()
def ExistePaciente(id):
    CrearArchivoPaciente()
    file = open("Datos/paciente.txt", "r")
    filas=file.readlines()
    for fila in filas:
        paciente=fila.split(",")
        if str(paciente[0])==id:
            print("El paciente ya existe")
            file.close()
            return True
    file.close()
    return False
def EditarPaciente():
    id = input("Ingrese el Id del paciente: ")
    nombre = input("Digite el nuevo nombre del paciente: ")
    apellido = input("Digite el nuevo apellido: ")
    cedula = input("Digite el nuevo numero de cedula:")
    direccion = input("Ingrese la nueva direccion: ")
    genero = input("Digite el nuevo genero: ")
    nacimiento = input("Ingrese la nueva fecha de nacimiento:")
    CrearArchivoPaciente()
    file = open("Datos/paciente.txt", "r")
    filas = file.readlines()
    filasTemporal=[]
    for fila in filas:
        paciente = fila.split(",")
        if str(paciente[0]) == id:
            filaModificada=str(id) + ","
            filaModificada=filaModificada+str(nombre) + ","
            filaModificada=filaModificada+str(apellido) + ","
            filaModificada =filaModificada+str(cedula) + ","
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
def EliminarPaciente(id):
    CrearArchivoPaciente()
    file = open("Datos/paciente.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        paciente = fila.split(",")
        if paciente[0] == id:
            filasTemporal.append(fila)
    file.close()
    file = open("Datos/paciente.txt", "w")
    for fila in filasTemporal:
        file.write(fila)
    file.close()
def ObtenerPaciente():
    CrearArchivoPaciente()
    file = open("Datos/paciente.txt", "r")
    filas = file.readlines()
    filasTemporal = []
    for fila in filas:
        paciente = fila.split(",")
        filasTemporal.append({'Id': paciente[0],
                            'Nombre':paciente[1],
                            'Apellido':paciente[2],
                            'Cedula': paciente[3],
                            'Direccion':paciente[4],
                            'Genero':paciente[5],
                            'Nacimiento':paciente[6]
                              })
    file.close()
    return filasTemporal

### HISTORIAL MÉDICO DE PACIENTE ###
######################################################################################################################
def CrearArchivoHistorialPaciente():
    existe = os.path.exists("Datos/historial_paciente.txt")
    if existe:
        print()
    else:
        file = open("Datos/historial_paciente.txt", "w")
        file.close()
def AgregarHistorialPaciente():
    imagenes_path = input("Introduzca el path de la imagen: ")
    codigorostro = emotions(imagenes_path)
    fecha = input("Ingrese la fecha de la cita: ")
    paciente = input("Ingrese el nombre completo del paciente atendido: ")
    medico = input("Ingrese el nombre del medico que atendio al paciente: ")
    emociones = EmocionesParteMedico(imagenes_path)
    partemedico = ParteMedico(imagenes_path)
    CrearArchivoHistorialPaciente()
    file = open("Datos/historial_paciente.txt", "a")
    file.write(str(codigorostro)+ ", ")
    file.write(str(fecha) + ", ")
    file.write(str(paciente) + ", ")
    file.write(str(medico) + ", ")
    file.write(str(emociones) + ", ")
    file.write(str(partemedico))
    file.write("\n")
    file.close()
    return {'Id': codigorostro,
            'Fecha': fecha,
            'paciente': paciente,
            'medico': medico,
            'Emociones':emociones,
            'Parte medico': partemedico}
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
                             'Fecha':hisPaciente[1],
                              "Paciente":hisPaciente[2],
                              "Medico":hisPaciente[3],
                              "Emciones": hisPaciente[4],
                              "Parte medico":hisPaciente[5]
                             })
    file.close()
    return filasTemporal

### Historial Medico ###
######################################################################################################################
def CrearArchivoHistorialMedico():
    existe=os.path.exists("Datos/historial_medico.txt")
    if existe:
        print()
    else:
        file=open("Datos/historial_medico.txt","w")
        file.close()
def AgregarHistorialMedico():
    imagenes_path = input("Introduzca el path de la imagen: ")
    codigorostro = emotions(imagenes_path)
    fecha = input("Ingrese la fecha: ")
    paciente = input("Ingrese el paciente: ")
    medico = input("Ingrese el médico: ")
    emociones = EmocionesParteMedico(imagenes_path)
    parteMedico = ParteMedico(imagenes_path)
    cantidadMinutos=input("Cantidad de minutos:")
    precioHora= input("Digite el precio por hora: ")
    precioTotal=input("Digite el precio total: ")
    CrearArchivoHistorialMedico()
    file = open("Datos/historial_medico.txt", "a")
    file.write(str(codigorostro) + ", ")
    file.write(str(fecha) +", ")
    file.write(str(paciente) + ", ")
    file.write(str(medico) + ", ")
    file.write(str(emociones) + ", ")
    file.write(str(parteMedico) + ", ")
    file.write(str(cantidadMinutos) + ", ")
    file.write(str(precioHora) + ", ")
    file.write(str(precioTotal) + ", ")
    file.write("\n")
    file.close()
    return {'Id': codigorostro,
            'Fecha': fecha,
            'Paciente': paciente,
            'Medico': medico,
            'Emociones': emociones,
            'Parte Medico': parteMedico,
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
                            'Fecha':hisMedico[1],
                            "Paciente":hisMedico[2],
                            "Medico":hisMedico[3],
                            "Emciones": hisMedico[4],
                            "Parte medico":hisMedico[5],
                            "Minutos":hisMedico[6],
                            "Precio por hora": hisMedico[7],
                            "Precio total": hisMedico[8]})
    file.close()
    return filasTemporal

### PARTE MEDICO ###
######################################################################################################################
def CrearArchivoParteMedico():
    existe = os.path.exists("Datos/parte_medico.txt.txt")
    if existe:
        print()
    else:
        file = open("Datos/parte_medico.txt", "w")
        file.close()
def EmocionesParteMedico(imagenes_path):
    SUBSCRIPTION_KEY = None
    SUBSCRIPTION_KEY = 'dbab3ae6c0bf483aa2b696698d1711e1'
    BASE_URL = 'https://southcentralus.api.cognitive.microsoft.com'
    OPTION = '/face/v1.0/'
    CF.BaseUrl.set(BASE_URL)
    CF.Key.set(SUBSCRIPTION_KEY)

    imagenes_data = open(imagenes_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
               'Content-Type': 'application/octet-stream'}

    params = {
        'detectionModel:detection_01'
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    response = requests.post(
        BASE_URL + OPTION + "detect/", headers=headers, params=params, data=imagenes_data)
    analysis = response.json()
    emociones= analysis
    for x in emociones:
        emocion=x['faceAttributes']['emotion']
        return {'Emociones': emocion
                }
def ParteMedico(imagenes_path):
    id=input("Ingrese el path de la imagen: ")
    codigorostro=emotions(id)
    list=[]
    x=EmocionesParteMedico(imagenes_path)['Emociones']
    anger=x['anger']
    disgust=x['disgust']
    contempt=x['contempt']
    sadness=x['sadness']
    happiness=x['happiness']
    neutral=x['neutral']
    fear=x['fear']
    surprise=x['surprise']
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
    file.write(str(codigorostro) + ", ")
    file.write(str(list))
    file.write("\n")
    file.close()
    return {'Id': codigorostro,
        'Enfermedades': list
            }
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

# Menú
# while True:
#
#     print("-------------------------------------------------------")
#     print("1- Registro de usuario.")
#     print("2- Inicio de sesion.")
#     print("3- Salir.")
#     print()
#     escoger = int(input("Ingrese una opcion: "))
#     print("-------------------------------------------------------")
#     if escoger == 1:
#         print("1- Registro como médico.")
#         print("2- Registro como paciente.")
#         print()
#         es = int(input("Ingrese una opcion: "))
#         print("-------------------------------------------------------")
#         if es == 1:
#             # Registro médico
#             AgregarMedico()
#         elif es == 2:
#             # Registro paciente
#             Agregarpaciente()
#     elif escoger == 2:
#         print("1- Inicio de sesión como médico.")
#         print("2- Inicio de sesión como paciente.")
#         print()
#         es1 = int(input("Ingrese una opción: "))
#         print("-------------------------------------------------------")
#         if es1 == 1:
#             #Inicio de sesion como medico
#             print("1- Ingresar con imagen.")
#             print("2- Ingresar con codigo de medico y contraseña.")
#             print()
#             opcion = int(input("Ingrese una opcion: "))
#             print("-------------------------------------------------------")
#             if opcion == 1:
#                 # Inicio de sesion con imagen.
#                 picture = input("Ingrese el path de la imagen: ")
#                 x = emotions(picture)
#                 lista = ObtenerMedico()
#                 for i in lista:
#                     persona = i['Id']
#                     nombre = i['Nombre']
#                     if str(x) == persona:
#                         print("El medico es:", nombre)
#                         print("Acceso Permitido.")
#                         print("-------------------------------------------------------")
#                         print("1- Editar medico.")
#                         print("2- Eliminar medico.")
#                         print("3- Exite medico.")
#                         print("4- Crear un nuevo historial medico.")
#                         print("5- Obtener historial medico.")
#                         print("6- Obtener historial paciente. ")
#                         print()
#                         opcion5 = int(input("Ingrese una opcion: "))
#                         if opcion5 == 1:
#                             EditarMedico()
#                         if opcion5 == 2:
#                             id = input("Ingrese el path de la imagen: ")
#                             EliminarMedico(id)
#                         if opcion5 == 3:
#                             id = input("Ingrese el path de la imagen: ")
#                             ExisteMedico(id)
#                         if opcion5 == 4:
#                             AgregarHistorialMedico()
#                         if opcion5 == 5:
#                             lista = ObtenerHistorialMedico()
#                             for i in lista:
#                                 picture = input("Ingrese el path de la imagen: ")
#                                 x = emotions(picture)
#                                 persona = i['Id']
#                                 if str(x) == persona:
#                                     print(ObtenerHistorialMedico())
#                         if opcion5 == 6:
#                             lista = ObtenerHistorialPaciente()
#                             for i in lista:
#                                 id = input("Ingrese el Id del paciente: ")
#                                 persona = i['Id']
#                                 if str(x) == id:
#                                     print(ObtenerHistorialPaciente())
#                     else:
#                         print("Acceso Denegado.")
#                         print("Usuario no registrado.")
#                         print("-------------------------------------------------------")
#             elif opcion == 2:
#                 # Inicio Sesion medico
#                 usuario = input("Ingrese su codigo de medico: ")
#                 contra = input("Ingrese su contraseña: ")
#                 print("-------------------------------------------------------")
#                 lista = ObtenerMedico()
#                 for x in lista:
#                     nombre=x['Nombre']
#                     usu= x['Codigo de medico']
#                     con= x['Contraseña']
#                     if usuario == usu:
#                         if contra == con:
#                             print("El medico es:",nombre)
#                             print("Acceso Permitido.")
#                             print("-------------------------------------------------------")
#                             print("1- Editar medico.")
#                             print("2- Eliminar medico.")
#                             print("3- Exite medico.")
#                             print("4- Crear un nuevo historial medico.")
#                             print("5- Obtener historial medico.")
#                             print("6- Obtener historial paciente.")
#                             print()
#                             opcion6 = int(input("Ingrese una opcion: "))
#                             if opcion6 == 1:
#                                 EditarMedico()
#                             if opcion6 == 2:
#                                 id = input("Ingrese el path de la imagen: ")
#                                 EliminarMedico(id)
#                             if opcion6 == 3:
#                                 id = input("Ingrese el Id del medico: ")
#                                 ExisteMedico(id)
#                             if opcion6 == 4:
#                                 AgregarHistorialMedico()
#                             if opcion6 == 5:
#                                 lista = ObtenerHistorialMedico()
#                                 for i in lista:
#                                     picture = input("Ingrese el path de la imagen: ")
#                                     persona = i['Id']
#                                     if str(x) == persona:
#                                         print(ObtenerHistorialMedico())
#                             if opcion6 == 6:
#                                 lista = ObtenerHistorialPaciente()
#                                 for i in lista:
#                                     id = input("Ingrese el Id del paciente: ")
#                                     persona = i['Id']
#                                     if str(x) == id:
#                                         print(ObtenerHistorialPaciente())
#                     elif usuario==usu:
#                             if  contra != con:
#                                 print("Contraseña Incorrecta.")
#                                 print("Acceso Denegado.")
#                                 print("-------------------------------------------------------")
#                     else:
#                         print("Usuario no registrado.")
#         elif es1 == 2:
#             # Inicio Sesion paciente
#             print("1- Ingresar con imagen.")
#             print("2- Ingresar con numero de cédula.")
#             print()
#             opcion1 = int(input("Ingrese una opcion: "))
#             print("-------------------------------------------------------")
#             if opcion1 == 1:
#                 # Inicio de sesion con imagen.
#                 picture = input("Ingrese el path de la imagen: ")
#                 x = emotions(picture)
#                 lista = ObtenerPaciente()
#                 for i in lista:
#                     persona = i['Id']
#                     nombre = i['Nombre']
#                     if str(x) == persona:
#                         print("El paciente es:",nombre)
#                         print("Acceso Permitido.")
#                         print("-------------------------------------------------------")
#                         print("1- Editar paciente.")
#                         print("2- Exitir paciente.")
#                         print("3- Crear una cita.")
#                         print("4- Obtener diagnostico de enfermedades.")
#                         print()
#                         opcion7=int(input("Ingrese una opcion: "))
#                         if opcion7 == 1:
#                             EditarPaciente()
#                         if opcion7 == 2:
#                             id = input("Ingrese el path de la imagen: ")
#                             ExistePaciente(id)
#                         if opcion7 == 3:
#                             AgregarHistorialPaciente()
#                         if opcion7 == 4:
#                             lista = ObtenerParteMedico()
#                             for i in lista:
#                                 picture = input("Ingrese el path de la imagen: ")
#                                 x = emotions(picture)
#                                 persona = i['Id']
#                                 enfermedades = i['Enfermedades']
#                                 if str(x) == persona:
#                                     print(enfermedades)
#                     else:
#                         print("Acceso Denegado.")
#                         print("Usuario no registrado.")
#                         print("-------------------------------------------------------")
#             elif opcion1 == 2:
#                 cedula = input("Ingrese su número de cédula: ")
#                 lista = ObtenerPaciente()
#                 for x in lista:
#                     nombre=x['Nombre']
#                     ced = x['Cedula']
#                     if cedula == ced:
#                         print("El paciente es:",nombre)
#                         print("Acceso Permitido.")
#                         print("-------------------------------------------------------")
#                         print("1- Editar paciente.")
#                         print("2- Exitir paciente.")
#                         print("3- Crear una cita.")
#                         print("4- Obtener diagnostico de enfermedades.")
#                         opcion8 = int(input("Ingrese una opcion: "))
#                         if opcion8 == 1:
#                             EditarPaciente()
#                         if opcion8 == 2:
#                             id = input("Ingrese el path de la imagen: ")
#                             ExistePaciente(id)
#                         if opcion8 == 3:
#                             AgregarHistorialPaciente()
#                         if opcion8 == 4:
#                             lista = ObtenerParteMedico()
#                             for i in lista:
#                                 picture = input("Ingrese el path de la imagen: ")
#                                 x = emotions(picture)
#                                 persona = i['Id']
#                                 enfermedades = i['Enfermedades']
#                                 if str(x) == persona:
#                                     print(enfermedades)
#                     elif cedula != ced:
#                         print("Acceso Denegado.")
#                         print("Verifique que este registrado.")
#                         print("-------------------------------------------------------")
#
#     elif escoger == 3:
#         break



class Ventana(tk.Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)  # parámetros que usted quiere enviar atraves del la clase Frame
        self.master = master
        self.IniciarMenu()  # Mostrar el menú

        self.label = tk.Label(self, text="Hospital")
        self.label.pack(padx=20, pady=20)

        self.button1 = tk.Button(root, text='Salir de la aplicación', command=self.ExitApplication, bg='brown',
                                 fg='white')
        # self.button1.pack()
        # self.listbox = tk.Listbox(self)
        # self.listbox.pack()

    def IniciarMenu(self):
        self.master.title("Hospital.")
        self.pack(fill=BOTH, expand=1)
        # Crear la instancia del menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Crear el objeto Archivo
        registro = Menu(menu)
        #menu.add_cascade(label="Registro", menu=registro)
        #menu.add_command(label="Medico", command=self.GenerarVentana1)

        # Crear el objeto Ventanas
        ventanas = Menu(menu)
        menu.add_cascade(label="Registro", menu=ventanas)
        menu.add_cascade(label="Inicio de sesion", menu=ventanas)
        ventanas.add_command(label="Medico", command=self.GenerarVentana1)
        ventanas.add_command(label="Paciente", command=self.GenerarVentana2)
        # ventanas.add_command(label="Medico", command=self.GenerarVentana3)
        # ventanas.add_command(label="Paciente", command=self.GenerarVentana4)




    def ExitApplication(self):
        MsgBox = tk.messagebox.askquestion('Salida de la aplicación',
                                           '¿Esta seguro que desea salir de la aplicación?',
                                           icon='warning')
        if MsgBox == 'yes':
            root.destroy()
        else:
            tk.messagebox.showinfo('Return', 'Ahora se retorná a la pantalla principal')

    def GenerarVentana1(self):
        ventana1 = tk.Toplevel()
        ventana1.title("Crear Medico")

        #Ventanas de medico
        ventana1.lbNombre=tk.Label(ventana1, text="Nombre del medico: ")
        ventana1.lbApeliido = tk.Label(ventana1, text="Apellido del medico: ")
        ventana1.lbCodigoMedico = tk.Label(ventana1, text="Codigo medico: ")
        ventana1.lbContrasenna = tk.Label(ventana1, text="Contraseña: ")
        ventana1.lbSalario = tk.Label(ventana1, text="Salario: ")
        # Campos para escribir
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
                                      command=lambda: self.CerrarVentana(ventana1.destroy()))
        # Boton Guardar
        ventana1.btnGuardar = tk.Button(ventana1, text="Guardar",
                                        command=lambda: self.GuardarRegistroMedico(
                                            self.nombreMedico.get(),
                                            self.ApellidoMedico.get(),
                                            self.CodigoMedico.get(),
                                            self.Contrasenna.get(),
                                            self.Salario.get(),
                                            self.nombreMedico.set(""),
                                            self.ApellidoMedico.set(""),
                                            self.CodigoMedico.set(""),
                                            self.Contrasenna.set(""),
                                            self.Salario.set("")
                                        ))

        ventana1.lbNombre.grid(column=0, row=0, padx=(20, 10))
        ventana1.lbApeliido.grid(column=0, row=1, padx=(20, 10))
        ventana1.lbCodigoMedico.grid(column=0, row=2, padx=(20, 10))
        ventana1.lbContrasenna.grid(column=0, row=3, padx=(20, 10))
        ventana1.lbSalario.grid(column=0, row=4, padx=(20, 10))

        ventana1.entryNombreMedico.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventana1.entryApellidoMedico.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventana1.entryCodigoMedico.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        ventana1.entryContrasenna.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        ventana1.entrySalario.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))

        ventana1.btnSalir.grid(column=1, row=5, pady=15)
        ventana1.btnGuardar.grid(column=0, row=5, pady=15)

    def GenerarVentana2(self):
        ventana2 = tk.Toplevel()
        ventana2.title("Crear Paciente")

        #Ventanas de medico
        ventana2.lbNombre = tk.Label(ventana2, text="Nombre del paciente: ")
        ventana2.lbApellido = tk.Label(ventana2, text="Apellido del paciente: ")
        ventana2.lbCedula = tk.Label(ventana2, text="Numero de cedula: ")
        ventana2.lbDireccion = tk.Label(ventana2, text="Direccion: ")
        ventana2.lbGenero = tk.Label(ventana2, text="Genero: ")
        ventana2.lbNacimiento = tk.Label(ventana2, text="Fecha de nacimiento: ")
        # Campos para escribir
        self.nombrePaciente = tk.StringVar()
        ventana2.entryNombrePaciente = tk.Entry(ventana2, textvariable=self.nombrePaciente, width=40)
        self.ApellidoPaciente = tk.StringVar()
        ventana2.entryApellidoPaciente = tk.Entry(ventana2, textvariable=self.ApellidoPaciente, width=40)
        self.Cedula = tk.StringVar()
        ventana2.entryCedula = tk.Entry(ventana2, textvariable=self.Cedula, width=40)
        self.Direccion = tk.StringVar()
        ventana2.entryDireccion = tk.Entry(ventana2, textvariable=self.Direccion, width=40)
        self.Genero = tk.StringVar()
        ventana2.entryGenero = tk.Entry(ventana2, textvariable=self.Genero, width=40)
        self.Nacimiento = tk.StringVar()
        ventana2.entryNacimiento = tk.Entry(ventana2, textvariable=self.Nacimiento, width=40)
        # Boton Salir
        ventana2.btnSalir = tk.Button(ventana2, text="Salir",
                                      command=lambda: self.CerrarVentana(ventana2.destroy()))
        # Boton Guardar
        ventana2.btnGuardar = tk.Button(ventana2, text="Guardar",
                                        command=lambda: self.GuardarRegistroPaciente(
                                            self.nombrePaciente.get(),
                                            self.ApellidoPaciente.get(),
                                            self.Cedula.get(),
                                            self.Direccion.get(),
                                            self.Genero.get(),
                                            self.Nacimiento.get(),
                                            self.nombrePaciente.set(""),
                                            self.ApellidoPaciente.set(""),
                                            self.Cedula.set(""),
                                            self.Direccion.set(""),
                                            self.Genero.set(""),
                                            self.Nacimiento.set("")
                                        ))

        ventana2.lbNombre.grid(column=0, row=0, padx=(20, 10))
        ventana2.lbApellido.grid(column=0, row=1, padx=(20, 10))
        ventana2.lbCedula.grid(column=0, row=2, padx=(20, 10))
        ventana2.lbDireccion.grid(column=0, row=3, padx=(20, 10))
        ventana2.lbGenero.grid(column=0, row=4, padx=(20, 10))
        ventana2.lbNacimiento.grid(column=0, row=5, padx=(20, 10))

        ventana2.entryNombrePaciente.grid(column=1, row=0, pady=5, columnspan=2, padx=(20, 10))
        ventana2.entryApellidoPaciente.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
        ventana2.entryCedula.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
        ventana2.entryDireccion.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
        ventana2.entryGenero.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
        ventana2.entryNacimiento.grid(column=1, row=5, pady=5, columnspan=2, padx=(20, 10))

        ventana2.btnSalir.grid(column=1, row=6, pady=15)
        ventana2.btnGuardar.grid(column=0, row=6, pady=15)

    def CerrarVentana(self, *argumentos):
        print("Gracias por usar nuestra aplicación")

    def RefrescarDatos(self):
        global listaCursos
        i = 0
        self.listbox.delete(0,tk.END)
        while i < len(listaCursos):
            self.listbox.insert(i, listaCursos[i])
            i += 1

    def GuardarRegistroMedico(self, *argumentos):
        print("Guardar registro")
        messagebox.showinfo("Información", "Registro almacenado")
        nuevoCurso = [argumentos[0], argumentos[1],argumentos[2], argumentos[3], argumentos[4]]
        CrearArchivoMedico()
        file = open("Datos/medico.txt", "a")
        #file.write(str(id) + ",")
        file.write(str(argumentos[0]) + ",")
        file.write(str(argumentos[1]) + ",")
        file.write(str(argumentos[2]) + ",")
        file.write(str(argumentos[3]) + ",")
        file.write(str(argumentos[4]))
        file.write("\n")
        file.close()
        return {#'id': id,
                'Nombre': argumentos[0],
                'Apellido': argumentos[1],
                'Codigo de medico': argumentos[2],
                'Contraseña': argumentos[3],
                'Salario por hora': argumentos[4]
                }
    def GuardarRegistroPaciente(self, *argumentos):
        print("Guardar registro")
        messagebox.showinfo("Información", "Registro almacenado")
        nuevoCurso = [argumentos[0], argumentos[1],argumentos[2], argumentos[3], argumentos[4],argumentos[5]]
        CrearArchivoPaciente()
        file = open("Datos/paciente.txt", "a")
        #file.write(str(id) + ",")
        file.write(str(argumentos[0]) + ",")
        file.write(str(argumentos[1]) + ",")
        file.write(str(argumentos[2]) + ",")
        file.write(str(argumentos[3]) + ",")
        file.write(str(argumentos[4]) + ",")
        file.write(str(argumentos[5]))
        file.write("\n")
        file.close()
        return {#'Id': id,
                'Cedula': argumentos[0],
                'Nombre': argumentos[1],
                'Apellido': argumentos[2],
                'Direccion': argumentos[3],
                'Genero': argumentos[4],
                'Fecha de nacimiento': argumentos[5]
                }
    # def VerRegistro(self):
    #     global listaCursos
    #     global registroActual
    #     self.curso = listaCursos[registroActual]
    #     self.nombreCurso.set(self.curso[0])
    #     self.codigoCurso.set(self.curso[1])
    #
    # def RegistroSiguiente(self):
    #     global registroActual
    #     global listaCursos
    #     if registroActual < len(listaCursos)-1:
    #         registroActual += 1
    #         self.VerRegistro()
    #
    # def RegistroAnterior(self):
    #     global registroActual
    #     if registroActual > 0:
    #         registroActual -=1
    #         self.VerRegistro()

    # def GenerarVentana2(self):
    #     ventana2 = tk.Toplevel()
    #     ventana2.title("Crear Paciente")
    #
    #     ventana2.lbNombre = tk.Label(ventana2, text="Nombre del paciente: ")
    #     ventana2.lbApellido = tk.Label(ventana2, text="Apellido del paciente: ")
    #     ventana2.lbCedula = tk.Label(ventana2, text="Numero de cedula: ")
    #     ventana2.lbDireccion = tk.Label(ventana2, text="Direccion: ")
    #     ventana2.lbGenero = tk.Label(ventana2, text="Genero: ")
    #     ventana2.lbNacimiento = tk.Label(ventana2, text="Fecha de nacimiento: ")
    #
    #     self.nombrePaciente = tk.StringVar()
    #     ventana2.entryNombrePaciente = tk.Entry(ventana2, textvariable=self.nombrePaciente, width=40)
    #     self.ApellidoPaciente = tk.StringVar()
    #     ventana2.entryApellidoPaciente = tk.Entry(ventana2, textvariable=self.ApellidoPaciente, width=40)
    #     self.Cedula = tk.StringVar()
    #     ventana2.entryCedula = tk.Entry(ventana2, textvariable=self.Cedula, width=40)
    #     self.Direccion = tk.StringVar()
    #     ventana2.entryDireccion = tk.Entry(ventana2, textvariable=self.Direccion, width=40)
    #     # self.Genero = tk.StringVar()
    #     # ventana2.entryGenero = tk.Entry(ventana2, textvariable=self.nombreCurso, width=40)
    #     self.Genero1 = tk.IntVar()
    #     Checkbutton(self.Genero1, text="male", variable=self.Genero1).grid(row=4, sticky=W)
    #     self.Genero2= tk.IntVar()
    #     Checkbutton(self.Genero2, text="female", variable=self.Genero2).grid(row=5, sticky=W)
    #     self.Nacimiento = tk.StringVar()
    #     ventana2.entryNacimiento = tk.Entry(ventana2, textvariable=self.Nacimiento, width=40)
    #
    #     ventana2.btnSalir = tk.Button(ventana2, text="Salir",
    #                                   command=lambda: self.CerrarVentana(ventana2.destroy()))
    #
    #     ventana2.btnSiguiente = tk.Button(ventana2, text="Siguiente",
    #                                       command=self.RegistroSiguiente)
    #     ventana2.btnAnterior = tk.Button(ventana2, text="Anterior",
    #                                      command=self.RegistroAnterior)
    #
    #     ventana2.lbNombre.grid(column=0, row=0, padx=(20,10))
    #     ventana2.lbApellido.grid(column=0, row=1, padx=(20, 10))
    #     ventana2.lbCedula.grid(column=0, row=2, padx=(20, 10))
    #     ventana2.lbDireccion.grid(column=0, row=3, padx=(20, 10))
    #     #ventana2.lbGenero.grid(column=0, row=0, padx=(20, 10))
    #     ventana2.lbNacimiento.grid(column=0, row=6, padx=(20, 10))
    #
    #     ventana2.entryNombrePaciente.grid(column=1, row=0, pady=5, columnspan=2, padx=(20,10))
    #     ventana2.entryApellidoPaciente.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
    #     ventana2.entryCedula.grid(column=1, row=2, pady=5, columnspan=2, padx=(20, 10))
    #     ventana2.entryDireccion.grid(column=1, row=3, pady=5, columnspan=2, padx=(20, 10))
    #     ventana2.entryNacimiento.grid(column=1, row=4, pady=5, columnspan=2, padx=(20, 10))
    #
    #     ventana2.btnSiguiente.grid(column=0, row=3, pady=15)
    #     ventana2.btnAnterior.grid(column=1, row=3, pady=15)
    #     ventana2.btnSalir.grid(column=2, row=3, pady=15)
    #
    #     self.VerRegistro()

    # def GenerarVentana3(self):
    #     ventana2 = tk.Toplevel()
    #     ventana2.title("Mostrar Curso")
    #
    #     ventana2.lbCurso = tk.Label(ventana2, text="Nombre del curso: ")
    #     ventana2.lbCodigo = tk.Label(ventana2, text="Codigo del curso: ")
    #
    #     self.nombreCurso = tk.StringVar()
    #     ventana2.entryNombreCurso = tk.Entry(ventana2, textvariable=self.nombreCurso, width=40)
    #
    #     self.codigoCurso = tk.StringVar()
    #     ventana2.entryCodigoCurso = tk.Entry(ventana2, textvariable=self.codigoCurso, width=40)
    #
    #     ventana2.btnSalir = tk.Button(ventana2, text="Salir",
    #                                   command=lambda: self.CerrarVentana(ventana2.destroy()))
    #
    #     ventana2.btnSiguiente = tk.Button(ventana2, text="Siguiente",
    #                                       command=self.RegistroSiguiente)
    #     ventana2.btnAnterior = tk.Button(ventana2, text="Anterior",
    #                                      command=self.RegistroAnterior)
    #
    #     ventana2.lbCurso.grid(column=0, row=0, padx=(20,10))
    #     ventana2.lbCodigo.grid(column=0, row=1, padx=(20, 10))
    #
    #     ventana2.entryNombreCurso.grid(column=1, row=0, pady=5, columnspan=2, padx=(20,10))
    #     ventana2.entryCodigoCurso.grid(column=1, row=1, pady=5, columnspan=2, padx=(20, 10))
    #
    #     ventana2.btnSiguiente.grid(column=0, row=3, pady=15)
    #     ventana2.btnAnterior.grid(column=1, row=3, pady=15)
    #     ventana2.btnSalir.grid(column=2, row=3, pady=15)



if __name__=="__main__":
    root = tk.Tk()
    root.geometry("400x300")
    listaCursos = []
    registroActual = 0
    main = Ventana(root)
    main.pack(fill="both", expand=True)
    root.mainloop()



