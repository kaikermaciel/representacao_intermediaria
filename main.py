"""
Alunos: 
- Kaike Ribas Maciel : 22250538
- Maria Vitória Costa do Nascimento : 22053592
- Rodrigo Santos Correa: 22251139
"""

from antlr4 import *
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from Visitor import EvalVisitor

import sys

input_text = FileStream(sys.argv[1])
lexer = MiniCLexer(input_text)
stream = CommonTokenStream(lexer)
parser = MiniCParser(stream)

tree = parser.program()
visitor = EvalVisitor()
visitor.visit(tree)
visitor.print_errors()
print(visitor.errors)
#print(tree.toStringTree(recog=parser))
