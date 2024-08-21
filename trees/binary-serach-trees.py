from collections import deque
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class BST:
  def __init__(self, root=None):
    self.root = root
  
  def insert(self, root, target):
    if root:
      if root.val > target:
        if root.left:
          self.insert(root.left, target)
        else:
          root.left = TreeNode(target)
          return root.left
      else:
        if root.right:
          self.insert(root.right, target)
        else:
          root.right = TreeNode(target)
          return root.right
    else:
      self.root = TreeNode(target)

  def levelorder(self):
    if self.root == None:
      print('root is none')
      return
    q = deque([self.root])
    while len(q) > 0:
      root = q.popleft()
      print(f'{root.val}', end=', ')
      if root.left != None:
        q.append(root.left)
      if(root.right != None):
        q.append(root.right)

  def find(self, root, target):
    if root == None:
      return root
    while root:
      if root.val == target:
        return root
      if root.val < target:
        root = root.right
      else:
        root = root.left

  def find_min_node(self, root):
    while root.left != None:
      root = root.left
    return root

  def delete(self, root, target):
    print(f'del({root.val}, {target})')
    if root == None:
      return None
    elif target < root.val:
      root.left = self.delete(root.left, target)
      # print('left of',root.val, root.left.val if root.left else None)
    elif target > root.val:
      root.right = self.delete(root.right, target)
      # print('right of',root.val, root.right.val if root.right else None)


    else:
      #case 1 node have no children
      if root.left == None and root.right == None:
        # print('this shoul be 4', root.val)
        root = None
      
      #case2 node have only one children
      elif root.left == None:
        root = root.right
      elif root.right == None:
        root = root.left
      else:
      #case3 node have both the children
        min_node = self.find_min_node(root.right)
        root.val = min_node.val
        root.right = self.delete(root.right, min_node.val)
    return root
    
    
      

tree = BST()

tree.insert(tree.root, 6)
tree.insert(tree.root, 7)
tree.insert(tree.root, 3)
tree.insert(tree.root, 2)
tree.insert(tree.root, 5)
tree.insert(tree.root, 8)
tree.insert(tree.root, 1)
tree.insert(tree.root, 4)

tree.levelorder()
print()

tree.delete(tree.root, 6)

print()

tree.levelorder()

