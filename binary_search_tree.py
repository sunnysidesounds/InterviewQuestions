
class Node :
  def __init__(self, value):
    self.value = value 
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)
    if self.root == None:
      self.root = new_node      
    else:
      current_node = self.root      
      while(current_node != None):
        if value < current_node.value:
          if current_node.left != None:
            current_node.left = new_node

          current_node = current_node.left
        else:
          if current_node.right != None:
            current_node.right = new_node
          current_node = current_node.right
       
  def lookup(self, value):
    if self.root == None:
      return None
    node = self.root
    while(node != None):
      if value <= node.value:
        node = node.left
      elif value > node.value:
        node = node.right
      else:
        return node

  def remove(self, value):
    # Code here
    print()

  def traverse(self, node):
    tree = {}
    tree['value'] = node.value
    tree['left'] = None if node.left == None else self.traverse(node.left)
    tree['right'] = None if node.right == None else self.traverse(node.right)
    print(tree)
