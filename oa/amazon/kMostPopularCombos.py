import heapq
import random
from typing import List

# TODO 1) Dedup like AM subsets

class Solution:
    def kMostPopularDedup(self, popularity: List[int], k: int) -> List[int]:
        n = len(popularity)
        res = [[]]
        def dfs(i, curr):
            nonlocal n 
            nonlocal res
            if i == n:
                return 

            res.append(curr + [popularity[i]])
            dfs(i + 1, curr + [popularity[i]])
            dfs(i + 1, curr)

        dfs(0, [])
        return res

    def kMostPrefixSum(self, popularity: List[int], k: int) -> List[int]:
        sumHeap = [0]
        # O(n ^ 2 * log(k))
        for i in range(len(popularity)):
            curSum = 0
            for j in range(i, len(popularity)):
                curItem = popularity[j]
                curSum += curItem

                # insert into heap
                if len(sumHeap) < k:
                    heapq.heappush(sumHeap, curSum)
                elif curSum > sumHeap[0]:
                    heapq.heapreplace(sumHeap, curSum)

        # O(k)
        sumHeap.reverse()
        return sumHeap


def generatePopularity(popLength) -> List[int]:
    """
    1 <= len(popularity) <= 10k
    -10^9 <= popularity[i] <= 10^9
    """
    return [random.randint(-(10 ** 9), 10 ** 9) for _ in range(popLength)]


def generateK(n) -> int:
    """1 <= k <= min(2000, 2^n)"""
    return random.randint(1, min(2000, 2 ** n))


if __name__ == '__main__':
    pop = generatePopularity(1000)
    k = generateK(len(pop))
    # pop = [3, 5, -2]
    # k = 3
    s = Solution()
    print(s.kMostPrefixSum(pop, k))