#!/usr/bin/python


class Arg():
    def __init__(self, name, type):
        self.name = name
        self.type = type


class SymbolTable(object):
    def __init__(self, parent):  # parent scope and type table name
        self.parent = parent
        self.dictionary = {}


    def put(self, name, type):  # put variable type or fundef under <name> entry
        if name in self.dictionary.keys():
            self.dictionary[name] = type
            return False
        else:
            self.dictionary[name] = type
            return True

    def get(self, name):  # get variable type or fundef from <name> entry
        if name in self.dictionary.keys():
            return self.dictionary[name]
        elif self.parent != None:
            return self.getParentScope().get(name)
        else:
            return None


    def getParentScope(self):
        return self.parent


