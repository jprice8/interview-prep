import heapq
import math
from typing import List, Tuple


class Solution:
    def kClosest(self, points: List[Tuple[int, int]], k: int) -> List[Tuple[int, int]]:
        heap = []
        for point in points:
            # Calculate distance
            distance = self.calculateDistance(point[0], point[1])
            # Insert (distance, idx) into heap)
            heapq.heappush(heap, (distance, point))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    def calculateDistance(self, x: int, y: int) -> int:
        x1, y1 = x, y 
        x2, y2 = 0, 0
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def minHeapThree(self, arr: List[int]) -> List[int]:
        heapq.heapify(arr)
        res = []
        for _ in range(3):
            res.append(heapq.heappop(arr))

        return res

    def maxHeapThree(self, arr):
        arr = [num * -1 for num in arr]
        heapq.heapify(arr)
        res = []
        for _ in range(3):
            res.append(-1 * heapq.heappop(arr))
        return res


if __name__ == '__main__':
    # arr = [10, 6, 8, 4, 5]
    points = [(1, 1), (2, 2), (3, 3)]
    s = Solution()
    print(s.kClosest(points, 2))