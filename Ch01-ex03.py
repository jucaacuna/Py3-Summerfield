#!/usr/bin/env python3
# ENERO 2023
# Ejercicos resueltos del libro Summerﬁeld, M. (2010). Programming in Python 3: A Complete Introduction to
# the Python Language (2nd edition). Pearson Education, Inc.  

import random

sustantivos = ["arbol","Laura","Moria","casa","mate","luna","Harry","barco","pirata","naranja"]
articulos = ["el","la","un","una",""]
adjetivos = ["rojo","grande","redondo","cuadrado","liso","mojado","seco","bajo","divertido","dulce"]

estructura1 = (articulos,sustantivos,adjetivos)
estructura2 = (articulos,adjetivos,sustantivos)
e=(estructura1,estructura2)
i = 0

while i < 3:
    linea=""
    ind=random.randint(0,1)
    for tipoPalbra in e[ind]:
        linea += random.choice(tipoPalbra)+" "
    print(linea)
    i+=1