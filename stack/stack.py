class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next


class Stack:
  def __init__(self, top=None):
    self.top = top
  def push(self, val):
    new_node = Node(val)
    new_node.next = self.top
    self.top = new_node
    
  def pop(self):
    self.top = self.top.next
    
  def peek(self):
    return self.top.val
