class State:
    def __init__(self, literals):
        self.literals = literals

    def __str__(self):
        return str(self.literals)

    def __eq__(self, other):
        return all(literal in self.literals for literal in other.literals)

    def satisfy(self, conditions):
        return all(condition in self.literals for condition in conditions)

    def apply(self, action):
        temp = list(set(self.literals) | set(action.effects))
        return State(temp)

    def disapply(self, action):
        temp = list(set(self.literals) - set(action.effects)
                    | set(action.preconditions))
        return State(temp)

    def __repr__(self):
        return str(self.literals)
