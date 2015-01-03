
class Memory:
    def __init__(self):
        self.variables = {}

    def has_key(self, name):  # variable name
        return self.variables.has_key(name)

    def get(self, name):  # get from memory current value of variable <name>
        for element in self.variables.keys():
            if element == name:
                return self.variables[element]
        return None

    def insert(self, name, value): # puts into memory current value of variable <name>
        self.variables[name]=value

    def set(self, name, value): # sets value of variable <name>
        for element in self.variables.keys():
            if element == name:
                self.variables[element] = value
                return True
        return False

class MemoryStack:
    def __init__(self, memory=None):  # initialize memory stack with memory <memory>
        if memory == None:
            self.stack = []
        else:
            self.stack = [memory]

    def get(self, name):  # get from memory stack current value of variable <name>
        for i in reversed(range(len(self.stack))):
            return self.stack[i].get(name)
        return None

    def insert(self, name, value): # puts into memory stack current value of variable <name>
        self.stack[len(self.stack)-1].insert(name, value)

    def set(self, name, value): # sets value of variable <name>
        for i in reversed(range(len(self.stack))):
            val = self.stack[i].get(name)
            if val != None:
                return self.stack[i].set(name, value)
        return False

    def push(self, memory):  # push memory <memory> onto the stack
        self.stack.append(memory)

    def pop(self):  # pops the top memory from the stack
        if self.stack != []:
            return self.stack[-1]
        else:
            return None


