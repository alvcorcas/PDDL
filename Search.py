from Heuristics import *

no_path = 'There is no path from initial state to target'

def forward_search_prego(initial_state, target, actions):
    return forward_search_prego_aux([], [], initial_state, target, actions)


def forward_search_prego_aux(path, visited, current, target, actions):
    if current.satisfy(target):
        return path

    applicable = [action for action in actions if (
        (current.satisfy(action.preconditions)) and (current.apply(action) not in visited))]

    sorted_applicable = sorted(applicable, key=lambda a: prego(
        current.apply(a), target, actions))

    for action in sorted_applicable:
        e = current.apply(action)
        result = forward_search_prego_aux(
            path + [action], visited + [e], e, target, actions)
        if result:
            return result
    return no_path


def forward_search_delta0(initial_state, target, actions):
    return forward_search_delta0_aux([], [], initial_state, target, actions)


def forward_search_delta0_aux(path, visited, current, target, actions):
    if current.satisfy(target):
        return path

    applicable = [action for action in actions if (
        (current.satisfy(action.preconditions)) and (current.apply(action) not in visited))]

    sorted_applicable = sorted(applicable, key=lambda a: delta0(
        current.apply(a), target, actions))

    for action in sorted_applicable:
        e = current.apply(action)
        result = forward_search_delta0_aux(
            path + [action], visited + [e], e, target, actions)
        if result:
            return result
    return no_path

#p1,p3,p4,p9
# p10,p11,p21

# A-p6-p18,p8;
# B-p4-p20,p14,p16;
# C-p18,p20-p5;
# D-p7,p3-p6;
# E-p1-p7,p2;
# F-p5-p10,p13;
# G-p9,p13,p12-p11,p19;
# H-p14,p8-p12;
# I-p2,p19,p16-p15;
# J-p15-p21


def backward_search_prego(initial_state, target, actions):
    return backward_search_prego_aux([], [], initial_state, target, actions)


def backward_search_prego_aux(path, visited, initial_state, current, actions):
    if current.satisfy(initial_state):
        return path

    relevants = [action for action in actions if (
        (current.satisfy(action.effects)) and (current.disapply(action) not in visited))]

    sorted_relevants = sorted(relevants, key=lambda a: prego(
        current.disapply(a), initial_state, actions))

    for action in sorted_relevants:
        e = current.disapply(action)
        result = backward_search_prego_aux(
           [action] + path, visited + [e], initial_state, e, actions)
        if result:
            return result
    return no_path


def backward_search_delta0(initial_state, target, actions):
    return backward_search_delta0_aux([], [], initial_state, target, actions)


def backward_search_delta0_aux(path, visited, initial_state, current, actions):
    if current.satisfy(initial_state):
        return path

    relevants = [action for action in actions if (
        (current.satisfy(action.effects)) and (current.disapply(action) not in visited))]

    sorted_relevants = sorted(relevants, key=lambda a: delta0(
        current.disapply(a), initial_state, actions))

    for action in sorted_relevants:
        e = current.disapply(action)
        result = backward_search_delta0_aux(
           [action] + path, visited + [e], initial_state, e, actions)
        if result:
            return result
    return no_path


# Acciones relevantes:
# En el planteamiento de la teoria hay un fallo:
# D = Accion("D",[p1,p4],[p5,p3])