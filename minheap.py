class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left

        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify(smallest)

    def heappush(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1
        
        while i != 0 and (self.heap[(i - 1) // 2][0] > self.heap[i][0]):
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def heappop(self):
        if len(self.heap) == 1:
            return self.heap.pop()

        res = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return res

    def replace(self, item):
        res = self.heap[0]
        self.heap[0] = item
        self.heapify(0)
        return res
