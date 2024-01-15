class Node(object) :
  def __init__(self,data) :
    self.data = data
    self.left = None
    self.right = None

class BinaryTree(object) :
  def NodeBaru(self,data) :
    return Node(data)

  def Insert(self,data,root) :
    if root is None :
      return self.NodeBaru(data)
    else :
      if data < root.data :
        root.left = self.Insert(data,root.left)
      else :
        root.right = self.Insert(data,root.right)
    return root
  
  def PreOrder(self,root) :
    if root is not None :
      print(root.data, end=" ")
      self.PreOrder(root.left)
      self.PreOrder(root.right)

  def InOrder(self,root) :
    if root is not None :
      self.InOrder(root.left)
      print(root.data, end=" ")
      self.InOrder(root.right)

  def PostOrder(self,root) :
    if root is not None :
      self.PostOrder(root.left)
      self.PostOrder(root.right)
      print(root.data, end=" ")

# PohonBiner
x = BinaryTree()
#             12
#         /        \
#        8         22
#      /  \      / 
#     4   10   19        
#   / \   /     \
#  2  6  9      20

rt = x.NodeBaru(12) #root
x.Insert(22,rt)
x.Insert(8,rt)
x.Insert(19,rt)
x.Insert(10,rt)
x.Insert(9,rt)
x.Insert(20,rt)
x.Insert(4,rt)
x.Insert(2,rt)
x.Insert(6,rt)

print("-Data PreOrder-")
x.PreOrder(rt)
print("\n-Data InOrder-")
x.InOrder(rt)
print("\n-Data PostOrder-")
x.PostOrder(rt)