from typing import List


class Solution:
    def mountainPeak(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        boundary_idx = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1]:
                boundary_idx = mid 
                r = mid - 1
            else:
                l  = mid + 1
        return boundary_idx

if __name__ == '__main__':
    arr = [0, 1, 2, 3, 2, 1]

    s = Solution()
    print(s.mountainPeak(arr))