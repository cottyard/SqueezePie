import ply.yacc as yacc
import testcases
from lexer import tokens

def p_define(p):
  "define : VAR ID OP_EQUAL NUMBER SEMICOLON"
  p[0] = p[1] + p[2] + p[3] + str(p[4]) + p[5]
  
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