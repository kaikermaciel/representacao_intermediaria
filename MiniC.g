 
/* Alunos: 
- Kaike Ribas Maciel : 22250538 
- Maria Vitória Costa do Nascimento: 22053592
- Rodrigo Santos Correa: 22251139
*/

grammar MiniC;

program : definition (definition)*;

definition: data_definition | function_definition;

data_definition : ('int' | 'char') declarator (',' declarator)* ';';

declarator : IDENTIFIER;

function_definition : ('int' | 'char' )? function_header function_body;

function_header : declarator parameter_list;

parameter_list : '(' (parameter_declaration)? ')';

parameter_declaration : ('int' | 'char') declarator (',' declarator)*;

function_body : '{' (data_definition)* (statement)* '}';

block : '{' (statement)* '}' ;

statement:  ifStat
        |   whileStat
        |   assignState
        |   exprStat
        |   block;

ifStat: 'if' '(' expression ')' statement ('else' statement)? ;  
whileStat: 'while' '(' expression ')' statement;
assignState: IDENTIFIER '=' (expression) ';';
exprStat: (expression) ';';

expression : binary (',' binary)* ;

binary: IDENTIFIER '=' binary | IDENTIFIER '+=' binary | IDENTIFIER '-=' binary | IDENTIFIER '*=' binary | IDENTIFIER '/=' binary | IDENTIFIER '%=' binary | binary '==' binary | binary '!=' binary | binary '<' binary | binary '<=' binary | binary '>' binary | binary '>=' binary | binary '+' binary | binary '-' binary | binary '*' binary | binary '/' binary | binary '%' binary | unary ;

unary : '++' IDENTIFIER | '--' IDENTIFIER | primary ;

primary : IDENTIFIER | CONSTANT_INT | CONSTANT_CHAR |'(' expression ')' | IDENTIFIER '(' (argument_list)? ')' ;

argument_list : binary (',' binary)* ;

IDENTIFIER : [a-zA-Z] [a-zA-Z0-9_]* ;

CONSTANT_INT: [0-9]+;

CONSTANT_CHAR: '\'' [a-zA-Z]+ '\'';


WS : [ \t\r\n]+ -> skip ;
