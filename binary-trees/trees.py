from collections import deque

class TreeNode:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        if(self.root == None):
            self.root = TreeNode(val)
        else:
            found = False
            node = self.root
            while(not found):
                if(node.val > val):
                    if(node.left != None):
                        node = node.left
                    else:
                        node.left = TreeNode(val)
                        break
                else:
                    if(node.right != None):
                        node = node.right
                    else:
                        node.right = TreeNode(val)
                        break

    def levelorder(self):
    # init a queue
    # i need to put the root inside the queue
    # for every element inside the queue
    # take the first element, root left, the element's right should be added to the queue
    # print the popped out element;
        if self.root == None:
            print('root is none')
            return
        q = deque([self.root])
        while len(q) > 0:
            root = q.popleft()
            print(root.val)
            if root.left != None:
                q.append(root.left)
            if(root.right != None):
                q.append(root.right)

tree = BST()
tree.insert(6)
tree.insert(7)
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(5)
tree.insert(4)
tree.insert(9)
tree.insert(8)

tree.levelorder()

    
