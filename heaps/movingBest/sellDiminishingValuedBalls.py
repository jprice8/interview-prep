import heapq
from typing import List


class Solution:
    def sellBalls(self, inventory: List[int], orders: int) -> int:
        max_heap = [-i for i in inventory]
        heapq.heapify(max_heap)
        res = 0

        for _ in range(orders):
            high_ball = heapq.heappop(max_heap)
            high_ball = -high_ball
            res += high_ball
            high_ball -= 1
            heapq.heappush(max_heap, -high_ball)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.sellBalls([3, 5], 6))