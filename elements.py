import graph
import str_utils


class Staircase(graph.Edge):
    def __init__(self, name, floors, direction):
        graph.Edge.__init__(self, None, name, 10, direction)
        for i in range(floors):
            self.nodes.append(StairJunction(i, [self]))

    def message(self, a, b):
        assert a.floor != b.floor
        if a.floor > b.floor:
            return "go down the staircase to the " + b.name + "."
        else:
            return "go up the staircase to the " + b.name + "."

    def get_floor(self, floor):
        return self.nodes[floor]

    def path_sign(self, a, b):
        return 0


class StairJunction(graph.Node):
    def __init__(self, floor, edges):
        graph.Node.__init__(self, "", edges)
        self.name = str_utils.ordinal(floor) + " Floor" if floor != 0 else "Ground Floor"
        self.floor = floor


# TODO: Remove class; replace with corridor() function?
class Corridor(graph.Edge):
    def __init__(self, rooms, avg_distance, location_dict, direction):
        graph.Edge.__init__(self, None, "corridor", avg_distance, direction)
        for room in rooms:
            node = graph.Node(room, [self])
            location_dict[room] = node
            self.nodes.append(node)


class InvisibleNode(graph.Node):
    pass
