class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        total_max = nums[0]

        for idx in range(1, len(nums)):
            current_num = nums[idx]
            current_sum = max(current_sum + current_num, current_num)

            total_max = max(total_max, current_sum)

        return total_max


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(nums))