"""

  You're given a <span>Node</span> class that has a <span>name</span> and an
  array of optional <span>children</span> nodes. When put together, nodes form a
  simple tree-like structure.

  Implement the <span>depthFirstSearch</span> method on the
  <span>Node</span> class, which takes in an empty array, traverses the tree
  using the Depth-first Search approach (specifically navigating the tree from
  left to right), stores all of the nodes' names in the input array, and
  returns it.

  If you're unfamiliar with Depth-first Search, we recommend watching the Conceptual
  Overview section of this question's video explanation before starting to code.

Sample Input
graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K

Sample Output
["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

"""

class Node:

    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def breadith_first_search(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop()
            array.append(current.name)
            for child in current.children:
                queue.append(child)

            return array




