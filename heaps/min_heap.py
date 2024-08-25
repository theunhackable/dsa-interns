class MinHeap:
  def __init__(self):
    self.heap = []
  def top(self):
    if len(self.heap) == 0:
      return None
    return self.heap[0]
  
  def insert(self, val):
    self.heap.append(val)
    self.heapify_up(len(self.heap) - 1)

  def heapify_up(self, ind):
    if ind <= 0:
      return
    parent_ind = self.parent_index(ind)
    parent_val = self.heap[parent_ind]
    ind_val = self.heap[ind]
    if(parent_val > ind_val):
      # swap
      self.heap[ind] = parent_val
      self.heap[parent_ind] = ind_val
      # and check again
      self.heapify_up(parent_ind)

  def print_heap(self):
    for ele in self.heap:
      print(ele, end=', ')
    print()

  def parent_index(self, ind):
    return (ind - 1) // 2 
  def left_child_index(self, ind):
    return 2 * ind + 1
  def right_child_index(self, ind):
    return 2 * ind + 2
  


heap = MinHeap()

heap.insert(14)
heap.insert(12)
heap.insert(10)
heap.insert(9)
heap.insert(5)
heap.insert(4)
heap.insert(7)
heap.insert(2)
heap.insert(3)

heap.print_heap()