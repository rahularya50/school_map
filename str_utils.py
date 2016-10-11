def message(start, end, edge):
    from elements import StairJunction, Staircase, InvisibleNode
    if isinstance(edge, Staircase):
        return edge.message(start, end)
    elif isinstance(end, InvisibleNode):
        return "walk all the way along the " + edge.name + "."
    elif isinstance(start, StairJunction):
        return "walk along the " + edge.name + " from the staircase to " + end.name + "."
    elif isinstance(end, StairJunction):
        return "walk along the " + edge.name + " to the staircase."
    else:
        return edge.message(start, end)


def dir_gen(old_dir, new_dir):
    delta = (new_dir - old_dir + 4) % 4
    if delta == 0:
        return ""
    elif delta == 1:
        return "Turn right, and "
    elif delta == 2:
        return "Turn around, and "
    elif delta == 3:
        return "Turn left, and "


# TODO: Rewrite - copyright issues?
def ordinal(n):
    if 10 <= (n % 100) <= 20:
        out = 'th'
    else:
        out = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + out
