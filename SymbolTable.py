#!/usr/bin/python


class Arg():
    def __init__(self, name, type):
        self.name = name
        self.type = type


class SymbolTable(object):
    def __init__(self, parent):  # parent scope and symbol table name
        self.parent = parent
        self.dictionary = {}


    def put(self, name, symbol):  # put variable symbol or fundef under <name> entry
        if name in self.dictionary.keys():
            self.dictionary[name] = symbol
            return False
        else:
            self.dictionary[name] = symbol
            return True

    def get(self, name):  # get variable symbol or fundef from <name> entry
        if name in self.dictionary.keys():
            return self.dictionary[name]
        elif self.parent != None:
            return self.getParentScope().get(name)
        else:
            return None


    def getParentScope(self):
        return self.parent


