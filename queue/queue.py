class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class Queue:
    def __init__(self, top=None, back=None):
        self.top = top
        self.back = back

    def push(self, val):
        if self.top == None:
           self.top = Node(val)
           self.back = self.top
           return
        else:
            self.back.next = Node(val)
        self.back = self.back.next
    
    def pop(self):
       if self.top == None:
          return
       self.top = self.top.next

    def peek(self):
       if self.top == None:
          return None
       return self.top.val
       

q1 = Queue()
#testing edge case peek
print(q1.peek())
#testing edge case pop
q1.pop()
#testing edge case push
q1.push(1)
#testing regular push
q1.push(2)
q1.push(3)
#testing regular peek
print(q1.peek())
#testing regular pop
q1.pop()
print(q1.peek())
q1.pop()
print(q1.peek())

