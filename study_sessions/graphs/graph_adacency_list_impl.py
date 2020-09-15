class Node:

    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

    def __str__(self):
        return str(self.id) + ' connected to ' + str([x.id for x in self.connected_to])


class Graph:

    def __init__(self):
        self.node_list = {}
        self.num_nodes = 0

    def add_node(self, key):
        self.num_nodes += 1
        new_node = Node(key)
        self.node_list[key] = new_node
        return new_node

    def get_node(self, n):
        if n in self.node_list:
            return self.node_list[n]
        else:
            return None

    def add_edge(self, _from, _to, weight=0):
        if _from not in self.node_list:
            nv = self.add_node(_from)
            if _to not in self.node_list:
                nv = self.add_node(_to)

            self.node_list[_from].add_neighbor(self.node_list[_to], weight)

    def get_nodes(self):
        return self.node_list.keys()


    def __iter__(self):
        return iter(self.node_list.values())

    def __contains__(self, n):
        return n in self.node_list
