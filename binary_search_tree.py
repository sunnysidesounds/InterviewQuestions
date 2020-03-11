import json

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
    return tree


  def pretty(self, d, indent=0):
    for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
        self.pretty(value, indent+1)
      else:
        print('\t' * (indent+1) + str(value))
