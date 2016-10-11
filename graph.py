class Edge:
    def __init__(self, nodes, name, avg_distance, direction):
        self.nodes = nodes if nodes is not None else []
        self.name = name
        self.avg_distance = avg_distance
        self.direction = direction

    def message(self, a, b):
        return "walk along the " + str(self.name) + " to " + str(b.name) + "."

    def __repr__(self):
        return str(self.nodes)

    def add_nodes(self, nodes):
        if type(nodes) is not list:
            nodes = [nodes]
        self.nodes += nodes

    def dist_between(self, a, b):
        return abs(self.nodes.index(a) - self.nodes.index(b)) * self.avg_distance

    def path_sign(self, a, b):
        return 1 if self.nodes.index(a) > self.nodes.index(b) else 0


class Node:
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges[:]

    def add_edge(self, edge):
        self.edges.append(edge)

    def __repr__(self):
        return str(self.name)


def make_edge(a, b, edge):
    if a is not None:
        a.edges.append(edge)
        edge.nodes.insert(0, a)
    if b is not None:
        b.edges.append(edge)
        edge.nodes.append(b)
