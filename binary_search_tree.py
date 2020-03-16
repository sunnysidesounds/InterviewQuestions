
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
      node = self.root      
      while(node != None):
        if value < node.value:
          if node.left == None:
            node.left = new_node
            return node
          node = node.left
        else:
          if node.right == None:
            node.right = new_node
            return node
          node = node.right
       
  def lookup(self, value):
    if self.root == None:
      return None
    node = self.root
    while(node != None):
      if value <= node.value:
        node = node.left
      elif value > node.value:
        node = node.right
      elif node.value == value:
        return node
    return None

  def remove(self, value):
    # Code here
    print()

  def traverse(self, node):
    tree = {}
    tree['value'] = node.value
    tree['left'] = None if node.left == None else self.traverse(node.left)
    tree['right'] = None if node.right == None else self.traverse(node.right)
    print(tree)

  def breath_first_search(self):
    current_node = self.root
    output = []
    queue = []
    queue.append(current_node)
    while(len(queue) > 0):
      current_node = queue.pop()
      output.append(current_node)
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)

    return output

  def validate_a_bst(self):
    current_node = self.root
    queue = []
    while(len(queue) > 0):
      current_node = queue.pop()
      if current_node.left.value < current_node.right.value:
        if current_node.left:
          queue.append(current_node.left)
        if current_node.right:
          queue.append(current_node.right)
      else:
        return False

    return True




