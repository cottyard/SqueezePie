import builtin
from excep import ReturnControl

def apply(function, arguments, env):
  if is_builtin_func(function):
    return apply_builtin(function, arguments, env)

  # evaluate the arguments in the current environment
  args_value = [a.evaluate(env) for a in arguments]

  # when running the function, use the closure of that function as env
  params, body, env = function

  # print '===apply==='
  # print str(params)
  # print '; '.join([str(s) for s in body])
  # print str(env)

  env = env.nested()

  for p, a in zip(params, args_value):
    env.set(p, a)
    # print 'setting param', p, 'to', a
  
  # print '==========='

  try:
    for stmt in body:
      stmt.execute(env)
  except ReturnControl as rc:
    return rc.expr.evaluate(env)

def apply_builtin(builtin_func, arguments, env):
  # print '===apply builtin ==='
  # print builtin_func
  # print arguments
  # print env
  # print '===================='

  return builtin_func(*[a.evaluate(env) for a in arguments])

def function(params, body, env):
  return (params, body, env)

def is_builtin_func(function):
  return not isinstance(function, tuple)