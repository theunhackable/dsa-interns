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
  
  def delete(self):
    if len(self.heap) == 0:
      return
    if len(self.heap) == 1:
      self.heap = []
      return
    # replace first element with the last element
    self.heap[0] = self.heap[-1]
    # remove the last element
    self.heap.pop()
    # heapifydown the heap
    self.heapify_down(0)

  def heapify_down(self, ind):
    print(ind)
    # what if the index is out of range
    if ind >= len(self.heap) - 1:
      return
    # get the left child index and right child index
    left_child_ind = self.left_child_index(ind)
    right_child_ind = self.right_child_index(ind)

    # get the values of parent, left child and right child
    parent_val = self.heap[ind]
    left_child_val = self.heap[left_child_ind]
    right_child_val = -1
    if right_child_ind < len(self.heap):
      right_child_val = self.heap[right_child_ind]

    # take the min of the children and compare it with the parent
    if left_child_val < right_child_val and left_child_val < parent_val:
      self.heap[left_child_ind] = parent_val
      self.heap[ind] = left_child_val
      # repeat the same thing for the newly updated node
      self.heapify_down(left_child_ind)
    
    elif right_child_ind < len(self.heap) and right_child_val < left_child_val and right_child_val < parent_val:
      self.heap[right_child_ind] = parent_val
      self.heap[ind] = right_child_val
      # repeat the same thing for the newly updated node
      self.heapify_down(right_child_ind)


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

print('insertions completed')
heap.print_heap()

heap.delete()
print('after poping')
heap.print_heap()
