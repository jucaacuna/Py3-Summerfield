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

def mediana(lista):
    for a in range(1, len(lista)):
        elemento = 0
        while elemento < len(lista)-1:

            if lista[elemento] > lista[elemento + 1]:
                c=lista[elemento]
                lista[elemento]=lista[elemento + 1]
                lista[elemento + 1]=c
            elemento += 1

    print("Lista ordenada:",lista)
    cociente=int(len(lista)/2)
    if cociente*2 == len(lista):
        print("La cantidad de elementos es par")
        mediana_v=(lista[cociente]+lista[cociente-1])/2
    else:
        lugar= int(len(lista)/2)
        mediana_v =lista[lugar]
    
    print("El valor de la mediana es:", mediana_v)


    

def operaciones_lista(lista):
    print("Cantidad de elementos:", len(lista), "Suma de elementos: ", sum(lista))
    print("Máximo:", max(lista),"mínimo:", min(lista),"Promedio:",int(sum(lista)/len(lista)))

listaNum = []
cargar_lista("Indique los números: ", listaNum)
print("Los numeros ingresados fueron: ",listaNum)
operaciones_lista(listaNum)
mediana(listaNum)