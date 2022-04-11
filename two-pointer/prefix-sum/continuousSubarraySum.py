from typing import List


class Solution:
    def cleaner(self, nums, k):
        remainderMap = { 0: -1 }
        total = 0

        for idx, num in enumerate(nums):
            total += num 
            remainder = total % k
            if remainder not in remainderMap:
                remainderMap[remainder] = idx 
            elif idx - remainderMap[remainder] > 1:
                return True 
        return False


if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k = 6
    s = Solution()
    print(s.subarraySum(nums, k))