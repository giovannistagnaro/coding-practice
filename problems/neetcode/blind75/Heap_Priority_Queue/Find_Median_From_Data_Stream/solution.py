import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) > 0 and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        min_len = len(self.minHeap)
        max_len = len(self.maxHeap)
        if max_len - min_len > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif max_len - min_len < -1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            a, b = self.minHeap[0], -self.maxHeap[0]
            return (a + b) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            a = self.minHeap[0]
            return a
        else:
            b = -self.maxHeap[0]
            return b