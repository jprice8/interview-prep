import collections
from typing import List


class Solution:
    def subsum(self, arr: List[int], target: int) -> List[int]:
        pMap = collections.defaultdict(int)

        runningSum = 0
        for idx, num in enumerate(arr):
            runningSum += num
            pMap[runningSum] = idx

            # check if ans is in map
            delta = runningSum - target
            if delta in pMap:
                return [pMap[delta + 1], idx]


if __name__ == '__main__':
    arr = [1, 3, 2, 5, 4]
    s = Solution()
    print(s.subsum(arr, 5))