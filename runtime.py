import builtin
from pie_excep import PieUnresolvedSymbol, ReturnControl

def apply(id, arguments, env):
  try:
    params, body = env.lookup(id)
  except PieUnresolvedSymbol:
    return builtin.find(id)(*[a.evaluate(env) for a in arguments])

  env = env.nested()
  for p, a in zip(params, arguments):
    env.set(p, a.evaluate(env))
  
  try:
    for stmt in body:
      stmt.execute(env)
  except ReturnControl as rc:
    return rc.expr.evaluate(env)
  

def function(params, body):
  return (params, body)
