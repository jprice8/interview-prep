import heapq


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: float) -> None:
        if len(self.min_heap) == 0 or num < self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self._balance()

    def findMedian(self) -> float:
        pass

    def _balance(self) -> None:
        if len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)


if __name__ == '__main__':
    finder = MedianFinder()
    finder.addNumber(1)
    finder.addNumber(2)
    print(finder.findMedian())
    finder.addNumber(3)
    print(finder.findMedian())