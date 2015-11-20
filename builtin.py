def find(id):
    def times(o1, o2):
      return o1 * o2

    def minus(o1, o2):
      return o1 - o2

    def greater_than(o1, o2):
      return o1 > o2

    def log(*obj):
      for o in obj:
        print o,

    return {
      '*': times,
      '-': minus,
      '>': greater_than,
      'log': log
    }[id]
