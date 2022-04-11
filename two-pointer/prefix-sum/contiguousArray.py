from typing import List


class Solution:
    def contiguousArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1 

        ans = 0
        countTable = [0] * len(nums)
        for idx, num in enumerate(nums):
            changeInt = 1 if num == 1 else -1

            if idx == 0:
                countTable[0] += changeInt
            else:
                countTable[idx] += countTable[idx - 1] + changeInt

        return ans

    def leetCodeSolution(self, nums: List[int]) -> int:
        maxLength = 0
        hashmap = {}
        count = 0
        for idx in range(len(nums)):
            num = nums[idx]
            if num == 0:
                count -= 1
            else:
                count += 1

            if count == 0:
                maxLength = idx + 1

            if count in hashmap:
                maxLength = max(maxLength, idx - hashmap[count])
            else:
                hashmap[count] = idx 
        return maxLength


if __name__ == '__main__':
    # nums = [0, 1]
    nums = [0, 0, 1, 0, 0, 0, 1, 1]
    s = Solution()
    print(s.leetCodeSolution(nums))