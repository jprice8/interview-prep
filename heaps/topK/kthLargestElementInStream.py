import heapq
from typing import List


class Solution:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # create max heap
        nums = [-i for i in nums]
        heapq.heapify(nums)

        # create min heap
        self.min_heap = []
        for _ in range(k):
            if nums:
                polled = heapq.heappop(nums)
                heapq.heappush(self.min_heap, -polled)

    def add(self, val: int) -> int:
        # Not k elements in min heap yet
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)

        # At least k in min heap
        elif val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]


if __name__ == '__main__':
    s = Solution(1, [])
    print(s.add(-3))
    print(s.add(-2))
    print(s.add(-4))
    print(s.add(0))
    print(s.add(4))
