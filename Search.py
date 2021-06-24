import Heuristics as heur

no_path = 'There is no path from initial state to target'

def forward_search_prego(initial_state, target, actions):
    return forward_search_prego_aux([], [], initial_state, target, actions)

def forward_search_prego_aux(path, visited, current, target, actions):
    if current.satisfy(target.literals):
        return path

    applicable = [action for action in actions if
                  current.satisfy(action.preconditions) and current.apply(action) not in visited]

    sorted_applicable = sorted(applicable, key=lambda a: heur.prego(
        current.apply(a), target.literals, actions)) 

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
    if current.satisfy(target.literals):
        return path

    applicable = [action for action in actions if
                  current.satisfy(action.preconditions) and current.apply(action) not in visited]

    sorted_applicable = sorted(applicable, key=lambda a: heur.delta0(
        current.apply(a), target.literals, actions))

    for action in sorted_applicable:
        e = current.apply(action)
        result = forward_search_delta0_aux(
            path + [action], visited + [e], e, target, actions)
        if result:
            return result
    return no_path


def backward_search_prego(initial_state, target, actions):
    return backward_search_prego_aux([], [], initial_state, target, actions)

def backward_search_prego_aux(path, visited, initial_state, current, actions):
    if initial_state == current:
        return path

    relevants = [action for action in actions if current.satisfy(
        action.effects) and current.disapply(action) not in visited]

    sorted_relevants = sorted(relevants, key=lambda a: heur.prego(
        initial_state, current.disapply(a).literals,  actions))

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
    if initial_state == current:
        return path

    relevants = [action for action in actions if
                 current.satisfy(action.effects) and current.disapply(action) not in visited]

    sorted_relevants = sorted(relevants, key=lambda a: heur.delta0(
        initial_state, current.disapply(a).literals, actions))

    for action in sorted_relevants:
        e = current.disapply(action)
        result = backward_search_delta0_aux(
            [action] + path, visited + [e], initial_state, e, actions)
        if result:
            return result
    return no_path
