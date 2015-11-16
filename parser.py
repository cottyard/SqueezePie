import ply.yacc as yacc
import testcases
from lexer import tokens
from environment import Environment
from representation import *

global_env = Environment()

def p_program(p):
  "program : statements"
  p[0] = Program(p[1])

def p_statements(p):
  "statements : statements statement"
  p[1].append(p[2])
  p[0] = p[1]

def p_empty_statements(p):
  "statements :"
  p[0] = []

def p_statement(p):
  """statement : while_stmt
               | define_stmt
               | assign_stmt"""
  p[0] = p[1]

def p_define(p):
  "define_stmt : VAR ID OP_EQUAL NUMBER SEMICOLON"
  p[0] = DefineStmt(p[2], p[4])

def p_assign(p):
  "assign_stmt : ID OP_EQUAL expression SEMICOLON"
  p[0] = AssignStmt(p[1], p[3])

def p_while(p):
  "while_stmt : WHILE LPAREN expression RPAREN compound_statements"
  p[0] = WhileStmt(p[3], p[5])
  
def p_compound_statements(p):
  "compound_statements : LBRACKET statements RBRACKET"
  p[0] = p[2]

def p_expression_bin_op(p):
  """expression : expression OP_PLUS expression
                | expression OP_MINUS expression
                | expression OP_TIMES expression
                | expression OP_DIVIDE expression
                | expression OP_GT expression
  """
  p[0] = BinaryOpExpr(p[2], p[1], p[3])

def p_expression_id(p):
  "expression : ID"
  p[0] = IdentifierExpr(p[1])

def p_term_factor(p):
  "expression : NUMBER"
  p[0] = NumberExpr(p[1])

def p_expression_expr(p):
  "expression : LPAREN expression RPAREN"
  p[0] = p[2]

precedence = (
    ('nonassoc', 'OP_GT'),
    ('left', 'OP_PLUS', 'OP_MINUS'),
    ('left', 'OP_TIMES', 'OP_DIVIDE'),
)

#def p_error(p):
    #print("Syntax error in input!")
#    pass


# Build the parser
parser = yacc.yacc()

# while True:
   # try:
   #     s = raw_input('calc > ')
   # except EOFError:
   #     break
   # if not s:
   #     continue
result = parser.parse(testcases.data)
print(result)
result.execute(global_env)
print(global_env)