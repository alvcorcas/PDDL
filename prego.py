from Action import *
from State import *
import numpy as np

# A = Action("A", ['p1'], ['p5'])
# B = Action("B", ['p4'], ['p2'])
# C = Action("C", ['p2'], ['p5'])
# D = Action("D", ['p1', 'p4', 'p5'], ['p3', 'p7'])


A = Action("A", ['p2'], ['p4'])
B = Action("B", ['p4'], ['p5'])
C = Action("C", ['p1'], ['p2'])
D = Action("D", ['p1', 'p4', 'p5'], ['p3'])
E = Action("E", ['p5', 'p2'], ['p3'])
F = Action("F", ['p1', 'p5'], ['p3'])

# A-p2-p4;B-p4-p5;C-p1-p2;D-p1,p4,p5-p3;E-p5,p2-p3;F-p1,p5-p3

actions = [A, B, C, D, E, F]
# print(actions)


def prego(state, targets, actions):
    result = []
    for target in targets:
        if target in state.literals:
            continue
        else:
            causes = [action for action in actions if target in action.effects]

            # Ninguna accion es causa del literal target
            if (len(causes) == 0):
                result = result + actions

            else:
                # Inicializo la heuristica como una lista con todas las acciones
                # y la voy sustituyendo por el conjunto de acciones con menor
                # cardinal que consigue el objetivo
                heuristic = actions
                for cause in causes:
                    temp = [cause] + prego(state, cause.preconditions, actions)
                    if len(temp) < len(heuristic):
                        heuristic = temp
                result = result + heuristic
    return result


def delta0(state, targets, actions):
    result = 0
    for target in targets:
        if target in state.literals:
            continue
        else:
            causes = [action for action in actions if target in action.effects]

            # Ninguna accion es causa del literal target
            if (len(causes) == 0):
                result = np.Infinity
                break

            else:
                # Inicializo la heuristica como una lista con todas las acciones
                # y la voy sustituyendo por el conjunto de acciones con menor
                # cardinal que consigue el objetivo
                heuristic = len(actions)
                for cause in causes:
                    temp = 1 + delta0(state, cause.preconditions, actions)
                    if temp < heuristic:
                        heuristic = temp
                result = result + heuristic
    return result


s = State(['p1'])
print(delta0(s, ['p5'], actions))


# DuDAD
# PReguntar la duda de si
