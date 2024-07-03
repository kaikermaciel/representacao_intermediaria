"""
Alunos: 
- Kaike Ribas Maciel : 22250538
- Maria Vitória Costa do Nascimento : 
- Rodrigo Santos Correa: 22251139
"""

from MiniCParser import MiniCParser
from MiniCVisitor import MiniCVisitor

class EvalVisitor(MiniCVisitor):
    def __init__(self):
        self.symbol_table = {}
        self.errors = []
        self.return_type = None

    def add_error(self, message, ctx):
        line = ctx.start.line
        char_position_in_line = ctx.start.column
        self.errors.append(f"Line {line}:{char_position_in_line}: {message}")

    def print_errors(self):
        if self.errors == []:
            print("Compilado com sucesso: Nenhum erro encontrado!")
        else:
            print("\nErrors:")
            for error in self.errors:
                print(error)
    temp_count = 0
    def new_temp(self):
        self.temp_count += 1
        return f't{self.temp_count}'
    
    def visitProgram(self, ctx: MiniCParser.ProgramContext):
        return self.visitChildren(ctx)
    
    def visitDefinition(self, ctx: MiniCParser.DefinitionContext):
        return self.visitChildren(ctx)

    def visitData_definition(self, ctx: MiniCParser.Data_definitionContext):
        if(ctx.declarator(0).getText() in self.symbol_table):
            self.add_error(f"Error: Variável '{ctx.declarator(0).getText()}' já foi declarada anteriormente", ctx)
        else:
            self.symbol_table[self.visit(ctx.declarator(0))] = ctx.getChild(0).getText() 
        return self.visitChildren(ctx)

    def visitDeclarator(self, ctx: MiniCParser.DeclaratorContext):
        return ctx.IDENTIFIER().getText()

    def visitFunction_definition(self, ctx: MiniCParser.Function_definitionContext):
        function_type = ctx.getChild(0).getText()

        # [0] = nome da função || [1] = total de argumentos no parâmetro
        function_information = self.visit(ctx.function_header()) 

        if function_type == 'int' or function_type == 'char':
            self.symbol_table[function_information[0]] = [function_type, function_information[1]]
            self.return_type = function_type
        else:
            self.symbol_table[function_information[0]] = 'void'
            self.return_type = function_type

        self.visit(ctx.function_body())
        self.current_function_return_type = None
        return 

    def visitFunction_header(self, ctx: MiniCParser.Function_headerContext):
        function_name = self.visit(ctx.declarator())
        arguments_count = self.visit(ctx.parameter_list())
        return [function_name, arguments_count]

    def visitParameter_list(self, ctx: MiniCParser.Parameter_listContext):
        if ctx.parameter_declaration():
            arguments_count = self.visit(ctx.parameter_declaration())
            return arguments_count
        return 0

    def visitParameter_declaration(self, ctx: MiniCParser.Parameter_declarationContext):
        if ctx.getChild(0).getText() == 'int' or ctx.getChild(0).getText() == 'char':
            for i in ctx.declarator():
                self.symbol_table[self.visit(i)] = ctx.getChild(0).getText()
            return len(ctx.declarator())

    def visitFunction_body(self, ctx: MiniCParser.Function_bodyContext):
        for i in ctx.data_definition():
            self.visit(i)
        for i in ctx.statement():
            self.visit(i)

    def visitStatement(self, ctx: MiniCParser.StatementContext):
        #tratamento de retorno
        if ctx.getChild(0).getText() == "return":
            var = self.visit(ctx.exprStat()) if ctx.exprStat() else 'void'
            if var != self.return_type:
                self.add_error(f"Error: Tipo de retorno incompatível. Esperado '{self.return_type}' mas obteve '{var}'", ctx)

        if ctx.ifStat():
            self.visit(ctx.ifStat())
        if ctx.whileStat():
            self.visit(ctx.whileStat())
        if ctx.assignState():
            self.visit(ctx.assignState())
        if ctx.exprStat():
            self.visit(ctx.exprStat())
        if ctx.block():
            self.visit(ctx.block())

    def visitIfStat(self, ctx:MiniCParser.IfStatContext):
        print("oiiii")
        if ctx.expression():
            cond = self.visit(ctx.expression())
            then_label = self.new_temp()
            end_label = self.new_temp()
            print(f"if {cond} goto {then_label}\ngoto {end_label}\n{then_label}:")
            if ctx.statement():
                self.visit(ctx.statement())
            print(f"{end_label}:")

    def visitWhileStat(self, ctx:MiniCParser.WhileStatContext):
        start_label = self.new_temp()
        middle_label = self.new_temp()
        end_label = self.new_temp()
        print(f'{start_label}: ')
        cond = self.visit(ctx.expression())
        print(f"if {cond} goto {middle_label}\ngoto {end_label}\n{middle_label}:")
        self.visit(ctx.statement())
        return
        
    def visitAssignState(self, ctx:MiniCParser.AssignStateContext):
        value = self.visit(ctx.expression())
        code = f"{ctx.IDENTIFIER().getText()} = {value};"
        print(code)
        return code

    def visitexprStat(self, ctx:MiniCParser.ExprStatContext):
        if ctx.expression():
            express = self.new_temp()
            code = f"{ctx.expression()};"
            print(code)
            return code

    def visitExpression(self, ctx: MiniCParser.ExpressionContext):
        l = list(ctx.getChildren())
        for i in ctx.binary():
            return self.visit(i)

    def visitBinary(self, ctx: MiniCParser.BinaryContext):
        if ctx.unary():
            return self.visitUnary(ctx.unary())
        else:
            left = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            if left.getText() in self.symbol_table:
                left_type = self.symbol_table[left.getText()]
            else:
                left_type = self.visit(left)
                if left.getChild(0) is None:
                    self.add_error(f"Error: Variavel '{left.getText()}' nao foi declarada",ctx)
                    return left.getText()

            if right.getText() in self.symbol_table:
                right_type = self.symbol_table[right.getText()]
            else:
                right_type = self.visit(right)


            if operator == '=':
                if left_type != right_type:
                    self.add_error(f"Error: Tipo incompatível para a atribuição. '{left_type}' e '{right_type}'", ctx)
                return left_type
            elif operator in ['+', '-', '*', '/', '%', '+=', '-=', '*=', '/=', '%=']:
                if left_type == 'int' and right_type == 'int':
                    print(left.getText(), operator, right.getText())
                    return 'int'
                elif left_type == 'char' and right_type == 'char':
                    return 'char'
                else:
                    self.add_error(f"Error: Operadores incompatíveis. '{left_type}' e '{right_type}'", ctx)
                    return None
            elif operator in ['==', '!=', '<', '<=', '>', '>=']:
                if left_type == right_type:
                    return f'{left.getText()}{operator}{right.getText()}'
                else:
                    self.add_error(f"Error: Operadores incompatíveis para comparação. '{left_type}' e '{right_type}'", ctx)
                    return None
        return None
    
    def visitUnary(self, ctx: MiniCParser.UnaryContext):
        if ctx.IDENTIFIER() is not None:
            var = ctx.IDENTIFIER().getText()
            if self.symbol_table.get(var) != 'int':
                self.add_error("Error: tipo nao aceito para o operador unario",ctx)
            return var
        else:
            return self.visit(ctx.getChild(0))

    def visitPrimary(self, ctx: MiniCParser.PrimaryContext):
        l = list(ctx.getChildren())
        if len(l) == 4: #caso identifer - argument_list : chamada de funçao
            if ctx.IDENTIFIER().getText() not in self.symbol_table:
                self.add_error(f"Error: Variavel '{ctx.IDENTIFIER().getText()}' nao foi declarada",ctx)
            else:
                argument_list_size = self.visit(l[2])
                function_info = self.symbol_table.get(ctx.IDENTIFIER().getText())
                self.return_type = function_info[0]
                if function_info[1] > argument_list_size:
                    self.add_error(f"Error: A quantidade de argumentos passados foi menor. A função requer {function_info[1]} mas apenas {argument_list_size} foi informado", ctx)
                elif function_info[1] < argument_list_size:
                    self.add_error(f"Error: A quantidade de argumentos passados foi maior. A função requer {function_info[1]} mas {argument_list_size} foram informados", ctx)     
                else:
                    parametro = self.get_argument_types(l[2])
                    for i in range(argument_list_size):
                        if parametro[i] != self.return_type:
                            self.add_error(f"Error: Tipo de argumento incompatível na posição {i+1}. Esperado '{self.return_type}' mas obteve '{parametro[i]}'", ctx)
        elif len(l) == 3: #caso expression
            return self.visit(l[1])
        else: #todos os casos : indetifier | constantes
            if ctx.IDENTIFIER():
                if ctx.IDENTIFIER().getText() not in self.symbol_table:
                    self.add_error(f"Error: Variavel '{ctx.IDENTIFIER().getText()}' nao foi declarada",ctx)
                return ctx.IDENTIFIER().getText()
            
            elif ctx.CONSTANT_INT():
                self.symbol_table[ctx.CONSTANT_INT().getText()] = 'int'
                return ctx.CONSTANT_INT().getText()
            
            elif ctx.CONSTANT_CHAR():
                self.symbol_table[ctx.CONSTANT_CHAR().getText()] = 'char'
                return ctx.CONSTANT_CHAR().getText()

    def get_argument_types(self, argument_list_ctx):
        types = []
        for i in range(0,argument_list_ctx.getChildCount(),2):
            arg = argument_list_ctx.getChild(i)
            if arg.getText() in self.symbol_table:
                types.append(self.symbol_table[arg.getText()])
            else:
                types.append(self.visit(arg))
        return types
    
    def visitArgument_list(self, ctx: MiniCParser.Argument_listContext):
        for i in ctx.binary():
            self.visit(i)  
        return len(ctx.binary())

    def visitBlock(self, ctx: MiniCParser.BlockContext):
        if ctx.statement():
            for i in ctx.statement():
                self.visit(i)
