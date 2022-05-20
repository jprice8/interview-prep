from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        def mergeSort(nums):
            # base case
            if len(nums) < 2:
                return nums

            # recursive calls
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)

        def merge(left, right):
            merged = [0] * (len(left) + len(right))
            k = l = r = 0

            # merge left and right
            while l < len(left) and r < len(right):
                if left[l][1] <= right[r][1]:
                    result[left[l][0]] += r
                    merged[k] = left[l]
                    l += 1
                else:
                    merged[k] = right[r]
                    r += 1
                k += 1

            # finish left
            while l < len(left):
                result[left[l][0]] += r
                merged[k] = left[l]
                l += 1
                k += 1

            # finish right
            while r < len(right):
                merged[k] = right[r]
                r += 1
                k += 1

            return merged

        mergeSort(list(enumerate(nums)))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.countSmaller([5, 2, 6, 1]))