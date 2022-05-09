# n^2 time | O(n) where n is the number of elements in array
def threeSum(array, target):
    result = []
    array.sort()

    for c in range(len(array) - 2):
        l = c + 1
        r = len(array) - 1

        while l < r:
            cs = array[c] + array[l] + array[r]
            if cs == target:
                result.append([array[c], array[l], array[r]])
                l += 1
                r -= 1
            elif cs < target:
                l += 1
            elif cs > target:
                r -= 1

    return result


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue

            l, r = idx + 1, len(nums) - 1
            while l < r:
                currSum = num + nums[l] + nums[r]
                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-2, -2, 0, 0, 2, 2])) # [-2, 0, 2]

