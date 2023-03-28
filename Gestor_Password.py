# SPANISH (Realizar un programa que permita generar contraseñas seguras.)

# ENGLISH (Make a program that allows you to generate secure passwords.)

# Import libraries
from pickle import TRUE
from docx2pdf import convert
from random import *
from ast import main
import string
import random
import time
import sys
import os

# Declaracion de variables para que las opciones se mantengan desactivadas, y solo cuando el usuario la activen se habiliten.
mayus = False
minus = False
num = False
longitud = 8

# Funcion de ingresar que sirve para que el usuario introduzca un numero de caracteres que tenga la pass.
def fIngresar(Introducir):
    import os
    while True:
        try:
            vTexto = int(input(Introducir))
        except ValueError:
            (print("\nPor favor, ingrese un numero entero...\n"))
            os.system("pause")
        else:
            break
    return vTexto

# Esto genera la pass de la siguiente manera.
def fGenerar_Pass(longitud = 8, Mayusculas = False, Minusculas = False, Numeros = False):
    caracteres = [] #Los caracteres de la pass se van a almacenar en esta var.
    if(Mayusculas):
        # Este metido va a agregar a caracteres todos los simbolos del ascii mayusculos, importados desde ese comando.
        caracteres += string.ascii_uppercase

    if(Minusculas):
        # Este metido va a agregar a caracteres todos los simbolos del ascii minisculos, importados desde ese comando.
        caracteres += string.ascii_lowercase

    if(Numeros):
        # Este metido va a agregar a caracteres todos los numeros, importados desde ese comando.
        caracteres += string.digits

    while True:
        max = True
        min = True
        num = True
        sim = True
        contraseña = "".join(random.choice(caracteres) for i in range(longitud))
        if(Mayusculas):
            max = False
            for i in contraseña:
                if (i.isupper()):
                    max = True
        if(Minusculas):
            min = False
            for i in contraseña:
                if (i.islower()):
                    min = True
        if(Numeros):
            num = False
            for i in contraseña:
                if (i.isdigit()):
                    num = True
        if(max and min and num and sim):
            break

    return contraseña

def fFormato():
    # Esta funcion realiza la siguiente funcion:
        # Al exportar una pass, si quieres puedes elegir en que formato exportarla.
        
    os.system("cls")
    os.system("color 0F")
    print("""
        ┌─────────────────────────────────────────────────────────┐
        │               Menu Gestor de contraseñas                │
        │_________________________________________________________│
        │                                                         │
        │    1- .txt                                              │
        │    2- .docx                                             │
        │    3- .xlsx                                             │
        │    4- Otro                                              │
        │    5- Volver                                            │
        │                                                         │
        └─────────────────────────────────────────────────────────┘ 
    """)
    TipoArchivo = input("\n\tElija un formato de archivo para guardar la pass: ") #Con esta variable, introduces el numero del formato que se ve en pantalla.

    if (TipoArchivo == '1'): # Si el archivo es igual a 1 pues se va a guardar en formato .txt
        archivo = open("Semana 08\Contraseña.txt", "a")
        archivo.write(fAutomatico + '\n')
        archivo.close()
        print("\n\tContraseña guardada en el archivo\n")

    elif (TipoArchivo == '2'): # Si el archivo es igual a 1 pues se va a guardar en formato .dock
        archivo = open("Semana 08\Contraseña.docx", "a")
        archivo.write(fAutomatico + '\n')
        archivo.close()
        print("\n\tContraseña guardada en el archivo\n")

    elif (TipoArchivo == '3'): # Si el archivo es igual a 1 pues se va a guardar en formato .xlsx
        archivo = open("Semana 08\Contraseña.xlsx", "a")
        archivo.write(fAutomatico + '\n')
        archivo.close()
        print("\n\tContraseña guardada en el archivo\n")
    
    # Si se selecciona la opcion 4, pues el usuario digita el tipo de formato obviamente seguido de un punto, ejemplo, .pdf
    elif (TipoArchivo == '4'):
        TipoArchivoIngresar = input("\n\tDigame usted el tipo de formato de archivo desea: ")
        archivo = open("Semana 08\Contraseña"+TipoArchivoIngresar, "a")
        archivo.write(fAutomatico + '\n')
        archivo.close()
        print("\n\tContraseña guardada en el archivo\n")
    
    elif (TipoArchivo == 5):
        return main()

while True:
    # Este es el menu que primeramente se ejecuta para poder ingresar al gestor de pass.
    Encriptar = '' # Esto sirve para encriptar la password seguido de eso en la linea de codigo 169 y 184, procedemos a completarla.
    os.system("cls")
    os.system("color F0")
    print("""
        ┌─────────────────────────────────────────────────────────┐
        │               Menu Gestor de contraseñas                │
        │_________________________________________________________│
        │                                                         │
        │    1- Ingresar Longitud (Default 8)                     │
        │    2- Generar pass automaticamente                      │
        │    3- Generar pass con opciones                         │
        │    4- Incluir Mayúsculas                                │
        │    5- Incluir Minúsculas                                │
        │    6- Incluir números                                   │
        │    7- Desactivar todas las opciones                     │
        │    8- Salir                                             │
        │                                                         │
        └─────────────────────────────────────────────────────────┘ 
    
    """)
    Op = fIngresar("\tIngrese una opcion: ")

    if(Op == 1):
        while True:
            longitud = fIngresar("\tIntroduce la longitud de la contraseña: ")
            if longitud >= 8:
                break
            else:
                print("\nLa longitud debe de ser mayor o igual a 8")

    elif (Op == 2):
        def fAutomatico(longitud): # fAutomatico() lo que hace es generar una pass automatica sin tener que activar las demas opciones.
            minusculas = string.ascii_lowercase
            mayusculas = string.ascii_uppercase
            numeros = string.digits
            secuencia = minusculas + mayusculas + numeros
            fAutomatico = sample(secuencia, longitud)
            resultado = "".join(fAutomatico)
            return resultado
        fAutomatico = fAutomatico(longitud)
        for item in range(len(fAutomatico)):
            Encriptar = Encriptar + '*' # Encriptar ahora va a tener el valor de asterisco para que nuestra pass se oculte.
        print("\n\tLa contraseña generada es: ", Encriptar, "\n")
        Guardar = input("\n\t¿Deseas guardarla en un archivo? (S/N): ").upper() # Si deseamos guardar el archivo, ponemos S, o si no, pues N.
        if Guardar == "S":
            fFormato() # Si hemos picado en que si, pues se va a llamar a la funcion fFormato()
        else:
            print("\n\tContraseña no guardada\n") # De lo contrario, pues no me va a guardar la pass y me va a tirar ese msj.

    elif(Op == 3):
        if(mayus == False and minus == False and num == False): # En este caso si op == 3, pues aqui si me va a pedir que al menos active una opcion para generar la pass.
            print("\tDebe Activar al menos una opcion...")

        else: # De lo contrario, pues va a generar la pass.
            contraseña = fGenerar_Pass(longitud, mayus, minus, num)
            for item in range(len(contraseña)):
                Encriptar = Encriptar + '*'
            print("\n\tLa contraseña generada es: ", Encriptar)
            Guardar = input("\n\t¿Deseas guardarla en un archivo? (S/N): ").upper()
            if Guardar == "S":
                fFormato()
            else:
                print("\n\tContraseña no guardada\n")

    elif(Op == 4): # Op 4 sirve para activar las mayusculas.
        if(mayus == False):
            mayus = True
            print("\n\tSe ha activado la opción de mayúsculas.\n")
        else:
            print("\n\tLa opción de mayúsculas ya está activada.\n")

    elif(Op == 5): # Op 4 sirve para activar las minusculas.
        if(minus == False):
            minus = True
            print("\n\tSe ha activado la opción de minúsculas.\n")
        else:
            print("\n\tLa opción de minúsculas ya está activada.\n")

    elif(Op == 6): # Op 4 sirve para activar los numeros.
        if(num == False):
            num = True
            print("\tSe ha activado la opción de números.\n")
        else:
            print("\tLa opción de números ya está activada.\n")

    elif(Op == 7): # op 7 Evalua si no se han activado ninguna de las opciones o si se activaron todas.
        if(mayus == False and minus == False and num == False):
            print("\tNo se ha activado ninguna opción.\n")
        else:
            print("\tSe han desactivado todas las opciones.\n")
            mayus = False
            minus = False
            num = False

    elif(Op == 8): # Op de salir del programa gestor de password
        exit()
    
    print("\n")
    os.system("pause")