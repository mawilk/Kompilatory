def indenting(indent):
    if indent == 0:
        return ''
    else:
        return "|  " * indent


class Node(object):
    def __str__(self):
        return self.printTree(0)

    def printTree(self, indent):
        raise Exception("printTree not defined in class " + self.__class__.__name__)


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def printTree(self, indent):
        result = indenting(indent) + self.op + "\n"
        result += self.left.printTree(indent + 1) + "\n"
        result += self.right.printTree(indent + 1)
        return result


class Const(Node):
    def __init__(self, value):
        self.value = str(value)

    def printTree(self, indent):
        return indenting(indent) + self.value


class Integer(Const):
    pass


class Float(Const):
    pass


class String(Const):
    pass


class Variable(Node):
    def __init__(self, name):
        self.name = name

    def printTree(self, indent):
        return indenting(indent) + self.name


class Funcall(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def printTree(self, indent):
        result = indenting(indent) + 'FUNCALL\n'
        result += indenting(indent + 1) + self.name + '\n'
        result += '\n'.join(element.printTree(indent + 1) for element in self.args)
        return result


class If(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

    def printTree(self, indent):
        result = indenting(indent) + 'IF\n'
        result += self.condition.printTree(indent + 1) + '\n'
        result += self.instruction.printTree(indent + 1)
        return result


class IfElse(Node):
    def __init__(self, condition, instruction1, instruction2):
        self.condition = condition
        self.instruction1 = instruction1
        self.instruction2 = instruction2

    def printTree(self, indent):
        result = indenting(indent) + 'IF\n'
        result += self.condition.printTree(indent + 1) + '\n'
        result += self.instruction1.printTree(indent + 1) + '\n'
        result += indenting(indent + 1) + 'ELSE\n'
        result += self.instruction2.printTree(indent + 1)
        return result


class NoArgInstruction(Node):
    def __init__(self):
        self.name = self.__class__.__name__

    def printTree(self, indent):
        return indenting(indent) + self.name.upper()


class Continue(NoArgInstruction):
    pass


class Break(NoArgInstruction):
    pass


class OneArgInstruction(Node):
    def __init__(self, arg):
        self.name = self.__class__.__name__
        self.arg = arg

    def printTree(self, indent):
        return indenting(indent) + self.name.upper() + '\n' + self.arg.printTree(indent + 1)


class Print(OneArgInstruction):
    pass


class Return(OneArgInstruction):
    pass


class While(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

    def printTree(self, indent):
        result = indenting(indent) + 'WHILE\n'
        result += self.condition.printTree(indent + 1) + '\n'
        result += self.instruction.printTree(indent + 1)
        return result


class Fundef(Node):
    def __init__(self, name, ret, arguments, instructions):
        self.name = name
        self.ret = ret
        self.arguments = arguments
        self.instructions = instructions

    def printTree(self, indent):
        result = indenting(indent) + 'FUNDEF\n'
        result += indenting(indent + 1) + self.name + '\n'
        result += indenting(indent + 1) + 'RET ' + self.ret + '\n'
        result += '\n'.join(x.printTree(indent + 1) for x in self.arguments) + '\n'
        result += self.instructions.printTree(indent + 1)
        return result


class Argument(Node):
    def __init__(self, arg_type, name):
        self.name = name
        self.arg_type = arg_type

    def printTree(self, indent):
        return indenting(indent) + "ARG " + self.name


class Declaration(Node):
    def __init__(self, decl_type, inits):
        self.decl_type = decl_type
        self.inits = inits

    def printTree(self, indent):
        result = indenting(indent) + "DECL\n"
        result += '\n'.join(element.printTree(indent + 1) for element in self.inits)
        return result


class Program(Node):
    def __init__(self, declarations, fundefs, instructions):
        self.declarations = declarations
        self.fundefs = fundefs
        self.instructions = instructions

    def printTree(self, indent):
        return '\n'.join(
            indenting(indent) + str(x) for x in self.declarations + self.fundefs + self.instructions) + '\n'


class CompoundInstructions(Node):
    def __init__(self, declarations, instructions):
        self.declarations = declarations
        self.instructions = instructions

    def printTree(self, indent):
        return '\n'.join(x.printTree(indent) for x in self.declarations + self.instructions)


class Labeled(Node):
    def __init__(self, name, instruction):
        self.name = name
        self.instruction = instruction

    def printTree(self, indent):
        result = indenting(indent) + 'LABELED\n'
        result += indenting(indent + 1) + self.name + '\n'
        result += self.instruction.printTree(indent + 1)
        return result


class Assignment(Node):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def printTree(self, indent):
        result = indenting(indent) + '=\n'
        result += indenting(indent + 1) + self.name + '\n'
        result += self.expression.printTree(indent + 1)
        return result


class Init(Node):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def printTree(self, indent):
        result = indenting(indent) + "=\n"
        result += indenting(indent + 1) + self.name + "\n"
        result += self.expression.printTree(indent + 1)
        return result


class Repeat(Node):
    def __init__(self, instruction, condition):
        self.instruction = instruction
        self.condition = condition

    def printTree(self, indent):
        result = indenting(indent) + 'REPEAT\n' + self.instruction.printTree(indent + 1) + '\n'
        result += indenting(indent) + 'UNTIL\n' + self.condition.printTree(indent + 1)
        return result
