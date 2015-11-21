from parser import parser
from environment import Environment
import builtin
import traceback

prompt = 'pie > '

def read_input():
    src = raw_input(prompt)
    if not src.endswith(';'):
        src += ';'
    return src

global_env = Environment(builtin.built_ins)

def repl():
    while True:
        source = read_input()
        try:
            ast = parser.parse(source)
            if ast is None:
                continue
            value = ast.execute(global_env)
        except Exception:
            print traceback.format_exc()
        else:
            if value is not None:
                print value

repl()