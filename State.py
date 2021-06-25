class State:
    def __init__(self, literals):
        self.literals = literals

    def __eq__(self, other):
        result = set(self.literals) == set(other.literals)
        return result

    def __repr__(self):
        return str(self.literals)

    def __str__(self):
        return str(self.literals)

    def satisfy(self, other):
        return all(l in self.literals for l in other.literals)

    def satisfy_preconditions(self, action):
        satisfy_pos_preconditions = all(
            p in self.literals for p in action.pos_preconditions) or len(action.pos_preconditions) == 0
        satisfy_neg_preconditions = all(
            n not in self.literals for n in action.neg_preconditions) or len(action.neg_preconditions) == 0

        print(len(action.neg_preconditions))

        return satisfy_pos_preconditions and satisfy_neg_preconditions

    def apply(self, action):
        literals = list(set(self.literals) -
                        action.neg_effects | action.pos_effects)

        return State(literals)

    def is_relevant(self, action):
        contains_any_pos_effects = any(
            p in self.literals for p in action.pos_effects) or len(action.neg_effects) == 0

        contains_any_neg_effects = any(
            n not in self.literals for n in action.neg_effects) or len(action.neg_effects) == 0

        pos_contains_neg = all(
            n in self.literals for n in action.neg_effects) or len(action.neg_effects) == 0

        neg_contains_pos = not any(
            p not in self.literals for p in action.pos_effects) or len(action.pos_effects) == 0

        result = (contains_any_pos_effects or contains_any_neg_effects) and (
            pos_contains_neg and neg_contains_pos)

        return result

    def disapply(self, action):
        literals = list(set(self.literals) -
                        action.pos_effects | action.pos_preconditions)

        return State(literals)

    def not_contains_any_in(self, visiteds):
        for visited in visiteds:
            if all(v in self.literals for v in visited.literals):
                return False
        return True
