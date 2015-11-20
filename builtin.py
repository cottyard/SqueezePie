def find(id):
    def plus(o1, o2):
      return o1 + o2

    def minus(o1, o2):
      return o1 - o2

    def times(o1, o2):
      return o1 * o2

    def divide(o1, o2):
      return o1 / o2

    def greater_than(o1, o2):
      return o1 > o2

    def log(*obj):
      for o in obj:
        print o,

    return {
      '+': plus,
      '-': minus,
      '*': times,
      '/': divide,
      '>': greater_than,
      'log': log
    }[id]
