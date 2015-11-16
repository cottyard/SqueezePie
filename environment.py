class Environment:
    def __init__(self, dict={}, parent=None):
        self.env = dict
        self.parent = parent

    def lookup(self, symbol):
        return self.find_env(symbol)[symbol]

    def find_env(self, symbol):
        if symbol in self.env:
            return self.env
        else:
            if self.parent is None:
                raise PieUnresolvedSymbolError(symbol)
            return self.parent.find_env(symbol)

    def set(self, name, value):
        self.env[name] = value

    def nested(self):
        return Environment({}, self)

    def __str__(self):
        return str(self.env)
