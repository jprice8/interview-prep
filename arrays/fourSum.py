class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res, quad = [], []
        
        def kSum(k, start, target):
            # base
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            
            # two sum II
            l, r = start, len(nums) - 1
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum < target:
                    l += 1
                elif currSum > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        kSum(4, 0, target)
        return res

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    s = Solution()
    print(s.fourSum(nums, target))