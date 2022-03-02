class Solution:
    def searchInSortedArray(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid 

            # left is sorted
            elif nums[left] <= nums[mid]:
                # Is target on this side?
                if nums[left] <= target < nums[mid]:
                    # yee
                    right = mid - 1
                else:
                    # no
                    left = mid + 1

            # right is sorted
            else:
                # Is target on this side?
                if nums[mid] < target <= nums[right]:
                    # yes
                    left = mid + 1
                else:
                    # no
                    right = mid - 1

        return -1



if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5]
    # nums = [2, 3, 4, 5, 1]
    # nums = [3, 4, 5, 1, 2]
    # nums = [4, 5, 1, 2, 3]
    nums = [4, 5, 6, 7, 0, 1, 2]
    s = Solution()
    print(s.searchInSortedArray(nums, 3))
