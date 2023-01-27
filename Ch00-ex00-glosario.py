#!/usr/bin/env python3
# ENERO 2023
# 
# GLOSARIO DE TÉRMINOS EN INGLÉS NO TAN CONOCIDOS POR MI AL MOMRNTO DE LEER EL LIBRO:
#
# Summerﬁeld, M. (2010). Programming in Python 3: A Complete Introduction to
# the Python Language (2nd edition). Pearson Education, Inc. 
#
# La próxima versión deberá guardar los términos en una base de datos. 


glosario = {}


def buscar (palabra):
    if palabra in glosario:
        print("-", palabra, "-")
        print ("Quiere decir:", glosario[palabra])
        return
    else:
        print("NO SE ENCUENTRA INGRESADA")

    
def cargarArchivo():    #carga en el diccionario los términos guardos el archivo.
    try:
        archivo = None  #previendo que no se pueda abrir
        archivo = open("./Ch00-ex00-glosario.txt", encoding="utf8")
        for línea in archivo:
            línea = línea.split(":")
            if len(línea) < 3 :
                glosario[línea[0]]=línea[1].rstrip()
    except (IOError, OSError) as err:
        print(err)
    finally:
        if archivo is not None:
            archivo.close()

def agregarDic (palabra,significado):
    glosario[palabra] = significado

def guardarARchivo():   #carga en el archivo los términos guardos en el diccionario.
    try:
        archivo = None
        with open("./Ch00-ex00-glosario.txt", "w", encoding="utf8") as archivo:
            for palabra in glosario:
                línea = palabra + ":" + glosario[palabra] + "\n"
                archivo.write(línea)
    except (IOError, OSError) as err:
        print(err)
    finally:
        if archivo is not None:
            archivo.close()

def main():
    cargarArchivo()         
    while True:

        acción= str.lower(input("Ingrese 'buscar', 'agregar' o 'salir': "))

        if acción == "buscar":
            palabra = str.lower(input("Ingrese la palabra a buscar: "))
            buscar(palabra)
        elif acción == "agregar":
            palabra = str.lower(input("Ingrese la palabra a agregar:"))
            significado = str.lower(input("Ingrese el significado:"))

            agregarDic(palabra,significado)
        elif acción == "salir":
            break
    guardarARchivo()
        

main()