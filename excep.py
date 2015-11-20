class PieException(Exception):
  pass

class PieControl(PieException):
  pass

class PieUnresolvedSymbol(PieException):
  pass

class ReturnControl(PieControl):
  def __init__(self, expr):
    self.expr = expr