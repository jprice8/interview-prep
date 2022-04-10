import random
from typing import List


class Solution:
    def __repr__(self) -> str:
        return str(self.prefixSums)

    def __init__(self, w: List[int]):
        self.prefixSums = []
        prefixSum = 0
        for weight in w:
            prefixSum += weight 
            self.prefixSums.append(prefixSum)
        self.totalSum = prefixSum

    def pickIndex(self) -> int:
        target = self.totalSum * random.random()
        # linear search to find target zone
        for idx, pSum in enumerate(self.prefixSums):
            if target < pSum:
                return idx

    def pickIndexUltra(self) -> int:
        target = self.totalSum * random.random()
        # bsearch
        l, r = 0, len(self.prefixSums) - 1
        boundary_idx = -1 
        while l <= r:
            mid = (l + r) // 2
            if target < self.prefixSums[mid]:
                boundary_idx = mid
                r = mid - 1
            else:
                l = mid + 1
        return boundary_idx




if __name__ == '__main__':
    # w = [4, 3, 2, 1]
    w = [1, 2, 3, 4]
    s = Solution(w)
    print(s.pickIndexUltra())