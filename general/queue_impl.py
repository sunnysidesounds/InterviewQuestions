class Node :
  def __init__(self, value):
    self.value = value 
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def peek(self):
    return self.first

  def ennqueue(self, value):
    new_node = Node(value)
    if self.first == None and self.last == None:
      self.first = new_node
      self.last = new_node

    temp_node = self.first
    self.last = new_node
    self.last.next = temp_node
    self.length += 1
    return self.last

  def dequeue(self):
    if self.length == 0:
      return None

    if self.first == self.last:
      self.last = None

    self.first = self.first.next
    self.length -= 1

    return self.first

  def is_empty(self):
    return False if self.length == 0 else True




# Joy
# Matt
# Pavel
# Samir

