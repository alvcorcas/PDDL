class State:
    def __init__(self, literals):
        self.literals = literals

    def __eq__(self, other):
        return all(o in self.literals for o in other.literals)

    def __repr__(self):
        return str(self.literals)

    def __str__(self):
        return str(self.literals)

    def satisfy(self, conditions):
        return all(c in self.literals for c in conditions)

    def apply(self, action):
        temp = list(set(self.literals) | action.effects)
        return State(temp)

    def disapply(self, action):
        temp = list(set(self.literals) - action.effects | action.preconditions)
        return State(temp)