from typing import List


class Solution:
    def firstOccurence(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        ans_idx = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                ans_idx = mid 
                right = mid - 1
        return ans_idx


if __name__ == '__main__':
    s = Solution()
    print(s.firstOccurence([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 1))