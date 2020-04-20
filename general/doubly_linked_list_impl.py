
class Node:
  def __init__(self, value):
    self.value = value 
    self.previous = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = Node(None)
    self.tail = self.head
    self.length = 0

  def add(self, value):
    newNode = Node(value)
    current = self.head
    while(current.next != None):
      current = current.next
    current.next = newNode
    newNode.previous = current
    self.length += 1

  def get(self, value):
    if self.head == None:
      return None

    current = self.head
    while(current.next != None):
      current = current.next
      if value == current.value:
        break
      if current.next == None:
        return None
    
    return current.value

  def delete(self, value):
    if self.head == None:
      return
    current = self.head
    previous = None
    while(current.next != None and value != current.value):
      previous = current
      current = current.next
    if previous == None:
      self.head = self.head.next
      return
    if current.next == None:
      previous.next = None
      return
    previous.next = current.next
    self.length -= 1