import ply.lex as lex

reserved = {
    'while': 'WHILE',
    'var': 'VAR',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE'
}

tokens = [
   'ID',
   'OP_EQUAL',
   'OP_EQ',
   'OP_GT',
   'OP_GTEQ',
   'OP_LT',
   'OP_LTEQ',
   'OP_TIMES',
   'OP_MINUS',
   'OP_PLUS',
   'OP_DIVIDE',
   'NUMBER',
   'LPAREN',
   'RPAREN',
   'LBRACKET',
   'RBRACKET',
   'SEMICOLON',
   'COMMA'
] + list(reserved.values())

t_OP_PLUS    = r'\+'
t_OP_MINUS   = r'-'
t_OP_TIMES   = r'\*'
t_OP_DIVIDE  = r'/'
t_OP_EQUAL = r'='
t_OP_EQ = r'=='
t_OP_GT = r'>'
t_OP_GTEQ = r'>='
t_OP_LT = r'<'
t_OP_LTEQ = r'<='
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'//.*\n'


# ignored characters (spaces and tabs)
t_ignore  = ' \t'

# error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# compute column
def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = token.lexpos - last_cr - 1
    return column

lexer = lex.lex()

