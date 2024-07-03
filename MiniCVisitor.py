# Generated from MiniC.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#program.
    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#definition.
    def visitDefinition(self, ctx:MiniCParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#data_definition.
    def visitData_definition(self, ctx:MiniCParser.Data_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#declarator.
    def visitDeclarator(self, ctx:MiniCParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function_definition.
    def visitFunction_definition(self, ctx:MiniCParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function_header.
    def visitFunction_header(self, ctx:MiniCParser.Function_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameter_list.
    def visitParameter_list(self, ctx:MiniCParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:MiniCParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function_body.
    def visitFunction_body(self, ctx:MiniCParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#block.
    def visitBlock(self, ctx:MiniCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#statement.
    def visitStatement(self, ctx:MiniCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#ifStat.
    def visitIfStat(self, ctx:MiniCParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#whileStat.
    def visitWhileStat(self, ctx:MiniCParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignState.
    def visitAssignState(self, ctx:MiniCParser.AssignStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#exprStat.
    def visitExprStat(self, ctx:MiniCParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#expression.
    def visitExpression(self, ctx:MiniCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#binary.
    def visitBinary(self, ctx:MiniCParser.BinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unary.
    def visitUnary(self, ctx:MiniCParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#primary.
    def visitPrimary(self, ctx:MiniCParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#argument_list.
    def visitArgument_list(self, ctx:MiniCParser.Argument_listContext):
        return self.visitChildren(ctx)



del MiniCParser