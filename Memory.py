class Symbol(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Memory:
    def __init__(self, name):  # memory name
        self.name = name
        self.symbols = []

    def has_key(self, name):  # variable name
        for symbol in self.symbols:
            if symbol.name == name:
                return True
        return False

    def get(self, name):  # get from memory current value of variable <name>
        for symbol in self.symbols:
            if symbol.name == name:
                return symbol.value
        return None

    def put(self, name, value):  # sets value of variable <name>
        for symbol in self.symbols:
            if symbol.name == name:
                symbol.value = value
        else:
            self.symbols.append(Symbol(name, value))


class MemoryStack:
    def __init__(self, memory=None):  # initialize memory stack with memory <memory>
        if memory != None:
            self.stack = [memory]
        else:
            self.stack = []

    def get(self, name):  # get from memory stack current value of variable <name>
        for i in reversed(range(len(self.stack))):
            value = self.stack[i].get(name)
            if value != None:
                return value
        return None

    def put(self, name, value):  # sets value of variable <name>
        for i in reversed(range(len(self.stack))):
            value = self.stack[i].get(name)
            if value != None:
                self.stack[i].put(name, value)
        else:
            self.stack[-1].put(name, value)


    def push(self, memory):  # push memory <memory> onto the stack
        self.stack.append(memory)

    def pop(self):  # pops the top memory from the stack
        if self.stack == []:
            return None
        else:
            return self.stack[-1]