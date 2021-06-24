from Action import *
from State import *
import numpy as np

def prego(state, targets, actions):
    return len(prego_aux(state, targets, actions))

def prego_aux(state, targets, actions):
    result = []
    for target in targets:
        if target not in state.literals:
            causes = {action for action in actions if target in action.effects}

            if (len(causes) == 0):
                result += actions

            else:
                heuristic = [
                    [cause] + prego_aux(state, cause.preconditions, actions) for cause in causes]
                result += min(heuristic, key=lambda x: len(x))
    return result


def delta0(state, targets, actions):
    result = 0
    for target in targets:
        if target not in state.literals:
            causes = {action for action in actions if target in action.effects}

            if (len(causes) == 0):
                result += np.Infinity

            else:
                heuristic = {
                    1 + delta0(state, cause.preconditions, actions) for cause in causes}
                result += min(heuristic)
    return result
