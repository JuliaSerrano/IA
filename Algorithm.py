import heapq
from datos import get_neighbours, get_line, get_distance_f, get_distance_g, get_distance_h


class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, name=None):
        self.parent = parent
        self.name = name
        self.g = 0
        self.h = 0
        self.f = 0

    # defining less than for purposes of heap queue
    def __lt__(self, other):
        return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
        return self.f > other.f

    def __eq__(self, other):
        return self.name == other.name


def return_path(current_node):

    path = []
    current = current_node
    while current is not None:
        path.append(current.name)
        current = current.parent
    return path[::-1]  # Return reversed path


def a_star_algorithm(start, end):
    linea_actual = get_line(start)
    start_node = Node(None, start,)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node.name == end_node.name:
            return return_path(current_node)

        # Generate children
        children = get_neighbours(current_node.name).keys()
        # print(children)
# dict_keys(['Attiki', 'Omonia'])

        for child in children:  # neighbours

            child = Node(current_node, child)
            # print(f"Child: {child.name}\n")

            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                # print(f"{child.name} in close list\n")
                continue

            # child not in close list
                # Create the f, g, and h values
            child.g = get_distance_g(current_node.name, child.name)
            child.h = get_distance_h(end_node.name, child.name)
            child.f = child.g + child.h


# si siguiente estacion varios -> mantengo linea
# si siguiente distinta linea -> penalizo

            try:
                line = get_line(child.name)
                len(line)

            # varias lineas -> mantengo
            except TypeError:
                linea_actual
            else:
                if(line != linea_actual):
                    child.g = child.g + 5
                    child.f = child.g + child.h

            # print(f"{child.name} is not in close list. G: {child.g} H: {child.h}\n")

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.name == open_node.name and child.g > open_node.g]) > 0:
                # print(f"{child.name} is already in open list\n")
                continue

            # Add the child to the open list
            # print(f"{child.name} added to the open list\n")
            heapq.heappush(open_list, child)
