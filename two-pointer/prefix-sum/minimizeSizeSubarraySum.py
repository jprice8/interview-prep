from typing import List


class Solution:
    def minSize(self, nums: List[int], target: int) -> int:
        minLength = float('inf')
        windowSum = nums[0]
        left, right = 0, 0 
        while right < len(nums):
            if windowSum >= target:
                # update min length
                minLength = min(minLength, right - left + 1)
                windowSum -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    windowSum += nums[right]
        return minLength if minLength != float('inf') else 0

    def neetcode(self, nums, target):
        l, total = 0, 0 
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res


if __name__ == '__main__':
    s = Solution()
    print(s.minSize([2, 3, 1, 2, 4, 3], 7))