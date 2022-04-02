import heapq
from typing import List


class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        arr = [-i for i in arr]
        heapq.heapify(arr)
        for _ in range(k):
            top_item = heapq.heappop(arr)
        return -top_item


if __name__ == '__main__':
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    s = Solution()
    print(s.findKthLargest(arr, k))