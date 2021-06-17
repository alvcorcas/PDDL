from Action import *

A = Action("A", ['p2'], ['p4'])
B = Action("B", ['p4'], ['p5'])
C = Action("C", ['p6'], ['p5'])
D = Action("D", ['p1', 'p4', 'p5'], ['p3', 'p7'])

actions = [A, B, C, D]
print(actions)

def prego(state, targets):
    global actions
    result = []
    for target in targets:
        if target in state.literals:
            break

        elif not(target in action.effects for action in actions):
            result = result + actions

        else:
            heuristic = actions
            for action in actions:
                if target in action.effects and state.satisfy(action.preconditions):
                    temp = [action] + prego(state, (precondition for precondition in action.preconditions))
                    if len(temp) < len(heuristic):
                        heuristic = temp
            result = result + heuristic
    return result

