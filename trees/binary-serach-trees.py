from collections import deque
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class BST:
  def __init__(self, root=None):
    self.root = root
  
  def insert_recursive(self, root, target):
    if root:
      if root.val > target:
        if root.left:
          self.insert(root.left, target)
        else:
          root.left = TreeNode(target)
      else:
        if root.right:
          self.insert(root.right, target)
        else:
          root.right = TreeNode(target)
    else:
      self.root = TreeNode(target)

  def levelorder(self):
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

tree.insert(tree.root, 6)
tree.insert(tree.root, 7)
tree.insert(tree.root, 3)
tree.insert(tree.root, 2)
tree.insert(tree.root, 1)
tree.insert(tree.root, 5)
tree.insert(tree.root, 4)


tree.levelorder()