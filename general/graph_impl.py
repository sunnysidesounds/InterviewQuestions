
class Graph:
  def __init__(self):
    self.number_of_nodes = 0
    self.ajacent_list = {}

  def add_vertex(self, node):
    self.ajacent_list[node] = []
    self.number_of_nodes += 1

  def add_edge(self, node1, node2):
    if node1 in self.ajacent_list:
      self.ajacent_list[node1].append(node2)
    else:
      self.add_vertex(node1)
      self.ajacent_list[node1].append(node2)

    if node2 in self.ajacent_list:
      self.ajacent_list[node2].append(node1)
    else:
      self.add_vertex(node2)
      self.ajacent_list[node2].append(node1)

  def show_connections(self):
    all_nodes = self.ajacent_list.keys
    for node in all_nodes:
      node_connections = self.ajacent_list[node]
      connections = ""
      for vertext in node_connections:
        connections += vertext + " "
      print("{node} --> {connections}".format(node=node, connections=connections))





#if __name__ == '__main__':

