class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            self.heap[index] = self.heap[self.parent(index)]
            self.heap[self.parent(index)] = self.heap[index]
            index = self.parent(index)

    def heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] >= self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] >= self.heap[largest]:
            largest = right

