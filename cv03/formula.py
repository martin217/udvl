

class Formula:
    def __init__(self, subformulas):
        self.sub = subformulas
    def eval(self, i):
        pass
    def toString(self):
        pass
    def subf(self):
        return self.sub

class Variable(Formula):
    def __init__(self, name):
        Formula.__init__(self, [])
        self.name = name
    def eval(self, i):
        return i[self.name]
    def toString(self):
        return self.name

class Negation(Formula):
    def __init__(self, orig):
        Formula.__init__(self, [orig])
    def originalFormula(self):
        return self.subf()[0]
    def eval(self, i):
        return not self.originalFormula().eval(i)
    def toString(self):
        return "-" + self.originalFormula().toString()

class Conjunction(Formula):
    def __init__(self, orig):
        Formula.__init__(self,orig)
    def eval(self, i):
        for formula in self.subf():
            if not formula.eval(i):
                return False
        return True
    def toString(self):
        return "(" + "&".join([formula.toString() for formula in self.subf()]) + ")"
    
    
class Implication(Formula):
    def __init__(self, left, right):
        Formula.__init__(self, [left,right])
    def rightSide(self):
        return self.subf()[1]
    def leftSide(self):
        return self.subf()[0]
    def eval(self, i):
        right = self.rightSide().eval(i)
        left = self.leftSide().eval(i)
        if left and not right:
            return False
        return True
    def toString(self):
        return "(" + self.leftSide().toString() + "=>" + self.rightSide().toString() + ")"
    
class Disjunction(Formula):
    def __init__(self, orig):
        Formula.__init__(self, orig)
    def eval(self, i):
        for formula in self.subf():
            if formula.eval(i):
                return True
        return False
    def toString(self):
        return "(" + "|".join([formula.toString() for formula in self.subf()]) + ")"

class Equivalence(Formula):
    def __init__(self, left, right):
        Formula.__init__(self, [left,right])
    def rightSide(self):
        return self.subf()[1]
    def leftSide(self):
        return self.subf()[0]
    def eval(self, i):
        right = self.rightSide().eval(i)
        left = self.leftSide().eval(i)
        if right == left:
            return True
        return False
    def toString(self):
        return "(" + self.leftSide().toString() + "<=>" + self.rightSide().toString() + ")"

