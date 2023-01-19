#!/usr/bin/env python3
# ENERO 2023
# Ejercicos resueltos del libro Summerﬁeld, M. (2010). Programming in Python 3: A Complete Introduction to
# the Python Language (2nd edition). Pearson Education, Inc. 

import sys
import unicodedata

def print_unicode_table(words):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode) # Stop at surrogate pairs
    a = 0
    while a < len(words):
        word = words[a]
        a += 1
        while code < end:
            c = chr(code)
            name = unicodedata.name(c, "*** unknown ***")
            bandera = True
            for word in words:
                if word not in name.lower():
                    bandera = False
                    break
            if bandera:
                print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
                    code, name.title()))
            code += 1




if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("uso: {0} [palabra1 palabra2 palabra3]".format(sys.argv[0]))
        # words continúa vacía
    else:
        words = sys.argv[1:]
        print_unicode_table(words)
