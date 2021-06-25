class Action:
    def __init__(self, name, pos_preconditions, neg_preconditions, pos_effects, neg_effects):
        self.name = name
        self.pos_preconditions = pos_preconditions
        self.neg_preconditions = neg_preconditions
        self.pos_effects = pos_effects
        self.neg_effects = neg_effects

    def __repr__(self):
        result = self.name + "-"
        for p in self.pos_preconditions:
            result += (p + ' ')

        result = result[:-1]
        result += "-"

        for p in self.neg_preconditions:
            result += (p + ' ')

        result = result[:-1]
        result += "-"

        for e in self.pos_effects:
            result += (e + ' ')
        
        result = result[:-1]
        result += "-"

        for e in self.neg_effects:
            result += (e + ' ')
        
        result = result[:-1]
        result += ";"
        return result

    def __str__(self):
        result = self.name + "-"
        for p in self.pos_preconditions:
            result += (p + ' ')

        result = result[:-1]
        result += "-"

        for p in self.neg_preconditions:
            result += (p + ' ')

        result = result[:-1]
        result += "-"

        for e in self.pos_effects:
            result += (e + ' ')
        
        result = result[:-1]
        result += "-"

        for e in self.neg_effects:
            result += (e + ' ')
        
        result = result[:-1]
        result += ";"
        return result