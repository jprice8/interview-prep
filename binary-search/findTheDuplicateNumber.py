from typing import List


class Solution:
    def findTheDuplicate(self, nums: List[int]) -> int:
        # low and hgih represents the range of values of the target
        low = 1
        high = len(nums) - 1

        while low <= high:
            curr = (low + high) // 2
            count = 0

            # Count how many numbers are less than or equal to curr
            count = sum(num <= curr for num in nums)
            if count > curr:
                duplicate = curr 
                high = curr - 1
            else:
                low = curr + 1
        return duplicate

    def tortoiseAndHare(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break 

        # Find the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare

if __name__ == '__main__':
    s = Solution()
    print(s.findTheDuplicate([1, 3, 4, 2, 4]))