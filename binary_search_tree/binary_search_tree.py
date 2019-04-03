class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value == self.value: #is in the tree already
      return
    elif value < self.value:
      if self.left:
           self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    else:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left:
        return self.left.contains(target)
      else:
        return False
    else:
      if self.right:
        return self.right.contains(target)
      else:
        return False   


    #pass

  def get_max(self):
    max_node = self
    #find the max node by traversing down the tree
    while max_node:
      if not max_node.right: #if there is no more right node
        return max_node.value #return the current max_node value
      max_node = max_node.right #move down the tree one step to the right



    #pass

  
  def for_each(self, cb):
    cb(self.value)
    if self.right and self:
      self.right.for_each(cb)
    if self.left and self:
      self.left.for_each(cb)
    return cb(self.value)  
      
    #pass

 