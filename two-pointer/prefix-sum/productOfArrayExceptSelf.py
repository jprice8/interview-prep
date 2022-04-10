from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        # first pass
        runningProduct = 1 * nums[0]
        for idx in range(1, len(nums)):
            ans[idx] = runningProduct
            # update running product
            runningProduct *= nums[idx]


        # second pass
        runningProduct = 1 * nums[-1]
        for idx in reversed(range(len(nums) - 1)):
            ans[idx] *= runningProduct
            runningProduct *= nums[idx]

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4] # [24, 12, 8, 6]
    s = Solution()
    print(s.productExceptSelf(nums))