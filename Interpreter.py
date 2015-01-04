from FunctionCalls import *
from AST import *
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *


class Interpreter(object):

    def __init__(self):
        self.memory = MemoryStack(Memory("GlobalMemory"))
        self.functions = {}

    @on('node')
    def visit(self, node):
        pass

    @when(BinExpr)
    def visit(self, node):
        left = node.left.accept2(self)
        right = node.right.accept2(self)
        return function_dict[node.op]([left,right])

    @when(Const)
    def visit(self, node):
        return node.value

    @when(Variable)
    def visit(self, node):
        pass

    @when(Funcall)
    def visit(self, node):
        pass

    @when(If)
    def visit(self, node):
        pass

    @when(IfElse)
    def visit(self, node):
        pass

    @when(Continue)
    def visit(self, node):
        pass

    @when(Break)
    def visit(self, node):
        pass

    @when(Print)
    def visit(self, node):
        print node.expression.accept2(self)

    @when(Return)
    def visit(self, node):
        pass

    @when(While)
    def visit(self, node):
        while node.condition.accept2(self):
            for instr in node.instructions:
                instr.accept2(self)

    @when(Fundef)
    def visit(self, node):
        self.functions[node.name] = node

    @when(Argument)
    def visit(self, node):
        pass

    @when(Declaration)
    def visit(self, node):
        for init in node.inits:
            init.accept2(self)

    @when(Program)
    def visit(self, node):
        for decl in node.declarations:
            decl.accept2(self)

        for fundef in node.fundefs:
            fundef.accept2(self)

        for instr in node.instructions:
            instr.accept2(self)

    @when(CompoundInstructions)
    def visit(self, node):
        self.memory.push(Memory("LocalMemory"))

        for decl in node.declarations:
            decl.accept2(self)
        for instr in node.instructions:
            instr.accept2(self)

        self.memory.pop()

    @when(Labeled)
    def visit(self, node):
        pass

    @when(Assignment)
    def visit(self, node):
        ## ???
        self.memory.put(node.name, node.expression.accept2(self))

    @when(Init)
    def visit(self, node):
        self.memory.put(node.name, node.expression.accept2(self))

    @when(Repeat)
    def visit(self, node):
        while True:
            for instr in node.instructions:
                instr.accept2(self)

            if not node.condition.accept2(self):
                break
