class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def push(self, val):
        new_node = Node(val)
        if self.back is None:
            # If the queue is empty, both front and back are the new node
            self.front = self.back = new_node
        else:
            # Add the new node at the end and update back
            self.back.next = new_node
            self.back = new_node

    def pop(self):
        if self.front is None:
            raise IndexError("pop from empty queue")
        
        # Remove the front node
        removed_value = self.front.val
        self.front = self.front.next
        
        if self.front is None:
            # If the queue is empty now, update back to None
            self.back = None
        
        return removed_value

    def peek(self):
        if self.front is None:
            raise IndexError("peek from empty queue")
        
        # Return the value of the front node
        return self.front.val
