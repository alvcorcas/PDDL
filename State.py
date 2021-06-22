class State:
    def __init__(self, literals):
        self.literals = literals

    def __str__(self):
        return self.literals

    def __eq__(self, other):
        return self.literals == other.literals

    def satisfy(self, conditions):
        for condition in conditions:
            if not(condition in self.literals):
                return False
        return True

    def apply(self, action):
        return State(list(set(self.literals + action.effects)))

    def disapply(self, action):
        return State(list(set((self.literals - action.effects) + action.preconditions)))

    def __repr__(self):
        return self.literals
