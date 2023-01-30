#!/usr/bin/env python3
# ENERO 2023
# Ejercicos resueltos del libro Summerﬁeld, M. (2010). Programming in Python 3: A Complete Introduction to
# the Python Language (2nd edition). Pearson Education, Inc. 


import os
import sys


def listarArchivos(path = "."):
    """ Esta función lista los archivos y los devuelve como lista
    The paths are optional; if not given . is used."""

    for dirpath, dirnames, files in os.walk(path): # Para cada directorio en el árbol enraizado en el directorio top (incluido top), produce una tupla de 3 tuplas (dirpath, dirnames, filenames).
        print("\nCarpeta encontrada:", dirpath)
        for file_name in files:
            print("|")
            print("--- {0}".format(file_name))

def procesarComando(): 
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
            print("\nuso: {0} [/path]".format(sys.argv[0]))
            return "-h"
        else:
            return sys.argv[1]

def main():
    dirección = None
    dirección = procesarComando()
    if dirección != "-h":
        if dirección == None:
            listarArchivos()
        else:
            listarArchivos(dirección)


main()