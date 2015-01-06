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
        if type(left) is list:
            left = left[0]
        if type(right) is list:
            right = right[0]
        # print left, right, node.lineno
        return function_dict[node.op]([left,right])

    @when(Const)
    def visit(self, node):
        return node.value

    @when(Variable)
    def visit(self, node):
        # ??
        x = self.memory.get(node.name)
        # print node.name, x
        # print(self.memory)
        return x

    @when(Funcall)
    def visit(self, node):
        function = self.functions.get(node.name)
        # print "CallPush"
        self.memory.push(Memory(node.name))
        
        params = function.arguments
        vals = node.args
        symbols = []
        for param,val in zip(params,vals):
            name = param.name
            value = val.accept2(self)
            if type(value) is list:
                value = value[0]
            symbols.append(Symbol(name,value))
            # self.memory.put(name,value,True)
        for symbol in symbols:
            self.memory.put(symbol.name,symbol.value,True)
        
        result = None
        try:
            function.instructions.accept2(self)
        except ReturnValueException as ret:
            result = ret.value
        
        # print "CallPop"
        self.memory.pop()
        return result

    @when(If)
    def visit(self, node):
        try:
            if node.condition.accept2(self):
                node.instruction.accept2(self)
        except BreakException:
            raise BreakException

    @when(IfElse)
    def visit(self, node):
        try:
            if node.condition.accept2(self):
                node.instruction1.accept2(self)
            else:
                node.instruction2.accept2(self)                
        except BreakException:
            raise BreakException

    @when(Continue)
    def visit(self, node):
        raise ContinueException

    @when(Break)
    def visit(self, node):
        raise BreakException

    @when(Print)
    def visit(self, node):
        print node.arg.accept2(self)

    @when(Return)
    def visit(self, node):
        result = node.arg.accept2(self)
        raise ReturnValueException(result)

    @when(While)
    def visit(self, node):
        try:
            while node.condition.accept2(self):
                try:
                    node.instruction.accept2(self)
                except ContinueException:
                    pass
        except BreakException:
            pass
            
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
        # print "CompoundPush"
        try:
            self.memory.push(Memory("LocalMemory"))

            for decl in node.declarations:
                decl.accept2(self)
            for instr in node.instructions:
                result = instr.accept2(self)

        finally:
            # print "CompoundPop"
            self.memory.pop()


    @when(Labeled)
    def visit(self, node):
        pass

    @when(Assignment)
    def visit(self, node):
        ## ???
        self.memory.put(node.name, node.expression.accept2(self), False)

    @when(Init)
    def visit(self, node):
        value = node.expression.accept2(self)
        if type(value) is list:
            value = value[0]
        # print node.name, value
        # print(self.memory)
        self.memory.put(node.name, value, True)

    @when(Repeat)
    def visit(self, node):
        try:
            while True:
                try:
                    for instr in node.instructions:
                        instr.accept2(self)
                except ContinueException:
                    pass
                if node.condition.accept2(self):
                    break
        except BreakException:
            pass
