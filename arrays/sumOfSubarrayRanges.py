from typing import List


class Solution:
    def sumOfSubarrayRanges(self, nums: List[int]) -> int:
        res = 0
        tmpArray = [float('-inf')] + nums + [float('-inf')]
        stack = []

        for idx, val in enumerate(tmpArray):
            while stack and tmpArray[stack[-1]] > val:
                currentMax = stack.pop()
                currentMin = stack[-1]
                res -= tmpArray[currentMax] * (idx - currentMax) * (currentMax - currentMin)
            stack.append(idx)

        tmpArray = [float('inf')] + nums + [float('inf')]
        stack = []
        for idx, val in enumerate(tmpArray):
            while stack and tmpArray[stack[-1]] < val:
                j = stack.pop()
                k = stack[-1]
                res += tmpArray[j] * (idx - j) * (j - k)
            stack.append(idx)

        return res
        

if __name__ == '__main__':
    nums = [4, -2, -3, 4, 1] # 59
    nums2 = [1, 2, 3] # 4
    nums3 = [1, 3, 3] # 4
    s = Solution()
    print(s.sumOfSubarrayRanges(nums))