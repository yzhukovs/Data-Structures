class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

    #pass

  def delete(self):
    if len(self.storage) == 0:
      return None
    elif len(self.storage) == 1:
      return self.storage.pop()
    return_value = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return return_value  
    #pass

  def get_priority(self):
    return self.storage[0]
    #pass

  def get_size(self):
    return len(self.storage)
    #pass

  def _bubble_up(self, index):
    
    if index == 0: #if first one in the heap and none above it just return
      return
    parent_index = ((index + 1) // 2) - 1  
    if self.storage[index] > self.storage[parent_index]: #if node is larger than parent
      self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index] #swap
      return self._bubble_up(parent_index)
    #pass

  def _sift_down(self, index):
    # get first child
    first_child_index = (index + 1) * 2 - 1
        # if no child
    if first_child_index > len(self.storage) - 1:
      return
        # if one child
    elif first_child_index == len(self.storage) - 1:
      if self.storage[index] < self.storage[first_child_index]:
                # swap parent and child - O(1)
          self.storage[index], self.storage[first_child_index] = self.storage[first_child_index], self.storage[index]
                #  increment to prepare for next loop
          return self._sift_down(first_child_index)
        # has two children
    else:
      second_child_index = first_child_index + 1
      larger_index = first_child_index
      second_is_larger = False
      if self.storage[second_child_index] > self.storage[first_child_index]:
        larger_index = second_child_index
        second_is_larger = True
      if self.storage[index] < self.storage[larger_index]:
        # swap parent and child - O(1)
        self.storage[index], self.storage[larger_index] = self.storage[larger_index], self.storage[index]
          #  increment to prepare for next loop
        return self._sift_down(larger_index)
    #pass
