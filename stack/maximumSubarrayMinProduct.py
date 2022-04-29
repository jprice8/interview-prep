from itertools import accumulate
from typing import List


class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     prefix_sums = list(accumulate([0] + nums + [0]))
    #     stack = [] # (index, height)
    #     max_area = 0

    #     for i, h in enumerate(nums + [0]):
    #         start = i
    #         while stack and stack[-1][1] >= h:
    #             index, height = stack.pop()
    #             max_area = max(max_area, (prefix_sums[i] - prefix_sums[index]) * height)
    #             start = index
    #         stack.append((start, h))

    #     return max_area % (10**9 + 7)

    def maxSumMinProductLC(self, nums: List[int]) -> int:
        prefix_sums = list(accumulate([0] + nums + [0]))
        left = []
        maxArea = 0
        for i, h in enumerate(nums + [0]):
            start = i
            while left and h <= left[-1][1]:
                prevStart, prevH = left.pop()
                maxArea = max(maxArea, (prefix_sums[i] - prefix_sums[prevStart]) * prevH)
                start = prevStart
            left.append((start, h))
        return maxArea % (10 ** 9 + 7)

if __name__ == '__main__':
    # nums = [2, 3, 3, 1, 2]
    nums = [1, 2, 3, 2] # 14
    s = Solution()
    # print(s.maxProduct([2, 3, 3, 1, 2])) # 3 * (3 + 3) = 18
    print(s.maxSumMinProductLC(nums))