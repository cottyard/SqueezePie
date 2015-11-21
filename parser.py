import ply.yacc as yacc
import testcases
from lexer import tokens
from representation import *

def p_program(p):
  "program : statements"
  p[0] = Program(p[1])

def p_statements(p):
  "statements : statements statement"
  p[1].append(p[2])
  p[0] = p[1]

def p_statements_empty(p):
  "statements :"
  p[0] = []

def p_statement(p):
  """statement : while_stmt
               | define_stmt
               | assign_stmt
               | expression SEMICOLON
               | return_stmt
               | if_stmt
  """
  p[0] = p[1]

def p_define(p):
  "define_stmt : VAR ID OP_EQUAL expression SEMICOLON"
  p[0] = DefineStmt(p[2], p[4])

def p_assign(p):
  "assign_stmt : ID OP_EQUAL expression SEMICOLON"
  p[0] = AssignStmt(p[1], p[3])

def p_while(p):
  "while_stmt : WHILE LPAREN expression RPAREN compound_statements"
  p[0] = WhileStmt(p[3], p[5])
  
def p_return_none(p):
  "return_stmt : RETURN SEMICOLON"
  p[0] = ReturnStmt()

def p_return(p):
  "return_stmt : RETURN expression SEMICOLON"
  p[0] = ReturnStmt(p[2])

def p_if(p):
  "if_stmt : IF LPAREN expression RPAREN compound_statements else_clause"
  p[0] = IfStmt(p[3], p[5], p[6])

def p_else_empty(p):
  "else_clause :"
  p[0] = None

def p_else(p):
  "else_clause : ELSE compound_statements"
  p[0] = p[2]

def p_compound_statements(p):
  "compound_statements : LBRACKET statements RBRACKET"
  p[0] = p[2]

def p_expression_bin_op(p):
  """expression : expression OP_PLUS expression
                | expression OP_MINUS expression
                | expression OP_TIMES expression
                | expression OP_DIVIDE expression
                | expression OP_GT expression
                | expression OP_GTEQ expression
                | expression OP_LT expression
                | expression OP_LTEQ expression
                | expression OP_EQ expression
  """
  p[0] = BinaryOp(p[2], p[1], p[3])

def p_expression_id(p):
  "expression : ID"
  p[0] = Identifier(p[1])

def p_term_factor(p):
  "expression : NUMBER"
  p[0] = Number(p[1])

def p_expression_expr(p):
  "expression : LPAREN expression RPAREN"
  p[0] = p[2]

def p_expression_func_call(p):
  """expression : function_call
                | function_decl
  """
  p[0] = p[1]

def p_func_call(p):
  "function_call : expression LPAREN arguments RPAREN"
  p[0] = FunctionCall(p[1], p[3])

def p_arguments_empty(p):
  "arguments :"
  p[0] = []

def p_arguments(p):
  "arguments : argument arguments_rest"
  p[0] = [p[1]] + p[2]

def p_arguments_rest(p):
  "arguments_rest : COMMA argument arguments_rest"
  p[0] = [p[2]] + p[3]

def p_arguments_rest_empty(p):
  "arguments_rest :"
  p[0] = []

def p_argument(p):
  "argument : expression"
  p[0] = p[1]

def p_func_decl(p):
  "function_decl : FUNCTION LPAREN parameters RPAREN compound_statements"
  p[0] = FunctionDecl(p[3], p[5])

def p_parameters(p):
  "parameters : parameter parameters_rest"
  p[0] = [p[1]] + p[2]

def p_parameters_rest(p):
  "parameters_rest : COMMA parameter parameters_rest"
  p[0] = [p[2]] + p[3]

def p_parameters_rest_empty(p):
  "parameters_rest :"
  p[0] = []

def p_parameter(p):
  "parameter : ID"
  p[0] = p[1]

precedence = (
    ('nonassoc', 'OP_GT', 'OP_GTEQ', 'OP_LT', 'OP_LTEQ', 'OP_EQ'),
    ('left', 'OP_PLUS', 'OP_MINUS'),
    ('left', 'OP_TIMES', 'OP_DIVIDE'),
    ('right', 'LPAREN') # to make function call possess higher precedence
)

def p_error(p):
    print "Syntax error with", p

# Build the parser
parser = yacc.yacc()

# while True:
   # try:
   #     s = raw_input('calc > ')
   # except EOFError:
   #     break
   # if not s:
   #     continue
