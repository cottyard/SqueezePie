import operator

def find(id):
    def log(*obj):
      for o in obj:
        print o,

    return {
      '+': operator.add,
      '-': operator.sub,
      '*': operator.mul,
      '/': operator.div,
      '>': operator.gt,
      '<': operator.lt,
      '>=': operator.ge,
      '<=': operator.le,
      'log': log,
      'true': True,
      'false': False
    }[id]
