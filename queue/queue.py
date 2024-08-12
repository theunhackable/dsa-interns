class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next


class Queue:
  def __init__(self, front=None, back=None):
    self.front = front
    self.back = back
  def push(self, val):
    #add element to the end of the ll
    new_node = Node(val)
    if self.back == None:
      self.front = new_node
      self.back = new_node  
    else:
      new_node.next = self.back 
      self.back = new_node 
    
  def pop(self):
    # remove first element from the ll
    pass
  def peek(self):
    #return the first element
    pass