#!/usr/bin/env python3
# ENERO 2023
# Ejercicos resueltos del libro Summerﬁeld, M. (2010). Programming in Python 3: A Complete Introduction to
# the Python Language (2nd edition). Pearson Education, Inc. 


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


class Account:
    def __init__(self, accountNumber, accountName):
        self.__accountNumber = accountNumber
        self.__accountName = accountName
        self.__transactions = []

    @property
    def accountnumber(self):
        return self.__accountNumber

    @property
    def accountName(self):
        return self.__accountName

    @accountName.setter
    def accountName(self, newName):
        if len(newName)>3:
            self.__accountName = newName

    def __len__(self):
        return len(self.__transactions)
    
    @property
    def balance(self):
        total = None
        for moviemiento in self.__transactions:
            total += moviemiento.usd()
        return total

    @property
    def all_usd(self):
        for movimiento in self.__transactions:
            if movimiento.currency != "USD":
                return False
        return True

    def apply(self, transaction):
        self.__transactions.append(transaction)
    
"""    def save():
        


    def load():
        
"""