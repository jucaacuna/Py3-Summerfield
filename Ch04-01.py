#!/usr/bin/env python3
# ENERO 2023
# Ejercicos resueltos del libro Summerﬁeld, M. (2010). Programming in Python 3: A Complete Introduction to
# the Python Language (2nd edition). Pearson Education, Inc. 

import os

lista = []
cambios = False #Identifica si hubieron cambios en la lista desde que se le cargó el archivo

def seleccionarArchivo():
    """ Esta función lista los archivos ".lst" en el directorio local.
    De no haberlos, pide ingresar el nombre para crear uno"""
    listita = []
    archivos = os.listdir(".")
    for archivo in archivos:
        if archivo[-4:] == ".lst":
            listita.append(archivo)
    if len(listita) == 0:
        print("\n No hay archivos en la carpeta")
        archivo = open("./LISTA.lst","x",encoding="utf8")    #crea el archivo
        archivo.close
        return "LISTA.lst"
    else:
        mostrarLista(listita)
        opción=int(input("¿Cuál archivo usaremos? _"))
        opción-=1
        return str(listita[opción])

def cargarArchivo(nombreArchivo):
    """ Lee el archivo y lo carga en lista """
    status = 1
    try:
        archivo = None  #previendo que no se pueda abrir
        archivo = open(nombreArchivo, encoding="utf8")
        conteo = 0
        for conteo, línea in enumerate(archivo):
            lista.append( línea.strip())
            
        if conteo < 1:
                print("No items are in the list")
                status = 0
        último = conteo
    except (IOError, OSError) as err:
        print(err)
    finally:    #Using "with" is also much shorter than writing equivalent try-finally blocks.  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        if archivo is not None:
            archivo.close()
            return status

def modificar_Lista(elemento, acción):
    """Carga nuevos elementos a la lista y elimina seleccionados """
    global cambios 
    cambios = True
    if acción == "a":
        str(elemento)
        lista.append(elemento)
        return
    elif acción == "d":
        int(elemento)
        lista.remove(lista[elemento])



def mostrarLista(elementos):
    """Muestra los elementos de la lista"""
    if len(elementos)<10:
        ancho=1
    elif 10<=len(elementos)<100:
        ancho=2
    for conteo, elemento in enumerate(elementos, start=1):
        print("{0:{a}}: {1}".format(conteo,elemento, a=ancho))
    return

def guardarArchivo(NombreArchivo, elementos):
    """Guarda en el archivo los cambios en la lista"""
    archivo = None
    try:
        if cambios == False:
            pass
        elif cambios == True:
            archivo = open(NombreArchivo, "w", encoding="utf-8")
            for elemento in elementos:
                archivo.write(elemento+"\n")
        
    except (IOError, OSError) as err:
        print(err)
    finally:    #Using "with" is also much shorter than writing equivalent try-finally blocks.  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        if archivo is not None:
            archivo.close()


def main():
    archivo = seleccionarArchivo()
    status=cargarArchivo(archivo)
    while True:
        if status == 0:     # si está vació el archivo
            a = str.upper(input("[A]dd  [Q]uit    :"))
            if a == "Q":
                break
            elif a == "A":
                b = input("Ingrese elemento:")
                modificar_Lista(b, acción="a")
                status += 1
        elif status == 1:
            a=str.upper(input("[A]dd  [D]elete  [S]ave  [Q]uit    :"))
            if a == "Q":
                break
            elif a == "A":
                b = input("Ingrese elemento:")
                modificar_Lista(b, acción="a")
                mostrarLista(lista)
            elif a == "S":        
                guardarArchivo("./archivo_de_listas.lst",lista)
            elif a == "D":
                b = input("Ingrese N° de elemento a eliminar:")
                modificar_Lista(b, acción="d")

main()