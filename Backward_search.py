import Heuristics as heur

no_path = 'There is no path from initial state to target'


def backward_search_prego(initial_state, target, actions):
    return backward_search_prego_aux([], [], initial_state, target, actions)


def backward_search_prego_aux(path, visiteds, initial_state, current, actions):
    if initial_state.satisfy(current):
        return path

    relevants = [action for action in actions if current.is_relevant(
        action) and current.disapply(action).not_contains_any_in(visiteds)]

    sorted_relevants = sorted(relevants, key=lambda a: heur.prego(
        initial_state, current.disapply(a).literals,  actions))

    for action in sorted_relevants:
        e = current.disapply(action)
        result = backward_search_prego_aux(
            [action] + path, visiteds + [e], initial_state, e, actions)
        if result != no_path:
            return result
    return no_path


def backward_search_delta0(initial_state, target, actions):
    return backward_search_delta0_aux([], [], initial_state, target, actions)


def backward_search_delta0_aux(path, visiteds, initial_state, current, actions):
    if initial_state.satisfy(current):
        return path

    relevants = [action for action in actions if
                 current.is_relevant(action) and current.disapply(action).not_contains_any_in(visiteds)]

    sorted_relevants = sorted(relevants, key=lambda a: heur.delta0(
        initial_state, current.disapply(a).literals, actions))

    for action in sorted_relevants:
        e = current.disapply(action)
        result = backward_search_delta0_aux(
            [action] + path, visiteds + [e], initial_state, e, actions)
        if result != no_path:
            return result
    return no_path


def backward_search_blind(initial_state, target, actions):
    return backward_search_blind_aux([], [], initial_state, target, actions)


def backward_search_blind_aux(path, visiteds, initial_state, current, actions):
    if initial_state.satisfy(current):
        return path

    relevants = [action for action in actions if
                 current.is_relevant(action) and current.disapply(action).not_contains_any_in(visiteds)]

    for action in relevants:
        e = current.disapply(action)
        result = backward_search_blind_aux(
            [action] + path, visiteds + [e], initial_state, e, actions)
        if result != no_path:
            return result
    return no_path
