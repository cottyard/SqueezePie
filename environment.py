from excep import PieUnresolvedSymbol

class Environment:
    def __init__(self, init_dict={}, parent=None):
        self.env = init_dict
        self.parent = parent

    def lookup(self, symbol):
        return self.find_env(symbol)[symbol]

    def find_env(self, symbol):
        # print 'looking up', symbol, 'in', str(self)
        if symbol in self.env:
            return self.env
        else:
            if self.parent is None:
                raise PieUnresolvedSymbol(symbol)
            return self.parent.find_env(symbol)

    def set(self, name, value):
        self.env[name] = value

    def nested(self):
        return Environment({}, self)

    def __str__(self):
        if self.parent is None:
            return '<top-level env>'
        return str(self.env)

    def __repr__(self):
        return str(self)