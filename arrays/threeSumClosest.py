from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # diff = float('inf')
        # nums.sort()
        
        # for idx, num in enumerate(nums):
        #     l, r = idx + 1, len(nums) - 1
        #     while l < r:
        #         currSum = num + nums[l] + nums[r]
        #         if abs(target - currSum) < abs(diff):
        #             diff = target - currSum 
        #         if currSum > target:
        #             r -= 1
        #         elif currSum <= target:
        #             l += 1

        #     if diff == 0:
        #         break
                    
        # return target - diff

        bestSum = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == target:
                    return currSum

                if abs(currSum - target) < abs(bestSum - target):
                    bestSum = currSum

                if currSum < target:
                    l += 1
                elif currSum > target:
                    r -= 1
        return bestSum


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1)) # 2