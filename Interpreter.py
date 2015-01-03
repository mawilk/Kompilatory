
from AST import *
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *


class Interpreter(object):


    @on('node')
    def visit(self, node):
        pass

    #
    # @when(AST.BinOp)
    # def visit(self, node):
    #     r1 = node.left.accept(self)
    #     r2 = node.right.accept(self)
    #     # try sth smarter than:
    #     # if(node.op=='+') return r1+r2
    #     # elsif(node.op=='-') ...
    #
    # @when(AST.RelOp)
    # def visit(self, node):
    #     r1 = node.left.accept(self)
    #     r2 = node.right.accept(self)
    #     # ...
    #
    # @when(AST.Assignment)
    # def visit(self, node):
    #     pass
    # #
    # #
    #
    # @when(AST.Const)
    # def visit(self, node):
    #     return node.value
    #
    # # simplistic while loop interpretation
    # @when(AST.WhileInstr)
    # def visit(self, node):
    #     r = None
    #     while node.cond.accept(self):
    #         r = node.body.accept(self)
    #     return r


    @when(BinExpr)
    def visit(self, node):
        pass

    @when(Const)
    def visit(self, node):
        pass

    @when(Integer)
    def visit(self, node):
        pass

    @when(Float)
    def visit(self, node):
        pass

    @when(String)
    def visit(self, node):
        pass

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

    @when(NoArgInstruction)
    def visit(self, node):
        pass

    @when(Continue)
    def visit(self, node):
        pass

    @when(Break)
    def visit(self, node):
        pass

    @when(OneArgInstruction)
    def visit(self, node):
        pass

    @when(Print)
    def visit(self, node):
        pass

    @when(Return)
    def visit(self, node):
        pass

    @when(While)
    def visit(self, node):
        pass

    @when(Fundef)
    def visit(self, node):
        pass

    @when(Argument)
    def visit(self, node):
        pass

    @when(Declaration)
    def visit(self, node):
        pass

    @when(Program)
    def visit(self, node):
        pass

    @when(CompoundInstructions)
    def visit(self, node):
        pass

    @when(Labeled)
    def visit(self, node):
        pass

    @when(Assignment)
    def visit(self, node):
        pass

    @when(Init)
    def visit(self, node):
        pass

    @when(Repeat)
    def visit(self, node):
        pass
