class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value): # O(log(n))
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)
    #pass

  def delete(self):
    if len(self.storage) == 0:
      return
    if len(self.storage) == 1:
      return self.storage.pop()
    minValue = self.storage[0]
    self.storage[0] = self.storage.pop()
    self._sift_down(0)
    return minValue
  

  def get_max(self):
    return self.storage[0]
    #pass

  def get_size(self):
    return len(self.storage)
    #pass

  def _bubble_up(self, index):
    if index <= 0:
      return
    parentIndex = (index - 1) // 2
    if self.storage[parentIndex] < self.storage[index]:
      swap = self.storage[index]
      self.storage[index] = self.storage[parentIndex]
      self.storage[parentIndex] = swap
      self._bubble_up(parentIndex)
    #pass

  def _sift_down(self, index):
    leftChildIndex = index * 2 + 1
    rightChildIndex = index * 2 + 2

    if leftChildIndex > len(self.storage) and rightChildIndex > len(self.storage):
      if self.storage[leftChildIndex] > self.storage[rightChildIndex]:
        maxChildIndex = leftChildIndex
      else:
        maxChildIndex = rightChildIndex
    elif leftChildIndex > len(self.storage):
      maxChildIndex = leftChildIndex
    else:
      maxChildIndex = rightChildIndex

    if maxChildIndex >= len(self.storage):
        return
    if self.storage[index] > self.storage[maxChildIndex]:
       swap = self.storage[maxChildIndex]
       self.storage[maxChildIndex] = self.storage[index]
       self.storage[index] = swap
       self._sift_down(maxChildIndex)
    #pass
