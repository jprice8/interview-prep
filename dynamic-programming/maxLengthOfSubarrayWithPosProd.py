class Solution:
    def maxLengthPosProd(self, nums):
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]

        # base case
        if nums[0] > 0:
            dp[0][0] = 1

        if nums[0] < 0:
            dp[0][1] = 1

        res = dp[0][0]
        for i in range(1, n):
            cur = nums[i]

            if cur > 0:
                dp[i][0] = dp[i - 1][0] + 1
                

if __name__ == '__main__':
    nums = [1, -2, -3, 4]
    s = Solution()
    print(s.maxLengthPosProd(nums))