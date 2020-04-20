
class Node :
  def __init__(self, value):
    self.value = value 
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = Node(None)
    self.tail = self.head
    self.length = 0

  def printList(self):
    array = [];
    currentNode = self.head;
    while(currentNode != None):
        array.append(currentNode.value)
        currentNode = currentNode.next
    
    print(array)

  def add(self, value):
    newNode = Node(value)
    current = self.head
    while(current.next != None):
      current = current.next
    current.next = newNode
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


  def reverse(self):
    previous = None
    current = self.head  
    while(current != None):
      next = current.next
      current.next = previous
      previous = current
      current = next          
    self.head = previous
    return self.head
