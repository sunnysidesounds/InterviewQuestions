class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    return self.top.value

  def push(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.top = new_node
      self.bottom = new_node
    else:
      previous_top = self.top
      self.top = new_node
      self.top.next = previous_top

    self.length += 1
    return self.top

  def pop(self):
    if self.length == 0 or self.top == None:
      return None

    if self.top == self.bottom:
      self.bottom = None
    self.top = self.top.next

    return self.top

  def is_empty(self):
    return False if self.length == 0 else True
