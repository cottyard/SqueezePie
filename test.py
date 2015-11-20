from parser import parser
import testcases
from environment import Environment

for case, src in {
                   k: v for k, v in testcases.__dict__.items() if not k.startswith('__')
                 }.items():
  parser.parse(src).execute(Environment())