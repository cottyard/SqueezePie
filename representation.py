import runtime
from pie_excep import ReturnControl

class Program:
  def __init__(self, statements):
    self.statements = statements

  def execute(self, env):
    for s in self.statements:
      s.execute(env)


class DefineStmt:
  def __init__(self, var_id_literal, var_value_expr):
    self.var_id_literal = var_id_literal
    self.var_value_expr = var_value_expr

  def execute(self, env):
    env.set(self.var_id_literal, self.var_value_expr.evaluate(env))


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


class ReturnStmt:
  def __init__(self, expr=None):
    self.expr = expr

  def execute(self, env):
    raise ReturnControl(self.expr)


class Expression:
  def execute(self, env):
    self.evaluate(env)


class FunctionCall(Expression):
  def __init__(self, id, arguments):
    self.id = id
    self.arguments = arguments

  def evaluate(self, env):
    return runtime.apply(self.id, self.arguments, env)


class FunctionDecl(Expression):
  def __init__(self, params, body):
    self.params = params
    self.body = body

  def evaluate(self, env):
    return runtime.function(self.params, self.body)


class BinaryOp(Expression):
  def __init__(self, op, left, right):
    self.op = op
    self.left = left
    self.right = right

  def evaluate(self, env):
    return runtime.apply(self.op, [self.left, self.right], env)


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
