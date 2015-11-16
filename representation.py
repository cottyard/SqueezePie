class Program:
  def __init__(self, statements):
    self.statements = statements

  def execute(self, env):
    for s in self.statements:
      s.execute(env)


class DefineStmt:
  def __init__(self, var_id_literal, var_value):
    self.var_id_literal = var_id_literal
    self.var_value = var_value

  def execute(self, env):
    env.set(self.var_id_literal, self.var_value)


class WhileStmt:
  def __init__(self, condition, statements):
    self.condition = condition
    self.statements = statements

  def execute(self, env):
    while self.condition.evaluate(env):
      for s in self.statements:
        s.execute(env)


class AssignStmt:
  def __init__(self, var_id_literal, var_value_expr):
    self.var_id_literal = var_id_literal
    self.var_value_expr = var_value_expr

  def execute(self, env):
    env.set(self.var_id_literal, self.var_value_expr.evaluate(env))


class Expression:
  pass


class BinaryOpExpr(Expression):
  def __init__(self, op, left, right):
    self.op = op
    self.left = left
    self.right = right

  def find_impl(self, op):
    def times(o1, o2):
      return o1 * o2

    def minus(o1, o2):
      return o1 - o2

    def greater_than(o1, o2):
      return o1 > o2

    return {
      '*': times,
      '-': minus,
      '>': greater_than
    }[op]

  def evaluate(self, env):
    return self.find_impl(self.op)(
      self.left.evaluate(env), 
      self.right.evaluate(env))


class IdentifierExpr(Expression):
  def __init__(self, id):
    self.id = id

  def evaluate(self, env):
    return env.lookup(self.id)


class NumberExpr(Expression):
  def __init__(self, num):
    self.num = num

  def evaluate(self, env):
    return self.num
