import ply.yacc as yacc
import testcases
from lexer import tokens

def p_program(p):
  "program : statements"
  p[0] = p[1]

def p_statements(p):
  "statements : statements statement"
  p[0] = p[2]

def p_empty_statements(p):
  "statements :"
  pass

def p_statement(p):
  """statement : while_stmt
               | define_stmt
               | assign_stmt"""
  p[0] = p[1]

def p_define(p):
  "define_stmt : VAR ID OP_EQUAL NUMBER SEMICOLON"
  p[0] = ' '.join([p[1], p[2], p[3], str(p[4]), p[5]])

def p_assign(p):
  "assign_stmt : ID OP_EQUAL expression SEMICOLON"
  p[0] = p[2]

def p_while(p):
  "while_stmt : WHILE LPAREN expression RPAREN compound_statements"
  print 'while'
  
def p_compound_statements(p):
  "compound_statements : LBRACKET statements RBRACKET"

def p_expression_bin_op(p):
  # "expression : expression binary_op expression"
  """expression : expression OP_PLUS expression
                | expression OP_MINUS expression
                | expression OP_TIMES expression
                | expression OP_DIVIDE expression
                | expression OP_GT expression
  """
  print p[2]

def p_expression_id(p):
  "expression : ID"

def p_term_factor(p):
  "expression : NUMBER"
  p[0] = p[1]

def p_expression_expr(p):
  "expression : LPAREN expression RPAREN"
  p[0] = p[2]

# def p_binary_op(p):
#   """binary_op : OP_PLUS
#                | OP_MINUS
#                | OP_TIMES
#                | OP_DIVIDE
#                | OP_GT"""
#   p[0] = p[1]
#   print p[1]

precedence = (
    ('left', 'OP_GT'),
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