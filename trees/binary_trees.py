from collections import deque
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Tree:
  def __init__(self, root=None):
    self.root = root
  def inorder(self, root):
    temp = root
    if temp == None:
      return
    self.inorder(temp.left)
    print(temp.val)
    self.inorder(temp.right)

  def preorder(self, root):
      # root , left, right
      temp = root
      if temp == None:
        return
      print(temp.val)
      self.preorder(temp.left)
      self.preorder(temp.right)

  def postorder(self, root):
      # root , left, right
      temp = root
      if temp == None:
        return
      self.postorder(temp.left)
      self.postorder(temp.right)
      print(temp.val)
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
    

root = TreeNode('super-wit')

testing = TreeNode('testing')
development = TreeNode('development')
muzology = TreeNode('muzology')
hipoint = TreeNode('hipoint')
leyland = TreeNode('leyland')
cksdevs = TreeNode('cksdevs')

root.left = testing
root.right = development

testing.left = muzology
testing.right = hipoint

development.left = leyland
development.right = cksdevs

tree = Tree(root)

# tree.inorder(root)

tree.levelorder()