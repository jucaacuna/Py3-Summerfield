#!/usr/bin/env python3
# ENERO 2023
# Ejercicos resueltos del libro Summerﬁeld, M. (2010). Programming in Python 3: A Complete Introduction to
# the Python Language (2nd edition). Pearson Education, Inc. 

# Implement a Transaction class that takes an amount, a date, a currency (default “USD”—U.S. dollars), a USD conversion rate (default 1),
# and a description (default None). All of the data attributes must be private. Provide the following read-only properties: amount, date,
#  currency, usd_conversion_rate, description, and usd (calculated from amount *usd_conversion_rate). This class can be implemented in about sixty lines
# including some simple doctests. A model solution for this exercise (and the next one) is in ﬁle Account.py.

class Trasaction():
# although it is always safe to return an object’s immutable data attributes, we should normally only ever return copies of an object’s
# mutable data attributes to avoid the object’s internal state leaking out and being accidentally invalidated.

    def __init__(self, amount, date, currency = "USD", usd_conversion_rate = 1, description = None):
        self.__amount = amount  # si el atributo tiene nombre que comienza con __ es privado
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description

    @property   # El decorator @property crea un atributo accesible desde fuera del objeto, manteniendo seguro (inmutable) el atributo secreto.
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date
    
    @property
    def currency(self):
        return self.__currency

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate
        
    @property
    def description(self):
        return self.__description

    @property
    def usd(self):
        return self.__amount * self.__usd_conversion_rate

