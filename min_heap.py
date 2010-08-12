class minHeap:

  def __init__(self, heapSize):
    self.heap = []
    self.maxSize = heapSize
    self.min_element = None
    self.max_element = None

  def insert(self, item):
    if self.min_element == None:
      self.heap.append(item)
      self.min_element = item
      self.max_element = item

    elif item > self.max_element and len(self.heap) >= self.maxSize:
      print "element too big"

    elif item < self.min_element:
      self.min_element = item
      self.heap.append(item)

    else:
      self.heap.append(item)

    if len(self.heap) > self.maxSize:
      self.remove_max()
      
  def remove_max(self):
    max_item = self.heap[0]
    for item in self.heap:
      if item > max_item:
        max_item = item
    self.heap.remove(max_item)

  def print_heap(self):
    print self.heap


heap = minHeap(10)

for i in range(0, 15):
  heap.insert(i)

heap.print_heap()


