class Solution:
    # O(n) time | O(1) space
    def optimalSolution(self, nums):
        res = max(nums)
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num 
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)

        return res
            
    def optimalSolution2(self, nums):
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for idx in range(1, len(nums)):
            curr = nums[idx]

            tmp_max = max(curr, curr * max_so_far, curr * min_so_far)
            min_so_far = min(curr, curr * max_so_far, curr * min_so_far)

            max_so_far = tmp_max

            result = max(max_so_far, result)

        return result



if __name__ == '__main__':
    # nums = [2, 3, -2, 4]
    nums = [-3, -1, -1]
    s = Solution()
    print(s.optimalSolution2(nums))