from Action import *
from State import *

# A = Action("A", ['p1'], ['p5'])
# B = Action("B", ['p4'], ['p2'])
# C = Action("C", ['p2'], ['p5'])
# D = Action("D", ['p1', 'p4', 'p5'], ['p3', 'p7'])


A = Action("A", ['p2'], ['p4'])
B = Action("B", ['p4'], ['p5'])
C = Action("C", ['p1'], ['p2'])
D = Action("D", ['p1', 'p4', 'p5'], ['p3'])
E = Action("E", ['p5', 'p2'], ['p3'])
F = Action("F", ['p1','p5'], ['p3'])

#A-p2-p4;B-p4-p5;C-p1-p2;D-p1,p4,p5-p3;E-p5,p2-p3;F-p1,p5-p3

actions = [A, B, C, D,E,F]
#print(actions)

def prego(state, targets,actions):
    #global actions
    result = []
    for target in targets:
        if target in state.literals:
            continue

        elif not(target in action.effects for action in actions):
            result = result + actions

        else:
            heuristic = actions
            for action in actions:
                if target in action.effects:
                    temp = [action] + prego(state, action.preconditions,actions)
                    if len(temp) < len(heuristic):
                        heuristic = temp
            result = result + heuristic
    return result

print(prego(State(["p1"]),["p3"],actions))