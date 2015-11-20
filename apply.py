import builtin

def apply(id, arguments, env):
  args = [a.evaluate(env) for a in arguments]
  return builtin.find(id)(*args)
