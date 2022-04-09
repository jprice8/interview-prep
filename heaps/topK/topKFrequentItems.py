from ast import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        if len(nums) <= k:
            return nums
        
        numCount = Counter(nums)

        minHeap = []
        for num, count in numCount.items():
            heapq.heappush(minHeap, (-count, num))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res


if __name__ == '__main__':
    nums = [4, 1, -1, 2, -1, 2, 3]
    s = Solution()
    print(s.topKFrequent(nums, 2))