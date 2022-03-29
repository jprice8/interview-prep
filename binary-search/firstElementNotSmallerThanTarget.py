from typing import List


class Solution:
    def firstElement(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        potential_match_idx = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                # discard all right
                right = mid - 1
                potential_match_idx = mid 
            else:
                left = mid + 1
        return potential_match_idx

if __name__ == '__main__':
    s = Solution()
    print(s.firstElement([1, 3, 3, 5, 8, 8, 10], 9))