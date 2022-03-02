class Solution:
    def findMinRotated(self, nums):
        left = 0
        right = len(array) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]

            


if __name__ == '__main__':
    array = []
    s = Solution()
    print(s.findMinRotated(array))