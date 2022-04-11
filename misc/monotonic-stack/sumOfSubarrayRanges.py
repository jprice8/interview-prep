from typing import List


class Solution:
    def sumOfRanges(self, nums: List[int]) -> int:
        maxStack = []
        minStack = []

        # fill max stack
        for num in nums:
            # update max
            return

    def lcSolution(self, numbers):
        res = 0
        inf = float('inf')
        nums = [-inf] + numbers + [-inf]
        stack = []
        # always increasing (min stack)
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                curr = stack.pop()
                stackTop = stack[-1]
                res -= nums[curr] * (curr - stackTop) * (idx - curr) # curr * left distance * right distance
            stack.append(idx)

        nums = [inf] + numbers + [inf]
        stack = []
        # always decreasing (max stack)
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                curr = stack.pop()
                stackTop = stack[-1]
                res += nums[curr] * (curr - stackTop) * (idx - curr) # curr * left distance * right distance
            stack.append(idx)

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.lcSolution([1, 2, 3]))