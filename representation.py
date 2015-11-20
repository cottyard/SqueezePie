from apply import apply

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
  def execute(self, env):
    self.evaluate(env)


class FunctionCall(Expression):
  def __init__(self, id, arguments):
    self.id = id
    self.arguments = arguments

  def evaluate(self, env):
    return apply(self.id, self.arguments, env)


class BinaryOp(Expression):
  def __init__(self, op, left, right):
    self.op = op
    self.left = left
    self.right = right

  def evaluate(self, env):
    return apply(self.op, [self.left, self.right], env)


class Identifier(Expression):
  def __init__(self, id):
    self.id = id

  def evaluate(self, env):
    return env.lookup(self.id)


class Number(Expression):
  def __init__(self, num):
    self.num = num

  def evaluate(self, env):
    return self.num
