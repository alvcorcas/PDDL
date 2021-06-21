from Heuristics import *


def forward_search(initial_state, target, actions):
    return forward_search_aux([], [], initial_state, target, actions)

def forward_search_aux(path, visited, current, target, actions):
    if current.satisfy(target):
        return path

    applicable  = [action for action in actions if (
        (current.satisfy(action.preconditions)) and (current.apply(action) not in visited))]

    sorted_applicable = sorted(applicable , key=lambda a: prego(
        current.apply(a), target, actions))

    for action in sorted_applicable:
        e = current.apply(action)
        result = forward_search_aux(
            path + [action], visited + [e], e, target, actions)
        if result:
            return result
    return 'There is no path from initial state to target'



# A-p6-p18,p8;
# B-p4-p20,p14,p16;
# C-p18,p20-p5;
# D-p7,p3-p6;
# E-p1-p7,p2;
# F-p5-p10,p13;
# G-p9,p13,p12-p11,p19;
# H-p14,p8-p12;I-p2,p19,p16-p15;
# J-p15-p21