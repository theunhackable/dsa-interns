class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, top=None):
        self.top = top
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top 
        self.top = new_node 

    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        popped_node = self.top
        self.top = self.top.next 
        return popped_node.data 

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        return self.top.data 
    def display(self):
        current_node = self.top
        while current_node:
            print(current_node.data, end=",")
            current_node = current_node.next

stk=Stack()
for i in range(10):
    n=int(input("Enter values to push : "))
    stk.push(n)
print(stk.peek())
print(stk.pop())
stk.display()
