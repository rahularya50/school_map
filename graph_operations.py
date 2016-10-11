import str_utils


def path_finder(start_node, end_node):
    explored = {}
    to_explore = {start_node: (0, [])}

    while to_explore:
        current_node = min(to_explore.keys(), key=lambda x: to_explore[x][0])
        current_dist = to_explore[current_node][0]
        current_path = to_explore[current_node][1]
        del to_explore[current_node]
        explored[current_node] = current_path
        if current_node == end_node:
            break
        for edge in current_node.edges:
            for node in edge.nodes:
                if node not in explored and (
                        node not in to_explore or to_explore[node][0] > current_dist + edge.dist_between(current_node,
                                                                                                         node)):
                        to_explore[node] = (current_dist + edge.dist_between(current_node, node),
                                            current_path + [(current_node, edge)])

    return explored[end_node] + [(end_node, None)]


def gen_desc(path):
    output = []

    for i, move in enumerate(path):
        if move[1] is None:
            output.append("You have arrived!")
            break
        if i == 0:
            prefix = ""
        else:
            edge = move[1]
            prev_edge = path[i-1][1]
            node = move[0]
            prev_node = path[i-1][0]
            next_node = path[i+1][0]

            sign = edge.path_sign(node, next_node)
            prev_sign = prev_edge.path_sign(prev_node, node)

            direction = edge.direction + 2*sign
            prev_direction = prev_edge.direction + 2*prev_sign

            from elements import Staircase
            if isinstance(prev_edge, Staircase):
                prev_direction += 2

            prefix = str_utils.dir_gen(prev_direction, direction)

        output.append(prefix + str_utils.message(path[i][0], path[i+1][0], move[1]))

    output = list(i[0].upper() + i[1:] for i in output)
    return output
