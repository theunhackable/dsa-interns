class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next


class Stack:
  def __init__(self, top=None):
    self.top = top
  def push(self, val):
    self.top = Node(val, self.top)
    #add element to the top
    pass
  def pop(self):
    self.top = self.top.next
    # remove top element
    pass
  def peek(self):
    return self.top.val
    #return the top element
    pass

node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)

stack1 = Stack(node1)
print("TESTING PEEK: ")
print(stack1.peek())

print("TESTING PUSH: ")
stack1.push(0)
print(stack1.peek())

print("TESTING POP: ")
stack1.pop()
print(stack1.peek())


