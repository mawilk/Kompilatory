
class Node(object):

    # def __str__(self):
    #     return self.printTree()
    #
    # def __str__(self):
    #     return self.__dict__.iteritems()

    def prosiaczek(self):
        print self.__class__.__name__
        for key,value in self.__dict__.iteritems():
            if isinstance(value,list):
                for n in value:
                    n.prosiaczek()
            elif isinstance(value,str):
                print value
            else:
                value.prosiaczek()



class BinExpr(Node):

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Const(Node):
    
    def __init__(self,value):
        self.value = value


class Integer(Const):
    pass


class Float(Const):
    pass


class String(Const):
    pass


class Variable(Node):
    
    def __init__(self,name):
        self.name = name
    
class Funcall(Node):

    def __init__(self,name,args):
        self.name = name
        self.args = args
        
class If(Node):
    
    def __init__(self,condition,instruction):
        self.condition = condition
        self.instruction = instruction
        
class IfElse(Node):
    
    def __init__(self,condition,instruction1,instruction2):
        self.condition = condition
        self.instruction1 = instruction1
        self.instruction2 = instruction2

class NoArgInstruction(Node):
    
    def __init__(self):
        self.instruction = self.__class__.__name__
        
class Continue(NoArgInstruction):
    pass
    
class Break(NoArgInstruction):
    pass
    
class OneArgInstruction(Node):

    def __init__(self,arg):
        self.instruction = self.__class__.__name__
        self.arg = arg

class Print(OneArgInstruction):
    pass
    
class Return(OneArgInstruction):
    pass
    
class While(Node):
    
    def __init__(self,condition,instruction):
        self.condition = condition
        self.instruction = instruction
        
class Fundef(Node):

    def __init__(self,name,ret,args,instructions):
        self.name = name
        self.ret = ret
        self.args = args
        self.instructions = instructions

class Arguments(Node):

    def __init__(self, arguments):
        self.arguments = arguments

class Argument(Node):

    def __init__(self,type,id):
        self.id = id
        self.type = type

class Fundefs(Node):

    def __init__(self, fundefs):
        self.fundefs = fundefs
        
class Declaration(Node):
    
    def __init__(self,type,inits):
        self.type = type
        self.inits = inits
        
class Declarations(Node):

    def __init__(self,declarations):
        self.declarations = declarations
        
class Program(Node):

    def __init__(self,declarations,fundefs,instructions):
        self.declarations = declarations
        self.fundefs = fundefs
        self.instructions = instructions
        
class Instructions(Node):

    def __init__(self,instructions):
        self.instructions = instructions
        
class CompoundInstructions(Node):

    def __init__(self,declarations,instructions):
        self.declarations = declarations
        self.instructions = instructions

class Expressions(Node):

    def __init__(self,expressions):
        self.expressions = expressions