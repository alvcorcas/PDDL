class State:
    def __init__(self, literals):
        self.literals = literals

    def __eq__(self, other):
        return set(self.literals) == set(other.literals)

    def __repr__(self):
        return str(self.literals)

    def __str__(self):
        return str(self.literals)

    def satisfy(self, conditions):
        return all(c in self.literals for c in conditions)

    def apply(self, action):
        return State(list(set(self.literals) | action.effects))

    def disapply(self, action):
        return State(list(set(self.literals) - action.effects | action.preconditions))
