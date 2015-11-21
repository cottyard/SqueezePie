import runtime
from excep import ReturnControl


class Program:
  def __init__(self, statements):
    self.statements = statements

  def execute(self, env):
    for s in self.statements:
      s.execute(env)

  def __str__(self):
    return '\n'.join([str(s) for s in self.statements])


class Statement:
  def __repr__(self):
    return str(self)


class DefineStmt(Statement):
  def __init__(self, var_id_literal, var_value_expr):
    self.var_id_literal = var_id_literal
    self.var_value_expr = var_value_expr

  def execute(self, env):
    env.set(self.var_id_literal, self.var_value_expr.evaluate(env))

  def __str__(self):
    return 'var %s = %s' % (self.var_id_literal, str(self.var_value_expr))


class WhileStmt(Statement):
  def __init__(self, condition, statements):
    self.condition = condition
    self.statements = statements

  def execute(self, env):
    while self.condition.evaluate(env):
      for s in self.statements:
        s.execute(env)


class AssignStmt(Statement):
  def __init__(self, var_id_literal, var_value_expr):
    self.var_id_literal = var_id_literal
    self.var_value_expr = var_value_expr

  def execute(self, env):
    env.set(self.var_id_literal, self.var_value_expr.evaluate(env))


class ReturnStmt(Statement):
  def __init__(self, expr=None):
    self.expr = expr

  def execute(self, env):
    raise ReturnControl(self.expr)

  def __str__(self):
    return 'return %s' % str(self.expr)


class IfStmt(Statement):
  def __init__(self, cond_expr, statements, else_statements):
    self.cond_expr = cond_expr
    self.statements = statements
    self.else_statements = else_statements

  def execute(self, env):
    cond = self.cond_expr.evaluate(env)
    to_exec = self.statements if cond else self.else_statements
    if to_exec is None:
      return
    for s in to_exec:
      s.execute(env)
  
  def __str__(self):
    string = 'if (%s) {%s}' % (
      str(self.cond_expr), 
      '; '.join([str(s) for s in self.statements]))
    if self.else_statements is not None:
      string += ' else {%s}' % '; '.join([str(s) for s in self.else_statements])
    return string


class Expression:
  def execute(self, env):
    self.evaluate(env)

  def __repr__(self):
    return str(self)


class FunctionCall(Expression):
  def __init__(self, expr, arguments):
    self.expr = expr
    self.arguments = arguments

  def evaluate(self, env):
    function = self.expr.evaluate(env)
    return runtime.apply(function, self.arguments, env)

  def __str__(self):
    return '(%s)(%s)' % (
      str(self.expr),
      ', '.join([str(s) for s in self.arguments]))


class FunctionDecl(Expression):
  def __init__(self, params, body):
    self.params = params
    self.body = body

  def evaluate(self, env):
    return runtime.function(self.params, self.body, env)

  def __str__(self):
    return 'function(%s){%s}' % (
      ', '.join([str(p) for p in self.params]),
      '; '.join([str(s) for s in self.body]))


class BinaryOp(Expression):
  def __init__(self, op, left, right):
    self.op = op
    self.left = left
    self.right = right

  def evaluate(self, env):
    return runtime.apply(env.lookup(self.op), [self.left, self.right], env)

  def __str__(self):
    return '%s %s %s' % (
      str(self.left), self.op , str(self.right))


class Identifier(Expression):
  def __init__(self, id):
    self.id = id

  def evaluate(self, env):
    return env.lookup(self.id)

  def __str__(self):
    return self.id

class Number(Expression):
  def __init__(self, num):
    self.num = num

  def evaluate(self, env):
    return self.num

  def __str__(self):
    return str(self.num)

