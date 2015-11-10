import ply.lex as lex

# List of token names.   This is always required
reserved = {
    'while': 'WHILE'
}

tokens = [
   'ID',
   'OP_EQUAL',
   'OP_GT',
   'OP_TIMES',
   'OP_MINUS',
   'OP_PLUS',
   'OP_DIVIDE',
   'NUMBER',
   'LPAREN',
   'RPAREN',
   'LBRACKET',
   'RBRACKET',
   'SEMICOLON'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_OP_PLUS    = r'\+'
t_OP_MINUS   = r'-'
t_OP_TIMES   = r'\*'
t_OP_DIVIDE  = r'/'
t_OP_EQUAL = r'='
t_OP_GT = r'>'
t_SEMICOLON = r';'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
n = 5;
p = 1;
while(n > 0)
{
  p = p * n;
  n = n - 1;
}
'''

# Give the lexer some input
lexer.input(data)

# Compute column
def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = token.lexpos - last_cr - 1
    return column

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print tok, find_column(data, tok)
