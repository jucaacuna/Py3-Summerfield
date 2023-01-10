#!/usr/bin/env python3
# ENERO 2023
# Ejercicos resueltos del libro Summerﬁeld, M. (2010). Programming in Python 3: A Complete Introduction to
# the Python Language (2nd edition). Pearson Education, Inc.  


def cargar_lista(msg, lista):
    while True:
        num=input(msg)
        if not num:
            break
        else:
            lista.append(int(num))

def operaciones_lista(lista):
    print("Cantidad de elementos:", len(lista), "Suma de elementos: ", sum(lista))
    print("Máximo:", max(lista),"mínimo:", min(lista),"Promedio:",int(sum(lista)/len(lista)))

listaNum = []
cargar_lista("Indique los números: ", listaNum)
print("Los numeros ingresados fueron: ",listaNum)
operaciones_lista(listaNum)