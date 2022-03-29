from typing import List


class Solution:
    def findingBoundary(self, arr: List[bool]) -> int:
        l, r = 0, len(arr) - 1
        boundary_idx = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid]:
                r = mid - 1
                boundary_idx = mid
            else:
                l = mid + 1

        return boundary_idx


if __name__ == '__main__':
    arr = [False, False, False, True]
    s = Solution()
    print(s.findingBoundary(arr))