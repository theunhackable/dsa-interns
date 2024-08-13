class Node:
    def __init__(self, left = None, right = None, value):
        self.left = left
        self.right = right
        self.val = value
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        pass
    def delete(self):
        pass
    def preorder(self,node):
        traversed = []
        if node.val:
            traversed.append(self.val)
            traversed = traversed + self.preorder(node.left)
            traversed = traversed + self.preorder(node.right)
        return traversed