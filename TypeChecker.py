#!/usr/bin/python
import AST
from SymbolTable import SymbolTable


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
        pass

    def visit_Const(self, node):
        pass

    def visit_Integer(self, node):
        pass

    def visit_Float(self, node):
        pass

    def visit_String(self, node):
        pass

    def visit_Variable(self, node):
        pass

    def visit_Funcall(self, node):
        pass

    def visit_If(self, node):
        pass

    def visit_IfElse(self, node):
        pass

    def visit_NoArgInstruction(self, node):
        pass

    def visit_Continue(self, node):
        pass

    def visit_Break(self, node):
        pass

    def visit_Print(self, node):
        pass

    def visit_Return(self, node):
        pass

    def visit_While(self, node):
        pass

    def visit_Fundef(self, node):
        pass

    def visit_Argument(self, node):
        pass

    def visit_Declaration(self, node):
        pass

    def visit_Program(self, node):
        pass

    def visit_CompoundInstruction(self, node):
        pass

    def visit_Labeled(self, node):
        pass

    def visit_Assignment(self, node):
        pass

    def visit_Init(self, node):
        pass

    def visit_Repeat(self, node):
        pass
