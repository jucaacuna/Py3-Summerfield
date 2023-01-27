#!/usr/bin/env python3

# Apuntes:
# An iterable data type is one that can return each of its items one at a time.
# An iterator is an object that provides a __next__() method which returns each
#  successive item in turn, and raises a StopIteration exception when there are no more items.


# ITERNADO UNA LISTA.
# HABRÍA QUE HACER OTRO PROGRAMA PARA RECORRER... SETS POR EJEMPLO

x = ("banana","manzana","pera","frutilla",
 "duraznito","sandía","kiwi","naranja") # Tupla de 8 elementos.

# Iterando un iterable con conteo por medio de enumerate()

def a():
    for conteo, fruta in enumerate(x): # enumerate() default start = 0
        print("Conteo:", conteo, "Fruta:", x[conteo])

# Iterando un iterable por medio de range(). Provee el conteo...
# Range devuelve un "iterator" (una secuencia de elementos que apuntan al siguiente). Con list() se lo
# puede transformar.

def b():
    for conteo in range(len(x)):    
        print("Conteo:", conteo, "Fruta:", x[conteo])

# Iterando con while

def c():
    conteo = 0
    while conteo < len(x):
        print("Conteo:", conteo, "Fruta:", x[conteo])
        conteo += 1



######################################################################
# MAIN #

def main ():
    opción = str.lower(input("¿Cuál función usamos? "))
    print(opción)
    if opción == "a":
        print("Llegamos a a")
        a()
    elif opción == "b":
        b()
    elif opción == "c":
        c()


main()