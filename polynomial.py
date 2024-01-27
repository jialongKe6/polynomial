class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        def add_parentheses(expr):
            return '(' + repr(expr) + ')' if isinstance(expr, (Add, Sub, Div)) else repr(expr)

        p1_repr = add_parentheses(self.p1)
        p2_repr = add_parentheses(self.p2)

        return p1_repr + " * " + p2_repr
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        # Add parentheses around operands if they are instances of Add or Sub
        p1_repr = '(' + repr(self.p1) + ')' if isinstance(self.p1, (Add, Sub)) else repr(self.p1)
        p2_repr = '(' + repr(self.p2) + ')' if isinstance(self.p2, (Add, Sub)) else repr(self.p2)
        return p1_repr + " / " + p2_repr

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)