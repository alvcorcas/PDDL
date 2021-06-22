class State:
    def __init__(self, literals):
        self.literals = literals

    def __str__(self):
        return str(self.literals)

    def __eq__(self, other):
        return self.literals == other.literals

    def satisfy(self, conditions):
        for condition in conditions:
            if not(condition in self.literals):
                return False
        return True

    def apply(self, action):
        temp = list(set(self.literals) | set(action.effects))
        return State(temp)

    def disapply(self, action):
        temp = list(set(self.literals) - set(action.effects) | set(action.preconditions))
        return State(temp)

    def __repr__(self):
        return str(self.literals)
