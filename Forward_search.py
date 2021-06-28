import Heuristics as heur

no_path = 'There is no path from initial state to target'


def forward_search_prego(initial_state, target, actions):
    return forward_search_prego_aux([], [], initial_state, target, actions)


def forward_search_prego_aux(path, visiteds, current, target, actions):
    if current.satisfy(target):
        return path

    applicable = [action for action in actions if
                  current.satisfy_preconditions(action) and current.apply(action) not in visiteds]

    sorted_applicable = sorted(applicable, key=lambda a: heur.prego(
        current.apply(a), target.literals, actions))

    for action in sorted_applicable:
        e = current.apply(action)
        result = forward_search_prego_aux(
            path + [action], visiteds + [e], e, target, actions)
        if result != no_path:
            return result
    return no_path


def forward_search_delta0(initial_state, target, actions):
    return forward_search_delta0_aux([], [], initial_state, target, actions)


def forward_search_delta0_aux(path, visiteds, current, target, actions):
    if current.satisfy(target):
        return path

    applicable = [action for action in actions if
                  current.satisfy_preconditions(action) and current.apply(action) not in visiteds]

    sorted_applicable = sorted(applicable, key=lambda a: heur.delta0(
        current.apply(a), target.literals, actions))

    for action in sorted_applicable:
        e = current.apply(action)
        result = forward_search_delta0_aux(
            path + [action], visiteds + [e], e, target, actions)
        if result != no_path:
            return result
    return no_path

def forward_search_blind(initial_state, target, actions):
    return forward_search_blind_aux([], [], initial_state, target, actions)


def forward_search_blind_aux(path, visiteds, current, target, actions):
    if current.satisfy(target):
        return path

    applicable = [action for action in actions if
                  current.satisfy_preconditions(action) and current.apply(action) not in visiteds]

    for action in applicable:
        e = current.apply(action)
        result = forward_search_blind_aux(
            path + [action], visiteds + [e], e, target, actions)
        if result != no_path:
            return result
    return no_path



