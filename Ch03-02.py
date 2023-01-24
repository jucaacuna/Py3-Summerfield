#!/usr/bin/env python3
# ENERO 2023
# Ejercicos resueltos del libro Summerﬁeld, M. (2010). Programming in Python 3: A Complete Introduction to
# the Python Language (2nd edition). Pearson Education, Inc. 

import collections
import string
import sys

def valor(elemento_dic):
    return elemento_dic[1]  # elemento_dic = dic.items(). 0=key, 1=value


words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            for word in line.lower().split():   # itera la línea, habiendo separado las palabras con split()
                word = word.strip(strip)        # Los cacteres definidos en "strip" son desagregados de los extremos de "word"
                if len(word) > 2:
                    words[word] += 1            # al diccionario "words" suma 1 a value en key = word. Va a agregar cada palabra al diccionario. Si ya está, le suma 1.
for word, conteo in sorted(words.items(), key=valor): #itera el diccionario (words.items) de manera ordenada por value.
    print("'{0}' occurs {1} times".format(word, words[word]))

