class Action:
    def __init__(self, name, pos_preconditions, neg_preconditions, pos_effects, neg_effects):
        self.name = name
        self.pos_preconditions = pos_preconditions
        self.neg_preconditions = neg_preconditions
        self.pos_effects = pos_effects
        self.neg_effects = neg_effects

    def __repr__(self):
        # result = "\nName: " + self.name + "\nPreconditions:"
        # for p in self.pos_preconditions:
        #     temp = "\n\t" + p
        #     result += temp

        # for p in self.neg_preconditions:
        #     temp = "\n\t-" + p
        #     result += temp

        # result += "\nEffects:"

        # for e in self.pos_effects:
        #     temp = "\n\t" + e
        #     result += temp

        # for e in self.neg_effects:
        #     temp = "\n\t-" + e
        #     result += temp
        result = self.name
        return result
