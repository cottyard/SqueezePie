import operator

def log(*obj):
  for o in obj:
    print o,

built_ins = {
  '+': operator.add,
  '-': operator.sub,
  '*': operator.mul,
  '/': operator.div,
  '>': operator.gt,
  '<': operator.lt,
  '>=': operator.ge,
  '<=': operator.le,
  '==': operator.eq,
  'log': log,
  'true': True,
  'false': False
}