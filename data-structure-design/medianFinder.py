import heapq
from typing import Any, List


class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


    def printHeaps(self) -> Any:
        print('Large Heap')
        print(self.large)
        print('Small Heap')
        print(self.small)


if __name__ == '__main__':
    obj = MedianFinder()
    print(obj.printHeaps())
    print(obj.addNum(3))
    print(obj.printHeaps())
    print(obj.addNum(2))
    print(obj.printHeaps())
    print(obj.addNum(7))
    print(obj.printHeaps())
    print(obj.addNum(4))
    print(obj.printHeaps())
    print(obj.addNum(10))
    print(obj.printHeaps())
    print(obj.findMedian()) # 4
    print(obj.printHeaps())
    print(obj.addNum(3)) 
    print(obj.printHeaps())
    print(obj.findMedian()) 