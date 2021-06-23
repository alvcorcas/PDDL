from Action import *
from State import *
import numpy as np

def prego(state, targets, actions):
    result = 0
    for target in targets:
        if target not in state.literals:
            causes = {action for action in actions if target in action.effects}

            # Ninguna accion es causa del literal target
            if (len(causes) == 0):
                result += len(actions)

            else:
                heuristic = np.Infinity
                for cause in causes:
                    temp = 1 + prego(state, cause.preconditions, actions)
                    if temp < heuristic:
                        heuristic = temp
                result += heuristic
    return result

def delta0(state, targets, actions):
    result = 0
    for target in targets:
        if target not in state.literals:
            causes = {action for action in actions if target in action.effects}

            # Ninguna accion es causa del literal target
            if (len(causes) == 0):
                result += np.Infinity

            else:
                heuristic = np.Infinity
                for cause in causes:
                    temp = 1 + delta0(state, cause.preconditions, actions)
                    if temp < heuristic:
                        heuristic = temp
                result += heuristic
    return result

