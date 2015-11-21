from parser import parser
import testcases
from environment import Environment
import builtin

for case, src in {
                   k: v for k, v in testcases.__dict__.items() if not k.startswith('__')
                 }.items():
  print '===', case, '==='
  ast = parser.parse(src)
  #print ast
  ast.execute(Environment(builtin.built_ins))
  print
