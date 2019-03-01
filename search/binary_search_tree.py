class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # run callback on self
    cb(self.value)
    
    # if there is a left value on self
    if self.left:
        # recurse function on left, passing in the callback
        self.left.depth_first_for_each(cb)
    # if there is a right value on self
    if self.right:
        # recurse function on right, passing in the callback
        self.right.depth_first_for_each(cb)   
        

  def breadth_first_for_each(self, cb):
    # create a queue starting at self
    queue = [self]
    # run a loop as long as the queue has a length > 0
    while len(queue):
      
      # remove first element and save to a variable
      current_node = queue.pop(0)
      # if the node has a left, append that onto the queue
      if current_node.left:
        queue.append(current_node.left)
      # if node has a right, append that onto the queue
      if current_node.right:
        queue.append(current_node.right)
      # run the function on the current node
      cb(current_node.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
