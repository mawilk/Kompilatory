#!/usr/bin/python
import AST
from SymbolTable import SymbolTable
from Types import ttype


# class NodeVisitor(object):
#     def visit(self, node):
#         method = 'visit_' + node.__class__.__name__
#         visitor = getattr(self, method, self.generic_visit)
#         return visitor(node)
#
#
#     def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
#         if isinstance(node, list):
#             for elem in node:
#                 self.visit(elem)
#         else:
#             for child in node.children:
#                 if isinstance(child, list):
#                     for item in child:
#                         if isinstance(item, AST.Node):
#                             self.visit(item)
#                 elif isinstance(child, AST.Node):
#                     self.visit(child)

                    # simpler version of generic_visit, not so general
                    #def generic_visit(self, node):
                    #    for child in node.children:
                    #        self.visit(child)


class TypeChecker(object):

    errors = []

    def visit_BinExpr(self, node):

        node.left.Scope = node.Scope
        node.right.Scope = node.Scope
        type1 = node.left.accept(self)
        type2 = node.right.accept(self)
        if ttype[node.op][type1][type2] != {}:
            return ttype[node.op][type1][type2]
        else:
            self.errors.append("Invalid expression")
            return 'int'

    def visit_Const(self, node):
        pass

    def visit_Integer(self, node):
        return 'int'

    def visit_Float(self, node):
        return 'float'

    def visit_String(self, node):
        return 'string'

    def visit_Variable(self, node):
        if node.Scope.getVariable(node.name) == False:
            self.errors.append("Variable "+node.name+" not initialised")
            return 'int'


    def visit_Funcall(self, node):
        type1 = node.Scope.getFunction(node.name)

        #TODO

        return type1

    def visit_If(self, node):
        node.condition.Scope = node.Scope
        node.condition.accept(self)
        node.instruction.Scope = SymbolTable(node.Scope)
        node.instruction.accept(self)


    def visit_IfElse(self, node):
        node.condition.Scope = node.Scope
        node.condition.accept(self)
        node.instruction1.Scope = SymbolTable(node.Scope)
        node.instruction1.accept(self)
        node.instruction2.Scope = SymbolTable(node.Scope)
        node.instruction2.accept(self)


    def visit_NoArgInstruction(self, node):
        pass


    def visit_Continue(self, node):
        pass


    def visit_Break(self, node):
        pass


    def visit_OneArgInstruction(self, node):
        node.arg.Scope = node.Scope
        node.arg.accept(self)


    def visit_Print(self, node):
        node.arg.Scope = node.Scope
        node.arg.accept(self)


    def visit_Return(self, node):
        node.arg.Scope = node.Scope
        node.arg.accept(self)


    def visit_While(self, node):
        node.condition.Scope = node.Scope
        node.condition.accept(self)
        node.instruction.Scope = SymbolTable(node.Scope)
        node.instruction.accept(self)


    def visit_Fundef(self, node):
        args = {}
        for arg in node.arguments:
            args[arg.name] = arg.type
        node.Scope.putFunction(node.name, node.type, args)
        Scope = SymbolTable(node.Scope)

        node.instructions.Scope = Scope
        node.instructions.accept(self)


    def visit_Argument(self, node):
        return node.name, node.type


    def visit_Declaration(self, node):
        for init in node.inits:
            init.Scope = node.Scope
            init.accept(self)


    def visit_Program(self, node):
        node.Scope = SymbolTable(None)

        for fundef in node.fundefs:
            fundef.Scope = node.Scope
            fundef.accept(self)

        for decl in node.declarations:
            decl.Scope = node.Scope
            decl.accept(self)

        for instr in node.instructions:
            instr.Scope = node.Scope
            instr.accept(self)

        return self.errors


    def visit_CompoundInstruction(self, node):
        for decl in node.declarations:
            decl.Scope = node.Scope
            decl.accept(self)

        for instr in node.instructions:
            instr.Scope = node.Scope
            instr.accept(self)


    def visit_Labeled(self, node):
        node.instruction.Scope = node.Scope
        node.instruction.accept(self)


    def visit_Assignment(self, node):
        node.expression.Scope = node.Scope
        type1 = node.expression.accept(self)
        if type1 == False:
            self.errors.append("Incorrect expression")
        type2 = node.Scope.getVariable(node.name)
        if type2 == None:
            self.errors.append("Variable was not declared")
        if type1 != type2:
            self.errors.append("Can't assign")


    def visit_Init(self, node):
        type = node.expression.accept(self)
        if node.Scope.putVariable(node.name, type) == False:
            self.errors.append("Variable " + node.name + "already initialized")


    def visit_Repeat(self, node):
        Scope = SymbolTable(node.Scope)
        for instr in node.instructions:
            instr.Scope = Scope
            instr.accept(self)

        node.condition.Scope = Scope
        node.condition.accept(self)
